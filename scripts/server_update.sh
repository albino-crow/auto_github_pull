#!/bin/sh
tmux send-keys -t server 'C-c' Enter
tmux send-keys -t staging-server 'sudo systemctl stop lumina_server_main.service' Enter
tmux send-keys -t server 'git pull' Enter
tmux send-keys -t server 'alembic upgrade head' Enter
tmux send-keys -t server 'PYTHONPATH=. python app/server.py' Enter
tmux send-keys -t staging-server 'sudo systemctl restart main_server_staging.service' Enter

