#!/bin/bash

docker-compose up -d &

while true; do
    kafka_response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8083/)
    schema_response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8081/)
    if [ "$kafka_response" == "200" ] && [ "$schema_response" == "200" ]; then
        break
    fi
    sleep 5
done

curl -X POST -H "Content-Type: application/json" -d @./connectors/cassandra-source.json http://localhost:8083/connectors
