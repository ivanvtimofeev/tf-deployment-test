#!/bin/bash -eu

my_file="$(readlink -e "$0")"
my_dir="$(dirname "$my_file")"

cd
source rhosp-environment.sh
source $my_dir/functions.sh


checkForVariable SSH_USER
checkForVariable RHEL_USER
checkForVariable RHEL_PASSWORD
checkForVariable RHEL_POOL_ID
checkForVariable mgmt_ip
checkForVariable ssh_private_key
checkForVariable undercloud_public_host
checkForVariable undercloud_admin_host

cd
echo "Copiyng ffu/* to undercloud node"
scp -r ./ffu ./rhosp-environment.sh $SSH_USER@$mgmt_ip:

echo "Preparing for undercloud RHEL upgrade"
run_ssh_undercloud './ffu/01_undercloud_prepare.sh'
reboot_and_wait_undercloud

run_ssh_undercloud './ffu/02_undercloud_upgrade_rhel_step1.sh'
reboot_and_wait_undercloud

run_ssh_undercloud './ffu/03_undercloud_upgrade_rhel_step2.sh'
reboot_and_wait_undercloud

run_ssh_undercloud './ffu/04_undercloud_upgrade_tripleo.sh'
run_ssh_undercloud './ffu/05_contrail_images_prepare.sh'

######################################################
#                  OVERCLOUD                         #
######################################################
run_ssh_undercloud './ffu/06_overcloud_prepare.sh'
run_ssh_undercloud './ffu/07_overcloud_prepare_templates.sh'
run_ssh_undercloud './ffu/08_overcloud_upgrade_prepare.sh'
run_ssh_undercloud './ffu/09_overcloud_upgrade_os.sh'
run_ssh_undercloud './ffu/10_overcloud_upgrade_contrail_ctrl.sh'
run_ssh_undercloud './ffu/11_overcloud_upgrade_compute.sh'
run_ssh_undercloud './ffu/12_overcloud_upgrade_converge.sh'
run_ssh_undercloud './ffu/13_collect_information.sh'

