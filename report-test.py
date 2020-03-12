#! /usr/bin/env python3
# Test the API for the use cases needed by RH IT.
from __future__ import print_function

import configparser
import os
from pathlib import Path
import openapi_client

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint


CONFIGDIR = '.koku'
CREDENTIALSFILE = 'config'

ENV_USERNAME = "KOKU_USERNAME"
ENV_PASSWORD = "KOKU_PASSWORD"


def usage():
    print('''
Usage:
In order to use cost management API you need to configure username and password in the CREDENTIALS section \
of configuration file or environment variable
''')
    print("Config file: " + str(Path('~', CONFIGDIR, CREDENTIALSFILE)))
    print('''
[CREDENTIALS]
username: <username>
password: <password>
''')

    print("Or use environment variables")
    print("Username\n$ export " + ENV_USERNAME+"=<username>")
    print("Password:\n$ export " + ENV_PASSWORD+"=<password>")
    exit()


# Open a ConfigParser
configfile = configparser.ConfigParser()

# Config File is in ~/$(CONFIGDIR)/$(CREDENTIALS)
# Information is under the default org info

try:
    configfile.read(Path('~', CONFIGDIR, CREDENTIALSFILE).expanduser())
except configparser.MissingSectionHeaderError:
    print("ERROR: Please use a CREDENTIALS header in the config file")
    usage()

# Get username and password from configuration file or environment

if "CREDENTIALS" in configfile.sections():
    username = configfile.get('CREDENTIALS', 'username')
    password = configfile.get('CREDENTIALS', 'password')
else:
    username = password = ""


username = os.environ.get(ENV_USERNAME, username)
password = os.environ.get(ENV_PASSWORD, password)

if(len(username) == 0 or len(password) == 0):
    print("ERROR: No configuration for username or password ")
    usage()

# Configure open_api client to access cost management
configuration = openapi_client.Configuration()
configuration.username = username
configuration.password = password


with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CostModelsApi(api_client)

    try:
        # Create a new cost model.
        api_response = api_instance.list_cost_models()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CostModelsApi->create_cost_model: %s\n" % e)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusApi(api_client)
    
    try:
        # Obtain server status
        api_response = api_instance.get_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_status: %s\n" % e)
