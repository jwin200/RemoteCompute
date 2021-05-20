#!/usr/bin/env bash
# setup.sh

apt-get update && apt-get upgrade
apt-get -y install curl
curl -sSL https://get.docker.com/ | sh
docker --version