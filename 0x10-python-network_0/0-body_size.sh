#!/bin/bash
# This script takes in a URL, sends an HTTP request to that URL, and displays the size of the response body.
# It uses the 'curl' command to send the request, retrieves the 'Content-Length' header from the response headers,
# and extracts the size using 'cut'.

# Usage: ./script_name.sh URL
# Example: ./script_name.sh https://example.com
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
