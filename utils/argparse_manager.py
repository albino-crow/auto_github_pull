import argparse
from settings.server import SERVER_PORT


def get_server_port():
    parser = argparse.ArgumentParser(description="Run a server with a specified port.")
    parser.add_argument("-p", "--port", type=int, default=SERVER_PORT)
    args = parser.parse_args()
    return args.port
