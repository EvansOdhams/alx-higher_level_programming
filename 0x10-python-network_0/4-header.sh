#!/bin/bash

# Get the URL from the command line argument
url=$1

# Set the header variable X-School-User-Id with the value 98
header="X-School-User-Id: 98"

# Send the GET request to the URL with the header variable
curl -H "$header" "$url"
