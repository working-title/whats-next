#!/usr/bin/env bash

# Update
sudo apt-get update

# Packages
sudo apt-get install -y git \
                        python-dev \
                        python-pip \


# Sync Github
(cd /srv/project ;
 git clone https://github.com/working-title/working-title.git;
 pip install -r requirement.txt
)
