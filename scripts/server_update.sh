#!/bin/sh
tmux send-keys -t server 'C-c' Enter
tmux send-keys -t server 'git pull' Enter
tmux send-keys -t server 'alembic upgrade head' Enter
tmux send-keys -t server 'PYTHONPATH=. python app/server.py' Enter
