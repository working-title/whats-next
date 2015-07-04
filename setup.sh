#!/usr/bin/env bash

# Update
echo "Updating Apt"
 sudo apt-get update -qq

echo "Upgrading Packages..."
sudo apt-get upgrade -qq

# Packages
echo "Installing the packages we need :)"
sudo apt-get install -y -qq git \
						python-dev \
						python-pip \

# Setup virtual environment
sudo pip install virtualenvwrapper

echo 'Configuring Python Virtual Environment'

echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv working-title

echo 'cd /srv/project' >> ~/.bashrc
echo 'workon working-title' >> ~/.bashrc


# Sync Github
echo 'Cloning our awesome code repo!'
(cd /srv/project ;
 git config --global push.default simple
 pip install -r requirements.txt
)

echo 'Done :) - Hopefully!'
