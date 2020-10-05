This is simple Flask app 

Getting Started

Prerequisites
  Python 3
  pip3 and pipenv to install dependencies and create virtualenv
  PostgreSQL


Setting up the local DB
  Run python3 manage.py db init
      python3 manage.py db migrate
      python3 manage.py db upgrade

Running the app
  Run virtualenv env to create the virtual environment than activate it by source env/bin/activate
  Run pip3 install -r requirements.txt
  cd into the app directory and run python3 main.py
