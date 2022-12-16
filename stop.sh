#!/bin/bash

docker container stop rabbit-con
docker container stop account-stat-con
docker container stop account-api-con
docker container stop transaction-db-con
docker container stop transaction-api-con
