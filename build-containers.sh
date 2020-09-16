#!/bin/bash

CONTAINER_REGISTRY=${CONTAINER_REGISTRY:-"localhost:5000"}
CONTRAIL_CONTAINER_TAG=${CONTRAIL_CONTAINER_TAG:-"dev"}

scriptdir=$(realpath $(dirname "$0"))

build_opts="--build-arg LC_ALL=en_US.UTF-8 --build-arg LANG=en_US.UTF-8 --build-arg LANGUAGE=en_US.UTF-8"
build_opts+=" --network host --no-cache --tag ${CONTAINER_REGISTRY}/tf-deployment-test:${CONTRAIL_CONTAINER_TAG} $scriptdir"

sudo docker build $build_opts