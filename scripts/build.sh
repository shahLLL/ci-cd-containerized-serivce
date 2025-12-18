#!/bin/bash

echo "Running Count O Tests"
cd ..
docker build -t count-o .
docker run --rm count-o