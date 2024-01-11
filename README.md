# First Time Setup

## Create a virtual environment with Pipenv

### Install dependencies

```
pipenv install
```

### Create a virtual environment

```
pipenv shell
```

## Initialize the database

Make sure you run this command inside the pipenv shell

```
flask --app app.web init-db
```

# Running the app

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

```
flask --app app.web init-db
```
