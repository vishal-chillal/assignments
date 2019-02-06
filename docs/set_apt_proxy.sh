#!/bin/bash


[ `id -u` != 0 ] && { echo "Run this script with admin privileges." ; exit -1 ; }

echo "Setting up apt proxy..."
echo "Acquire::http::Proxy \"http://aptcacher.lan.coriolis.co.in:3142\";" > \
	"/etc/apt/apt.conf.d/01proxy"

apt-get update
