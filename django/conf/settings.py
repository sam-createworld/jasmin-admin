import os

# Jasmin Settings
"""Jasmin telnet defaults"""
TELNET_HOST = os.environ.get('TELNET_HOST', default='127.0.0.1')
TELNET_PORT = os.environ.get('TELNET_PORT', default=8990)
TELNET_USERNAME = os.environ.get('TELNET_USERNAME', default='jcliadmin')
TELNET_PW = os.environ.get('TELNET_PW', default='jclipwd')  # no alternative storing as plain text
TELNET_TIMEOUT = os.environ.get('TELNET_TIMEOUT', default=10)  # reasonable value for intranet.


POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default='127.0.0.1')
POSTGRES_DB = os.environ.get('POSTGRES_DB', default='test_db')
POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME', default='root')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default='root')
# POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default='cwt-prod-db-pg11.postgres.database.azure.com')
# POSTGRES_DB = os.environ.get('POSTGRES_DB', default='test_db')
# POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME', default='cwtuser@cwt-prod-db-pg11')
# POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default='cwtpwd')

STANDARD_PROMPT = 'jcli : '  # There should be no need to change this
INTERACTIVE_PROMPT = '> '  # Prompt for interactive commands
# SUBMIT_LOG = os.environ.get.bool('SUBMIT_LOG', False)  # This is used for DLR Report

