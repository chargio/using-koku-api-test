#! /usr/bin/env bash
unset DOWNLOAD
OUTPUT_FILE=openapi.json
JSON_URL="https://cloud.redhat.com/api/cost-management/v1/openapi.json"

while getopts uf:h option
  do
    case "${option}" in
    u) DOWNLOAD="yes";;
    f) OUTPUT_FILE=${OPTARG};;
    h) echo -e "$0 options: options\nu - (update json from web) \nf - <json_file>\nh - This help";exit 1;;
    esac
done


if [ ! -z "$DOWNLOAD"]; then
  echo "Downloading api json to $OUTPUT_FILE"
  curl $JSON_URL -o $OUTPUT_FILE
fi

# Validate will generate an exeption is it is not right
echo "Validating file $OUTPUT_FILE"
openapi-generator validate -i $OUTPUT_FILE
if [[ $? != 0 ]]; then
  echo "Validation failed for file $OUTPUT_FILE"
  exit 1
fi

echo "Generating API in Python using $OUTPUT_FILE"
openapi-generator generate -i $OUTPUT_FILE -g python

