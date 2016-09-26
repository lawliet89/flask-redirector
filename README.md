# Flask Redirector [![Build Status](https://api.travis-ci.org/lawliet89/flask-redirector.svg?branch=master)](https://travis-ci.org/lawliet89/flask-redirector)
A simple Flask application to redirect URLs to another domain.

## Configuration
An example configuration file:
```ini
SCHEME = 'https'
HOST = 'www.example.com'
BASE_PATH = '/'
PORT = 443
REDIRECT_CODE = 301
```

Then, start the server with `./manager.py -c file.ini runserver`

## Running the server
```
$ ./manager.py
usage: manager.py [-c CONFIG_FILE] [--scheme {http,https}] [--host HOST]
                  [--base-path BASE_PATH] [--port PORT]
                  [--redirect-code REDIRECT_CODE] [-?]
                  {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        Provide a path to an ini file for configuration
  --scheme {http,https}
                        The scheme to redirect users to
  --host HOST           The HTTP Host to redirect users to
  --base-path BASE_PATH
                        The base path to redirect users to
  --port PORT           The port to redirect users to
  --redirect-code REDIRECT_CODE
                        The HTTP redirect code for use in redirecting
  -?, --help            show this help message and exit
```

## Issues
Internally, the application uses
[`urllib.parse.urljoin`](https://docs.python.org/3.5/library/urllib.parse.html#urllib.parse.urljoin) to join
URLs. Thus, if your `BASE_PATH` configuration does not end with a '/', you will get incorrect results. See
[this](http://stackoverflow.com/a/10893427/602002) for more information.


## Docker
The Docker image, by default, declars a volume `/usr/src/app/config` and expects a configuration file
`config.ini` inside.

You can run the image using a simple `docker-compose.yml` file

```yml
version: "2.0"
services:
  redirector:
    build: .
    ports:
      - 5000:5000
    volumes:
      - ./config:/usr/src/app/config

```
