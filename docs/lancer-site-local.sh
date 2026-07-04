#!/usr/bin/env bash
#
# Lancement depuis le dépôt du site :
#   cd /Users/alex/Claude/projets-formations/IGPDE-Carinne-C/docs
#   ./lancer-site-local.sh
#
# Lancement avec un autre port :
#   ./lancer-site-local.sh 8888
#
# Le script affiche les URL locales à ouvrir, puis garde le serveur actif
# jusqu'à l'arrêt manuel avec Ctrl+C.
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$ROOT_DIR"

HOST="${HOST:-127.0.0.1}"
PORT="${1:-${PORT:-8765}}"

if [[ ! "$PORT" =~ ^[0-9]+$ ]]; then
  echo "Erreur : le port doit être un nombre." >&2
  exit 1
fi

if [[ ! -f "$DOCS_DIR/index.html" ]]; then
  echo "Erreur : site introuvable dans $DOCS_DIR." >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "Erreur : python3 est introuvable." >&2
  exit 1
fi

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

while port_is_busy "$PORT"; do
  echo "Port $PORT déjà utilisé, essai du port $((PORT + 1))."
  PORT=$((PORT + 1))
done

cd "$DOCS_DIR"

echo "Site local : http://$HOST:$PORT/index.html"
echo "Version inaccessible : http://$HOST:$PORT/site-inaccessible/"
echo "Aide correction : http://$HOST:$PORT/site-aide-correction/"
echo "Version accessible : http://$HOST:$PORT/site-accessible/"
echo "Arrêt : Ctrl+C"

exec python3 -m http.server "$PORT" --bind "$HOST"
