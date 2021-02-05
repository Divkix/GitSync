#!/bin/bash

echo "Setting up..."

sudo apt update
sudo apt install git-core -y
git config --global user.name "Divkix"
git config --global user.email "techdroidroot@gmail.com"
sudo pip install --upgrade pygithub python-gitlab