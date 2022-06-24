#!/bin/bash
eval "$(conda shell.bash hook)"
conda init bash > /dev/null
conda activate pyconda3
python plot.py