#!/usr/bin/env python3
"""FlaskAppBuilder-JWT Test

Usage:
	fab-basicauth-test --help
	fab-basicauth-test [options]

Options:
 -h --help             Show this screen.
 -p --port=<port>      Port used by this test server [default: 8080].
 -d --debug            Start in debug mode.
 -c --config=<config>  LDAP config file, with variables as in https://flask-appbuilder.readthedocs.io/en/latest/security.html#authentication-ldap 

For further documentation see README file.

"""
import os
from docopt import docopt
import logging

from webapp import create_app
from webapp.security import BasicAuthSecurityManager

args = docopt(__doc__)

debug = args['--debug']
logging.getLogger().setLevel(logging.DEBUG if debug else logging.INFO)

from webapp import create_app

config_name = os.path.abspath(args['--config']) if args['--config'] else None
if debug: print("Loading config from: %s"%config_name)
local_app = create_app(config_name=config_name, security_manager_class=BasicAuthSecurityManager)

from webapp import app
app = local_app

app.run(host='0.0.0.0', port=args['--port'], debug=debug)  # pyinstaller one file packaging confuses flask autorestart when debugging

