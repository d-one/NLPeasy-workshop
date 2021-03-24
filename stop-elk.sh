#!/bin/bash

if [ $BINDER_PORT ]; then
    pkill node; pkill java;
    echo Stoped elastic and kibana
else
    echo Not running on binder.
fi
