#!/usr/bin/bash
# set -x
PYTHON=/usr/bin/python3
HOME=/home/k5aq
ADI_PATH=$HOME/Documents/WSJT-X
ADI=$ADI_PATH/wsjtx_log.adi
COUNTER=$HOME/Documents/Ham_Radio/adif_counter/adif_counter.py

$PYTHON $COUNTER $ADI