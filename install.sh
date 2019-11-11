#!/bin/bash
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
sudo pip install docker-compose