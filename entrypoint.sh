#!/bin/bash -e
my_file="$(readlink -e "$0")"
my_dir="$(dirname $my_file)"

set -x
echo "DDDD HOST_KEY = $HOST_KEY"
echo "DDDD HOST_ADDR = $HOST_USER"
echo "DDDD HOST_USER = $HOST_USER"

if [[ -f /root/.tf/stack.env ]] ; then
    source=/root/.tf/stack.env
fi

export WORKSPACE=$my_dir
source /env/bin/activate
cd $WORKSPACE
if [[ ! -f "$WORKSPACE/.testrepository" ]]; then
    testr init
fi

testr run
    