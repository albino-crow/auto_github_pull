#!/bin/sh
tmux send-keys -t staging-server 'C-c' Enter
tmux send-keys -t staging-server 'git pull' Enter
tmux send-keys -t staging-server 'alembic upgrade head' Enter
tmux send-keys -t staging-server 'python3 -m app.scripts.delete_checks' Enter
tmux send-keys -t staging-server 'python3 -m app.scripts.create_checks' Enter
tmux send-keys -t staging-server 'PYTHONPATH=. python app/server.py --port 3002' Enter
