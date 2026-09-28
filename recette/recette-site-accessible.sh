#!/usr/bin/env bash
set -euo pipefail

# Usage :
#   recette/recette-site-accessible.sh            (depuis la racine du dépôt)
#
# Variante avec port du site :
#   recette/recette-site-accessible.sh 8888
#
# La commande lance la recette sur `site-accessible/`, génère les artefacts
# ShipGuard, puis sert le tableau de revue sur http://127.0.0.1:8888/.

RECETTE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$RECETTE_DIR/.." && pwd)"
DOCS_DIR="$(cd -- "$RECETTE_DIR/../docs" && pwd)"
export SHIPGUARD_SITE_DIR="$DOCS_DIR"
cd "$RECETTE_DIR"

HOST="${HOST:-127.0.0.1}"
PORT="${1:-${PORT:-8765}}"
SCOPE="${SHIPGUARD_SCOPE:-site-accessible}"
REVIEW_PORT="${SHIPGUARD_REVIEW_PORT:-8888}"
REVIEW_HOST="${SHIPGUARD_REVIEW_HOST:-127.0.0.1}"
REVIEW_URL="http://$REVIEW_HOST:$REVIEW_PORT/"
TOOLS_DIR="$ROOT_DIR/.tools"
SHIPGUARD_VISUAL_REVIEW_SKILL_DIR="$TOOLS_DIR/shipguard/plugins/shipguard/skills/sg-visual-review"
AGENT_BROWSER_BIN="$RECETTE_DIR/node_modules/.bin/agent-browser"

case "$(uname -m)" in
  arm64) BROWSER_PLATFORM="mac-arm64" ;;
  x86_64) BROWSER_PLATFORM="mac-x64" ;;
  *)
    echo "Erreur : architecture macOS non prise en charge : $(uname -m)." >&2
    exit 1
    ;;
esac

BROWSER_EXECUTABLE="$TOOLS_DIR/chrome-154.0.8037.57-$BROWSER_PLATFORM/chrome-$BROWSER_PLATFORM/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"

require_command() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "Erreur : commande introuvable : $name" >&2
    exit 1
  fi
}

port_is_busy() {
  local port="$1"
  if command -v lsof >/dev/null 2>&1; then
    lsof -nP -iTCP:"$port" -sTCP:LISTEN >/dev/null 2>&1
    return
  fi
  python3 - "$HOST" "$port" <<'PY'
import socket
import sys

host, port = sys.argv[1], int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sys.exit(0 if sock.connect_ex((host, port)) == 0 else 1)
PY
}

wait_for_url() {
  local url="$1"
  local tries=40
  for _ in $(seq 1 "$tries"); do
    if curl -fsS -o /dev/null "$url" 2>/dev/null; then
      return 0
    fi
    sleep 0.25
  done
  echo "Erreur : URL indisponible après attente : $url" >&2
  return 1
}

require_command node
require_command python3
require_command curl

if [[ ! -x "$AGENT_BROWSER_BIN" ]]; then
  echo "Erreur : agent-browser local est introuvable. Lancez make installer-recette." >&2
  exit 1
fi
if [[ ! -x "$BROWSER_EXECUTABLE" ]]; then
  echo "Erreur : navigateur local de recette introuvable. Lancez make installer-recette." >&2
  exit 1
fi
export PATH="$(dirname -- "$AGENT_BROWSER_BIN"):$PATH"
export AGENT_BROWSER_EXECUTABLE_PATH="$BROWSER_EXECUTABLE"
require_command agent-browser

if [[ ! -d "$DOCS_DIR/$SCOPE" ]]; then
  echo "Erreur : dossier de recette introuvable : $SCOPE" >&2
  exit 1
fi

if [[ ! -f "$DOCS_DIR/$SCOPE/index.html" ]]; then
  echo "Erreur : $SCOPE/index.html est introuvable." >&2
  exit 1
fi

mkdir -p visual-tests/_results/screenshots visual-tests/pages

for file in build-review.mjs _review-template.html review-smoke-test.mjs monitor-smoke-test.mjs; do
  if [[ ! -f "$SHIPGUARD_VISUAL_REVIEW_SKILL_DIR/$file" ]]; then
    echo "Erreur : asset ShipGuard introuvable : $SHIPGUARD_VISUAL_REVIEW_SKILL_DIR/$file" >&2
    echo "Lancez make installer-recette pour restaurer les dépendances locales." >&2
    exit 1
  fi
  cp "$SHIPGUARD_VISUAL_REVIEW_SKILL_DIR/$file" "visual-tests/$file"
done

while port_is_busy "$PORT"; do
  echo "Port $PORT déjà utilisé pour le site, essai du port $((PORT + 1))."
  PORT=$((PORT + 1))
done

BASE_URL="http://$HOST:$PORT"
SITE_LOG="visual-tests/_results/site-server.log"

python3 -m http.server "$PORT" --bind "$HOST" --directory "$DOCS_DIR" >"$SITE_LOG" 2>&1 &
SITE_PID=$!

cleanup_site() {
  if kill -0 "$SITE_PID" 2>/dev/null; then
    kill "$SITE_PID" 2>/dev/null || true
    wait "$SITE_PID" 2>/dev/null || true
  fi
}
trap cleanup_site EXIT

echo "Site de recette : $BASE_URL/$SCOPE/"
wait_for_url "$BASE_URL/$SCOPE/index.html"

set +e
node visual-tests/run-static-site.mjs "$BASE_URL" "$SCOPE"
RUN_STATUS=$?
set -e

cleanup_site
trap - EXIT

node visual-tests/build-review.mjs --stop >/dev/null 2>&1 || true

if [[ "${SHIPGUARD_SERVE_REVIEW:-1}" == "0" ]]; then
  node visual-tests/build-review.mjs
  echo "Tableau ShipGuard généré : visual-tests/_results/review.html"
  exit "$RUN_STATUS"
fi

echo "Tableau ShipGuard : $REVIEW_URL"
echo "Arrêt : Ctrl+C"

if [[ "${SHIPGUARD_OPEN_REVIEW:-1}" == "1" ]] && command -v open >/dev/null 2>&1; then
  (sleep 1 && open "$REVIEW_URL" >/dev/null 2>&1) &
fi

set +e
node visual-tests/build-review.mjs --serve --host="$REVIEW_HOST" --port="$REVIEW_PORT"
SERVE_STATUS=$?
set -e

if [[ "$RUN_STATUS" -ne 0 ]]; then
  exit "$RUN_STATUS"
fi
exit "$SERVE_STATUS"
