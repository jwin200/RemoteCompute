from os import path
from docker.errors import ImageNotFound
from .docker_utils import CLIENT
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MEDIA_DIR = path.join(BASE_DIR, 'media/uploads/')


def make_dockerfile(base_image, dir_name, file_name):
    try:
        # Ensure the base image exists
        CLIENT.images.get(base_image)
    except ImageNotFound:
        print('Could not find Docker base image, skipping...')
        return

    # Ensure the folder exists
    dir_path = path.join(MEDIA_DIR, dir_name)
    if not path.isdir(dir_path):
        print('Could not find folder!')
        return

    # Ensure the file exists
    file_path = path.join(dir_path, file_name)
    if not path.isfile(file_path):
        print('Could not find file!')

    # Ensure there is a requirements file
    req_path = path.join(dir_path, 'requirements.txt')
    if not path.isfile(req_path):
        with open(f'{req_path}', 'w') as file:
            pass

    outline = f'''
        # syntax = docker/dockerfile:experimental
        FROM {base_image}
        MAINTAINER "Jonah Winchell" "jonahwinchell@gmail.com"
        
        RUN mkdir -p /opt/app && \\
            mkdir -p /opt/app/pip_cache
        WORKDIR /opt/app
        COPY . /opt/app/
        RUN python3 -m pip install --upgrade pip && \\
            python3 -m pip install -r requirements.txt --cache-dir pip_cache
        STOPSIGNAL SIGTERM
    '''

    # Save Dockerfile to this instance's directory
    with open(f'{dir_path}/Dockerfile', 'w') as file:
        file.write(outline)

    return outline
