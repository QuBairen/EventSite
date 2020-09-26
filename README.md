# EventSite
Simple Python REST app


# Development Setup
Simple Python REST app
## Install Python and tools

```shell
sudo apt-get update
sudo apt-get install python3.8
sudo apt-get install python3-pip
sudo apt-get install sqlite3

```
## Install Django and dependent modules

```shell
python3 -m pip install -r requirements.txt
```

## Install Debug SMTP Server

```shell
python3 -m pip install smtp 
```

## Run Application Locally

```shell
# Start SMTP debug server
python3 -m smtpd -n -c DebuggingServer localhost:1025

# Start application
python3 manage.py runserver

```


## Optional TODOS
* Python Isolation via Conda or venv
