# working-title

## GovHack 2015 

Helping people with post-school life choices.

## Installation
1. Download and install Vagrant from [here](http://www.vagrantup.com/downloads).
2. Download and install VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads).
3. Clone the repository (which is [here](https://github.com/working-title/working-title), but hopefully you know how to do that since you've found our repository!).
4. Change directory to project root.
5. Setup virtual environment by running 'vagrant up'.
6. Install python dependencies by running 'pip install -r requirements.txt'.
7. Migrate the database by running 'm migrate'.
8. Install default data by running 'm loaddata pathways/fixtures/initial_data.json'.
9. Start server with 'drun'.
10. Connect to site with browser at 'localhost:8000'.
