#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
python3 scripts/validate.py --root .
if command -v dotnet >/dev/null 2>&1; then
  dotnet test tests/GardusiGustavo.Package.Tests/GardusiGustavo.Package.Tests.csproj --nologo --verbosity quiet
else
  echo "dotnet toolchain unavailable; bootstrap validation only"
fi
for f in infra/scripts/*.sh; do bash -n "$f"; done
echo "csharp checks ok"
