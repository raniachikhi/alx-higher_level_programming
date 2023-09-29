#!/bin/bash
# Send an HTTP GET request to the provided URL and store the response headers in a variable
response_headers=$(curl -sI "$1")
content_length=$(echo "$response_headers" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

if [[ "$content_length" =~ ^[0-9]+$ ]]; then
    echo "$content_length"
else
    echo "Unable to determine content length."
fi
