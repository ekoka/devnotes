#!/bin/bash

USER="michael"
PASSWORD="1234abcd"
HOST="somehost"
PORT=21

lftp -c 
open -u $USER,$PASSWORD $HOST
user $USER $PASSWORD


