# To use with Pycharm and Postman

### author: Arjen Keller

## To Start 
- Install requirements.txt with "pip install -r requirements.txt" from env shell
- open flask shell in env with "flask shell" as command
- command: import os
- command: os.environ["ENVIRONMENT"] = 'dev'
- command: from server import db
- command: db.create_all()

## To Run
- complete former steps
- set wsgi.py as entrypoint/executable
- set environment key "ENVIRONMENT" to 'dev','test','prod' 
- run wsgi.py


## To Test
- import postman collection
- start with post command to create some entities


## Speedrun Installation
- import postman collection
- Install requirements.txt with "pip install -r requirements.txt" from env shell
- open flask shell in env with "flask shell" as command
- command: import os
- command: os.environ["ENVIRONMENT"] = 'dev' or 'prod' or 'test'
- set wsgi.py as entrypoint/executable
- set environment key "ENVIRONMENT" to 'dev','test','prod' 
- run wsgi.py
- run postman request deploy-db
