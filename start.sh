#!/bin/bash

cd messaging/ || exit 1
docker container stop rabbit-con
docker-compose up -d

cd ../account-service/ || exit 2
docker container stop account-api-con
docker-compose up -d

cd ../account-stat/ || exit 3
docker container stop account-stat-con
docker-compose up -d

cd ../transaction/transaction-files/ || exit 4
docker container stop transaction-db-con
docker-compose up -d

cd ../transaction-service/ || exit 5
docker container stop transaction-api-con
docker-compose up -d

cd ../../
