#!/bin/bash

echo "Running Count O Tests"
cd ..
docker build -t myproj-unittests .
docker run --rm myproj-unittests