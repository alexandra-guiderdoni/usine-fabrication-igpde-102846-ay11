#!/usr/bin/env bash
# Installe les dépendances locales de la recette visuelle.
set -euo pipefail

RECETTE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$RECETTE_DIR/.." && pwd)"
TOOLS_DIR="$ROOT_DIR/.tools"
SHIPGUARD_DIR="$TOOLS_DIR/shipguard"
SHIPGUARD_URL="https://github.com/bacoco/ShipGuard.git"
SHIPGUARD_REF="v2.14.0"
SHIPGUARD_COMMIT="4aca1c7bf4653210f85c91a547a4e9d7e8ccf8ad"
SHIPGUARD_ASSETS_DIR="$SHIPGUARD_DIR/plugins/shipguard/skills/sg-visual-review"
AGENT_BROWSER_BIN="$RECETTE_DIR/node_modules/.bin/agent-browser"
BROWSER_VERSION="154.0.8037.57"

case "$(uname -m)" in
  arm64)
    BROWSER_PLATFORM="mac-arm64"
    BROWSER_ARCHIVE="chrome-mac-arm64.zip"
    BROWSER_SHA256="0e6b3439469c1b8b95b2e89c72ea29f7af00fb2c28a8878358a0b6002b6d3a64"
    BROWSER_LAYOUT="chrome-mac-arm64"
    ;;
  x86_64)
    BROWSER_PLATFORM="mac-x64"
    BROWSER_ARCHIVE="chrome-mac-x64.zip"
    BROWSER_SHA256="f6c0dff4662f1ffb01f63f9de3888ea95e4c634870a8b9f55e6d2208ba29a8a9"
    BROWSER_LAYOUT="chrome-mac-x64"
    ;;
  *)
    echo "Erreur : architecture macOS non prise en charge : $(uname -m)." >&2
    exit 1
    ;;
esac

BROWSER_URL="https://storage.googleapis.com/chrome-for-testing-public/$BROWSER_VERSION/$BROWSER_PLATFORM/$BROWSER_ARCHIVE"
BROWSER_DIR="$TOOLS_DIR/chrome-$BROWSER_VERSION-$BROWSER_PLATFORM"
BROWSER_EXECUTABLE="$BROWSER_DIR/$BROWSER_LAYOUT/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"

require_command() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "Erreur : commande introuvable : $name" >&2
    exit 1
  fi
}

verify_shipguard_assets() {
  local file
  for file in build-review.mjs _review-template.html review-smoke-test.mjs monitor-smoke-test.mjs; do
    if [[ ! -f "$SHIPGUARD_ASSETS_DIR/$file" ]]; then
      echo "Erreur : asset ShipGuard introuvable : $SHIPGUARD_ASSETS_DIR/$file" >&2
      exit 1
    fi
  done
}

install_shipguard() {
  if [[ -e "$SHIPGUARD_DIR" ]]; then
    if [[ ! -d "$SHIPGUARD_DIR/.git" ]]; then
      echo "Erreur : $SHIPGUARD_DIR existe mais n'est pas un clone ShipGuard." >&2
      echo "Supprimez ce dossier manuellement, puis relancez make installer-recette." >&2
      exit 1
    fi

    local current_commit
    current_commit="$(git -C "$SHIPGUARD_DIR" rev-parse HEAD)"
    if [[ "$current_commit" != "$SHIPGUARD_COMMIT" ]]; then
      echo "Erreur : ShipGuard local est sur $current_commit, attendu : $SHIPGUARD_COMMIT." >&2
      echo "Supprimez ce dossier manuellement, puis relancez make installer-recette." >&2
      exit 1
    fi
    return
  fi

  mkdir -p "$TOOLS_DIR"
  local temporary_clone
  temporary_clone="$(mktemp -d "$TOOLS_DIR/.shipguard.XXXXXX")"

  cleanup_clone() {
    rm -rf -- "$temporary_clone"
  }
  trap cleanup_clone RETURN

  git clone --depth 1 --branch "$SHIPGUARD_REF" "$SHIPGUARD_URL" "$temporary_clone"

  local installed_commit
  installed_commit="$(git -C "$temporary_clone" rev-parse HEAD)"
  if [[ "$installed_commit" != "$SHIPGUARD_COMMIT" ]]; then
    echo "Erreur : ShipGuard installé sur $installed_commit, attendu : $SHIPGUARD_COMMIT." >&2
    exit 1
  fi

  mv "$temporary_clone" "$SHIPGUARD_DIR"
  trap - RETURN
}

install_browser() {
  if [[ -x "$BROWSER_EXECUTABLE" ]]; then
    return
  fi

  if [[ -e "$BROWSER_DIR" ]]; then
    echo "Erreur : installation Chrome incomplète dans $BROWSER_DIR." >&2
    echo "Supprimez ce dossier manuellement, puis relancez make installer-recette." >&2
    exit 1
  fi

  local temporary_dir
  temporary_dir="$(mktemp -d "$TOOLS_DIR/.chrome.XXXXXX")"

  cleanup_browser() {
    rm -rf -- "$temporary_dir"
  }
  trap cleanup_browser RETURN

  local archive
  archive="$temporary_dir/$BROWSER_ARCHIVE"
  curl --fail --silent --show-error --location "$BROWSER_URL" --output "$archive"

  local actual_sha256
  actual_sha256="$(shasum -a 256 "$archive" | awk '{print $1}')"
  if [[ "$actual_sha256" != "$BROWSER_SHA256" ]]; then
    echo "Erreur : empreinte Chrome inattendue : $actual_sha256." >&2
    echo "Empreinte attendue : $BROWSER_SHA256." >&2
    exit 1
  fi

  mkdir -p "$temporary_dir/extracted"
  ditto -x -k "$archive" "$temporary_dir/extracted"
  if [[ ! -x "$temporary_dir/extracted/$BROWSER_LAYOUT/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing" ]]; then
    echo "Erreur : exécutable Chrome introuvable après extraction." >&2
    exit 1
  fi

  mv "$temporary_dir/extracted" "$BROWSER_DIR"
  trap - RETURN
}

require_command git
require_command node
require_command npm
require_command curl
require_command ditto
require_command shasum

node_major="$(node -p 'process.versions.node.split(".")[0]')"
if (( node_major < 24 )); then
  echo "Erreur : Node.js 24 ou plus est requis pour agent-browser, version détectée : $(node --version)." >&2
  exit 1
fi

install_shipguard
verify_shipguard_assets

npm ci --prefix "$RECETTE_DIR" --ignore-scripts

if [[ ! -x "$AGENT_BROWSER_BIN" ]]; then
  echo "Erreur : agent-browser local est introuvable après npm ci." >&2
  exit 1
fi

agent_browser_version="$("$AGENT_BROWSER_BIN" --version | awk '{print $2}')"
if [[ "$agent_browser_version" != "0.38.1" ]]; then
  echo "Erreur : version locale d'agent-browser inattendue : $agent_browser_version." >&2
  exit 1
fi

install_browser

echo "Recette prête : ShipGuard $SHIPGUARD_REF, agent-browser $agent_browser_version et Chrome $BROWSER_VERSION."
