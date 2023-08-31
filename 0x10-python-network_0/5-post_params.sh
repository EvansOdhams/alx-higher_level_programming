#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "POST params:"
echo -e "\temail: $email"
echo -e "\tsubject: $subject"
echo -e "$response"
