from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"
API_DIR = APP_DIR / "api"
SERVICES_DIR = APP_DIR / "services"

APP_DIR.mkdir(parents=True, exist_ok=True)
API_DIR.mkdir(parents=True, exist_ok=True)
SERVICES_DIR.mkdir(parents=True, exist_ok=True)

for directory in [APP_DIR, API_DIR, SERVICES_DIR]:
    init_file = directory / "__init__.py"
    if not init_file.exists():
        init_file.write_text("", encoding="utf-8")

print("Backend package structure created")
