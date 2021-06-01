import docker

CLIENT = docker.from_env()


def run_from_dockerfile(dockerfile_path):
    CLIENT.containers.run()


def run_alpine():
    CLIENT.containers.run('alpine', 'echo hello world')


if __name__ == '__main__':
    run_alpine()
