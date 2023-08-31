#!/bin/bash
# script to send custom headers to servers

url="$1"
header="X-School-User-Id: 98"

response=$(curl -H "$header" "$url" 2>/dev/null)

if [ $? -ne 0 ]; then
    echo "Error: Failed to retrieve response from the server."
else
    echo "$response"
fi
