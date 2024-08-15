from subprocess import call

def github_update_staging():
    call("./scripts/staging_update.sh", shell=True)

def github_update_server():
    call("./scripts/server_update.sh", shell=True)
