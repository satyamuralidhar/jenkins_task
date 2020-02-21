import yaml
import subprocess
import os
import docker
stream = open('main.yaml', 'r')
data = yaml.load(stream)
docker_images = "docker images | grep task"
subprocess.call(docker_images , shell = True)
