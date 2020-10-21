#!/bin/bash -e

source /root/.tf/stack.env
cd "/home/centos/tf-deployment-test/"
if [[ ! -f "/home/centos/tf-deployment-test/.testrepository" ]]; then
    testr init
fi

testr run
    