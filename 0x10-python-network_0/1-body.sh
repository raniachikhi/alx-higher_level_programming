#!/bin/bash
# takes in a URL, sends a request to it, and displays the size of the body of the response
curl -sX GET $1 -L
