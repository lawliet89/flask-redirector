# Flask Redirector [![Build Status](https://api.travis-ci.org/lawliet89/flask-redirector.svg?branch=master)](https://travis-ci.org/lawliet89/flask-redirector)
A simple Flask application to redirect URLs to another domain.

## Configuration
An example configuration file:
```ini
REDIRECTOR_SCHEME = 'https'
REDIRECTOR_HOST = 'www.example.com'
REDIRECTOR_BASE_PATH = '/'
REDIRECTOR_PORT = 443
REDIRECTOR_REDIRECT_CODE = 301
```

Then, start the server with `./manager.py -c file.ini runserver`

## Running the server
```
$ ./manager.py --help
usage: manager.py [--port PORT] [--scheme {http,https}] [--host HOST]
                  [--redirect-code REDIRECT_CODE] [-c CONFIG_FILE]
                  [--base-path BASE_PATH] [-?]
                  {gunicorn,shell,runserver} ...

positional arguments:
  {gunicorn,shell,runserver}
    gunicorn            Run the app within Gunicorn
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  --port PORT           The port number to redirect to
  --scheme {http,https}
                        The scheme to redirect users to
  --host HOST           The HTTP Host to redirect users to
  --redirect-code REDIRECT_CODE
                        The HTTP status code for use in redirecting
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        Provide a path to an ini file for configuration
  --base-path BASE_PATH
                        The base path to redirect to. Must end in "/"
  -?, --help            show this help message and exit

```

### gunicorn
When used in production, you should use the `gunicorn` mode to run. See
[gunicorn](http://docs.gunicorn.org/en/stable/configure.html) for more information on the options.

```
$ ./manager.py gunicorn --help
usage: manager.py gunicorn [-?] [--threads INT] [--graceful-timeout INT]
                           [--keep-alive INT] [--preload] [--spew]
                           [--access-logfile FILE] [--keyfile FILE]
                           [-b ADDRESS] [-w INT] [--paste STRING] [-k STRING]
                           [--chdir CHDIR] [--statsd-host STATSD_ADDR]
                           [--ssl-version SSL_VERSION]
                           [--log-syslog-to SYSLOG_ADDR] [-t INT]
                           [--suppress-ragged-eofs] [--worker-tmp-dir DIR]
                           [--no-sendfile] [-p FILE]
                           [--access-logformat STRING] [-n STRING]
                           [--max-requests INT]
                           [--limit-request-field_size INT] [--check-config]
                           [-e ENV] [--log-config FILE]
                           [--forwarded-allow-ips STRING] [--capture-output]
                           [--pythonpath STRING] [--worker-connections INT]
                           [--log-syslog] [--log-level LEVEL] [-c CONFIG]
                           [--limit-request-line INT]
                           [--proxy-allow-from PROXY_ALLOW_IPS]
                           [--proxy-protocol] [--ca-certs FILE] [-R]
                           [--cert-reqs CERT_REQS] [--reload]
                           [--error-logfile FILE] [-m INT]
                           [--statsd-prefix STATSD_PREFIX]
                           [--max-requests-jitter INT] [--settings STRING]
                           [--log-syslog-prefix SYSLOG_PREFIX]
                           [--certfile FILE] [--do-handshake-on-connect]
                           [--logger-class STRING] [--ciphers CIPHERS]
                           [--limit-request-fields INT]
                           [--log-syslog-facility SYSLOG_FACILITY]
                           [--backlog INT] [-g GROUP] [-D] [-u USER]

Run the app within Gunicorn

optional arguments:
  -?, --help            show this help message and exit
  --threads INT         The number of worker threads for handling requests.
                        Run each worker with the specified number of threads.
                        A positive integer generally in the ``2-4 x
                        $(NUM_CORES)`` range. You'll want to vary this a bit
                        to find the best for your particular application's
                        work load. If it is not defined, the default is 1.
  --graceful-timeout INT
                        Timeout for graceful workers restart. After receiving
                        a restart signal, workers have this much time to
                        finish serving requests. Workers still alive after the
                        timeout (starting from the receipt of the restart
                        signal) are force killed.
  --keep-alive INT      The number of seconds to wait for requests on a Keep-
                        Alive connection. Generally set in the 1-5 seconds
                        range.
  --preload             Load application code before the worker processes are
                        forked. By preloading an application you can save some
                        RAM resources as well as speed up server boot times.
                        Although, if you defer application loading to each
                        worker process, you can reload your application code
                        easily by restarting workers.
  --spew                Install a trace function that spews every line
                        executed by the server. This is the nuclear option.
  --access-logfile FILE
                        The Access log file to write to. ``'-'`` means log to
                        stderr.
  --keyfile FILE        SSL key file
  -b ADDRESS, --bind ADDRESS
                        The socket to bind. A string of the form: ``HOST``,
                        ``HOST:PORT``, ``unix:PATH``. An IP is a valid
                        ``HOST``. Multiple addresses can be bound. ex.:: $
                        gunicorn -b 127.0.0.1:8000 -b [::1]:8000 test:app will
                        bind the `test:app` application on localhost both on
                        ipv6 and ipv4 interfaces.
  -w INT, --workers INT
                        The number of worker processes for handling requests.
                        A positive integer generally in the ``2-4 x
                        $(NUM_CORES)`` range. You'll want to vary this a bit
                        to find the best for your particular application's
                        work load. By default, the value of the
                        ``WEB_CONCURRENCY`` environment variable. If it is not
                        defined, the default is ``1``.
  --paste STRING, --paster STRING
                        Load a PasteDeploy config file. The argument may
                        contain a ``#`` symbol followed by the name of an app
                        section from the config file, e.g.
                        ``production.ini#admin``. At this time, using
                        alternate server blocks is not supported. Use the
                        command line arguments to control server configuration
                        instead.
  -k STRING, --worker-class STRING
                        The type of workers to use. The default class
                        (``sync``) should handle most "normal" types of
                        workloads. You'll want to read :doc:`design` for
                        information on when you might want to choose one of
                        the other worker classes. A string referring to one of
                        the following bundled classes: * ``sync`` *
                        ``eventlet`` - Requires eventlet >= 0.9.7 * ``gevent``
                        - Requires gevent >= 0.13 * ``tornado`` - Requires
                        tornado >= 0.2 * ``gthread`` - Python 2 requires the
                        futures package to be installed * ``gaiohttp`` -
                        Requires Python 3.4 and aiohttp >= 0.21.5 Optionally,
                        you can provide your own worker by giving Gunicorn a
                        Python path to a subclass of
                        ``gunicorn.workers.base.Worker``. This alternative
                        syntax will load the gevent class:
                        ``gunicorn.workers.ggevent.GeventWorker``.
                        Alternatively, the syntax can also load the gevent
                        class with ``egg:gunicorn#gevent``.
  --chdir CHDIR         Chdir to specified directory before apps loading.
  --statsd-host STATSD_ADDR
                        ``host:port`` of the statsd server to log to. ..
                        versionadded:: 19.1
  --ssl-version SSL_VERSION
                        SSL version to use (see stdlib ssl module's)
  --log-syslog-to SYSLOG_ADDR
                        Address to send syslog messages. Address is a string
                        of the form: * ``unix://PATH#TYPE`` : for unix domain
                        socket. ``TYPE`` can be ``stream`` for the stream
                        driver or ``dgram`` for the dgram driver. ``stream``
                        is the default. * ``udp://HOST:PORT`` : for UDP
                        sockets * ``tcp://HOST:PORT`` : for TCP sockets
  -t INT, --timeout INT
                        Workers silent for more than this many seconds are
                        killed and restarted. Generally set to thirty seconds.
                        Only set this noticeably higher if you're sure of the
                        repercussions for sync workers. For the non sync
                        workers it just means that the worker process is still
                        communicating and is not tied to the length of time
                        required to handle a single request.
  --suppress-ragged-eofs
                        Suppress ragged EOFs (see stdlib ssl module's)
  --worker-tmp-dir DIR  A directory to use for the worker heartbeat temporary
                        file. If not set, the default temporary directory will
                        be used.
  --no-sendfile         Disables the use of ``sendfile()``. If not set, the
                        value of the ``SENDFILE`` environment variable is used
                        to enable or disable its usage. .. versionadded:: 19.2
                        .. versionchanged:: 19.4 Swapped ``--sendfile`` with
                        ``--no-sendfile`` to actually allow disabling. ..
                        versionchanged:: 19.6 added support for the
                        ``SENDFILE`` environment variable
  -p FILE, --pid FILE   A filename to use for the PID file. If not set, no PID
                        file will be written.
  --access-logformat STRING
                        The access log format. ========== ===========
                        Identifier Description ========== =========== h remote
                        address l ``'-'`` u user name t date of the request r
                        status line (e.g. ``GET / HTTP/1.1``) m request method
                        U URL path without query string q query string H
                        protocol s status B response length b response length
                        or ``'-'`` (CLF format) f referer a user agent T
                        request time in seconds D request time in microseconds
                        L request time in decimal seconds p process ID
                        {Header}i request header {Header}o response header
                        ========== ===========
  -n STRING, --name STRING
                        A base to use with setproctitle for process naming.
                        This affects things like ``ps`` and ``top``. If you're
                        going to be running more than one instance of Gunicorn
                        you'll probably want to set a name to tell them apart.
                        This requires that you install the setproctitle
                        module. If not set, the *default_proc_name* setting
                        will be used.
  --max-requests INT    The maximum number of requests a worker will process
                        before restarting. Any value greater than zero will
                        limit the number of requests a work will process
                        before automatically restarting. This is a simple
                        method to help limit the damage of memory leaks. If
                        this is set to zero (the default) then the automatic
                        worker restarts are disabled.
  --limit-request-field_size INT
                        Limit the allowed size of an HTTP request header
                        field. Value is a number from 0 (unlimited) to 8190.
                        to set the limit on the allowed size of an HTTP
                        request header field.
  --check-config        Check the configuration.
  -e ENV, --env ENV     Set environment variable (key=value). Pass variables
                        to the execution environment. Ex.:: $ gunicorn -b
                        127.0.0.1:8000 --env FOO=1 test:app and test for the
                        foo variable environment in your application.
  --log-config FILE     The log config file to use. Gunicorn uses the standard
                        Python logging module's Configuration file format.
  --forwarded-allow-ips STRING
                        Front-end's IPs from which allowed to handle set
                        secure headers. (comma separate). Set to ``*`` to
                        disable checking of Front-end IPs (useful for setups
                        where you don't know in advance the IP address of
                        Front-end, but you still trust the environment). By
                        default, the value of the ``FORWARDED_ALLOW_IPS``
                        environment variable. If it is not defined, the
                        default is ``"127.0.0.1"``.
  --capture-output      Redirect stdout/stderr to Error log. .. versionadded::
                        19.6
  --pythonpath STRING   A comma-separated list of directories to add to the
                        Python path. e.g. ``'/home/djangoprojects/myproject,/h
                        ome/python/mylibrary'``.
  --worker-connections INT
                        The maximum number of simultaneous clients. This
                        setting only affects the Eventlet and Gevent worker
                        types.
  --log-syslog          Send *Gunicorn* logs to syslog.
  --log-level LEVEL     The granularity of Error log outputs. Valid level
                        names are: * debug * info * warning * error * critical
  -c CONFIG, --config CONFIG
                        The Gunicorn config file. A string of the form
                        ``PATH``, ``file:PATH``, or ``python:MODULE_NAME``.
                        Only has an effect when specified on the command line
                        or as part of an application specific configuration.
                        .. versionchanged:: 19.4 Loading the config from a
                        Python module requires the ``python:`` prefix.
  --limit-request-line INT
                        The maximum size of HTTP request line in bytes. This
                        parameter is used to limit the allowed size of a
                        client's HTTP request-line. Since the request-line
                        consists of the HTTP method, URI, and protocol
                        version, this directive places a restriction on the
                        length of a request-URI allowed for a request on the
                        server. A server needs this value to be large enough
                        to hold any of its resource names, including any
                        information that might be passed in the query part of
                        a GET request. Value is a number from 0 (unlimited) to
                        8190. This parameter can be used to prevent any DDOS
                        attack.
  --proxy-allow-from PROXY_ALLOW_IPS
                        Front-end's IPs from which allowed accept proxy
                        requests (comma separate). Set to ``*`` to disable
                        checking of Front-end IPs (useful for setups where you
                        don't know in advance the IP address of Front-end, but
                        you still trust the environment)
  --proxy-protocol      Enable detect PROXY protocol (PROXY mode). Allow using
                        HTTP and Proxy together. It may be useful for work
                        with stunnel as HTTPS frontend and Gunicorn as HTTP
                        server. PROXY protocol:
                        http://haproxy.1wt.eu/download/1.5/doc/proxy-
                        protocol.txt Example for stunnel config:: [https]
                        protocol = proxy accept = 443 connect = 80 cert =
                        /etc/ssl/certs/stunnel.pem key =
                        /etc/ssl/certs/stunnel.key
  --ca-certs FILE       CA certificates file
  -R, --enable-stdio-inheritance
                        Enable stdio inheritance. Enable inheritance for stdio
                        file descriptors in daemon mode. Note: To disable the
                        Python stdout buffering, you can to set the user
                        environment variable ``PYTHONUNBUFFERED`` .
  --cert-reqs CERT_REQS
                        Whether client certificate is required (see stdlib ssl
                        module's)
  --reload              Restart workers when code changes. This setting is
                        intended for development. It will cause workers to be
                        restarted whenever application code changes. The
                        reloader is incompatible with application preloading.
                        When using a paste configuration be sure that the
                        server block does not import any application code or
                        the reload will not work as designed.
  --error-logfile FILE, --log-file FILE
                        The Error log file to write to. Using ``'-'`` for FILE
                        makes gunicorn log to stderr. .. versionchanged:: 19.2
                        Log to stderr by default.
  -m INT, --umask INT   A bit mask for the file mode on files written by
                        Gunicorn. Note that this affects unix socket
                        permissions. A valid value for the ``os.umask(mode)``
                        call or a string compatible with ``int(value, 0)``
                        (``0`` means Python guesses the base, so values like
                        ``0``, ``0xFF``, ``0022`` are valid for decimal, hex,
                        and octal representations)
  --statsd-prefix STATSD_PREFIX
                        Prefix to use when emitting statsd metrics (a trailing
                        ``.`` is added, if not provided). .. versionadded::
                        19.2
  --max-requests-jitter INT
                        The maximum jitter to add to the *max_requests*
                        setting. The jitter causes the restart per worker to
                        be randomized by ``randint(0, max_requests_jitter)``.
                        This is intended to stagger worker restarts to avoid
                        all workers restarting at the same time. ..
                        versionadded:: 19.2
  --settings STRING     The Python path to a Django settings module.
                        (deprecated) e.g. ``myproject.settings.main``. If this
                        isn't provided, the ``DJANGO_SETTINGS_MODULE``
                        environment variable will be used. **DEPRECATED**: use
                        the ``--env`` argument instead.
  --log-syslog-prefix SYSLOG_PREFIX
                        Makes Gunicorn use the parameter as program-name in
                        the syslog entries. All entries will be prefixed by
                        ``gunicorn.<prefix>``. By default the program name is
                        the name of the process.
  --certfile FILE       SSL certificate file
  --do-handshake-on-connect
                        Whether to perform SSL handshake on socket connect
                        (see stdlib ssl module's)
  --logger-class STRING
                        The logger you want to use to log events in Gunicorn.
                        The default class (``gunicorn.glogging.Logger``)
                        handle most of normal usages in logging. It provides
                        error and access logging. You can provide your own
                        worker by giving Gunicorn a Python path to a subclass
                        like ``gunicorn.glogging.Logger``. Alternatively the
                        syntax can also load the Logger class with
                        ``egg:gunicorn#simple``.
  --ciphers CIPHERS     Ciphers to use (see stdlib ssl module's)
  --limit-request-fields INT
                        Limit the number of HTTP headers fields in a request.
                        This parameter is used to limit the number of headers
                        in a request to prevent DDOS attack. Used with the
                        *limit_request_field_size* it allows more safety. By
                        default this value is 100 and can't be larger than
                        32768.
  --log-syslog-facility SYSLOG_FACILITY
                        Syslog facility name
  --backlog INT         The maximum number of pending connections. This refers
                        to the number of clients that can be waiting to be
                        served. Exceeding this number results in the client
                        getting an error when attempting to connect. It should
                        only affect servers under significant load. Must be a
                        positive integer. Generally set in the 64-2048 range.
  -g GROUP, --group GROUP
                        Switch worker process to run as this group. A valid
                        group id (as an integer) or the name of a user that
                        can be retrieved with a call to
                        ``pwd.getgrnam(value)`` or ``None`` to not change the
                        worker processes group.
  -D, --daemon          Daemonize the Gunicorn process. Detaches the server
                        from the controlling terminal and enters the
                        background.
  -u USER, --user USER  Switch worker processes to run as this user. A valid
                        user id (as an integer) or the name of a user that can
                        be retrieved with a call to ``pwd.getpwnam(value)`` or
                        ``None`` to not change the worker process user.
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
