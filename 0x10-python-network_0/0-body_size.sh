#!/bin/bash
# This script takes in a URL, sends an HTTP request to that URL,
#and displays the size of the response body.
body=$(curl -sL $1)
size_in_bytes=$(echo -n "$body" | wc -c)
echo "$size_in_bytes"
