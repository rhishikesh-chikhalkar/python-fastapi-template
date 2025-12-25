#!/bin/bash
exec /opt/apps/python-fastapi-template/.venv/bin/uvicorn src.app.main:app --host 127.0.0.1 --port 8001
