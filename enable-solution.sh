#!/bin/bash

export SHARE_DIR=${SHARE_DIR:-~/opt}

PID_FILE=$SHARE_DIR/pid.elastic

if [ -r $PID_FILE ]; then
    kill `cat $PID_FILE`
fi

$SHARE_DIR/elasticsearch/bin/elasticsearch -d -p $PID_FILE -E path.data=$SHARE_DIR/elastic-data/elastic-data/ #-E index.number_of_replicas=0
