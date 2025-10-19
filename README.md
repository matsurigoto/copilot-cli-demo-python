# copilot-cli-demo-python

Flask API demo for teaching GitHub Copilot CLI.

## Endpoints
- `GET /health` -> { "status": "ok" }
- `GET /users` -> sample list

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
# open http://localhost:3002/health