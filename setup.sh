#!/usr/bin/env bash

# Update
sudo apt-get update

# Packages
sudo apt-get install -y git \
                        python-dev \
                        python-pip \

# Setup virtual environment
sudo pip install virtualenvwrapper

echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc

mkvirtualenv working-title

echo 'cd /srv/project' >> ~/.bashrc
echo 'workon working-title' >> ~/.bashrc

# Sync Github
(cd /srv/project ;
 git config --global push.default simple
 pip install -r requirements.txt
)
