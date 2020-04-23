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

import csv

CONFIGDIR = '.koku'
CREDENTIALSFILE = 'config'
OUTPUTDIR = Path("output")


OUTPUTDIR.mkdir(exist_ok=True)

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


#
# Environment variables take precedence to config file
#
username = os.environ.get(ENV_USERNAME, username)
password = os.environ.get(ENV_PASSWORD, password)

# Check if there are actually auth headers properly done.
if(len(username) == 0 or len(password) == 0):
    print("ERROR: No configuration for username or password ")
    usage()


# Configure open_api client to access cost management
configuration = openapi_client.Configuration()
configuration.username = username
configuration.password = password

# Let's get a list of sources and pretty print them in a csv file
with openapi_client.ApiClient(configuration) as api_client:
    # Output file TODO: change the name with a variable
    outputfile = OUTPUTDIR / 'sources'
    with open(outputfile, 'w', newline='') as csvoutput:
        # Create an instance of the API class
        csvwriter = csv.writer(csvoutput)
        api_instance = openapi_client.SourcesApi(api_client)
        try:
            # Read the list of models
            api_response = api_instance.list_sources()
            elements = ['id', 'name', 'source_type', 'uuid', 'provider_linked']
            csvwriter.writerow(elements)
            for x in api_response.data:
                csvwriter.writerow([x.to_dict()[element] for element in elements])
        except ApiException as e:
            print("Exception when calling SourcesApi->list_sources: %s\n" % e)


with openapi_client.ApiClient(configuration) as api_client:
    outputfile = OUTPUTDIR / 'cost_models'
    # Create an instance of the API class
    with open(outputfile, 'w', newline='') as csvoutput:
        # Create an instance of the API class
        csvwriter = csv.writer(csvoutput)
        api_instance = openapi_client.CostModelsApi(api_client)
        try:
            # The list of the cost models.
            api_response = api_instance.list_cost_models()
            elements = ['id']
            csvwriter.writerow(elements)
            for x in api_response.data:
                pprint(x)
        except ApiException as e:
            print("Exception when calling CostModelsApi->list_cost_models: %s\n" % e)



with openapi_client.ApiClient(configuration) as api_client:
    outputfile = OUTPUTDIR / 'number_of_provisions'
    api_instance = openapi_client.MetricsApi()

# Number of provisions. AWS CloudFormation stack name
# Monthly cost
# KPI -> Avg cost per provision
# Student --> Cost for OpenShift
# By GEO