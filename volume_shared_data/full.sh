#!/bin/bash
./kill_containers.sh
./create_volume.sh
./build.sh
./run.sh
./after.sh
