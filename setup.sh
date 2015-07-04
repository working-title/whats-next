#!/usr/bin/env bash

# Update
echo "Updating"
 sudo apt-get update -qq

# Packages
echo "Installing packages"
sudo apt-get install -y -qq git \
						python-dev \
						python-pip \

# Setup virtual environment
sudo pip install virtualenvwrapper

echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv working-title

echo 'cd /srv/project' >> ~/.bashrc
echo 'workon working-title' >> ~/.bashrc

# Sync Github
(cd /srv/project ;
 git config --global push.default simple
 pip install -r requirements.txt
)
