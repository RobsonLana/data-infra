#!/bin/bash

while true; do
    response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8083/)
    if [ "$response" == "200" ]; then
        break
    fi
    sleep 5
done

curl -X POST -H "Content-Type: application/json" -d @./connectors/cassandra-source.json http://localhost:8083/connectors

