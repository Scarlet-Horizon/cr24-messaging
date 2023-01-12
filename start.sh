#!/bin/bash

cd messaging/ || exit 1
docker-compose up -d

sleep 3

cd ../account-stat/ || exit 2
docker-compose up -d

cd ../account-service/ || exit 3
docker-compose up -d

cd ../transaction/transaction-files/ || exit 4
docker-compose up -d

cd ../transaction-service/ || exit 5
docker-compose up -d
