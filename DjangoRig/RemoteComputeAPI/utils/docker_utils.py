import docker


def run_alpine():
    client = docker.from_env()
    client.containers.run('alpine', 'echo hello world')


if __name__ == '__main__':
    run_alpine()
