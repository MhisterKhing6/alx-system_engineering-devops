#!/usr/bin/python3
from fabric.api import *
env.hosts = ['52.72.27.194', '52.201.158.148']
env.user = "ubuntu"

def config():
    sudo('echo "Kb empire" > /var/www/html/index.html')
config()