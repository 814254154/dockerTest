#!/bin/bash
DEFAULT_RPS="20"
DEFAULT_TIME="1m"
DEFAULT_SPAWN="5"

functio

git clone https://github.com/814254154/dockerTest.git 
if [ $? -ne 0 ]; then
    echo "Creating"
else 
    echo "git clone err"
    exit 0
fi

go build -0 main.go cgA && chmod 755 cgA && ./cgA