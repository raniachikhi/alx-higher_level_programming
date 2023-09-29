#!/bin/bash
# This script takes in a URL, sends an HTTP request to that URL,
#and displays the size of the response body.
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
