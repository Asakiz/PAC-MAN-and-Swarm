#!/bin/bash

python gridworld.py -a value -i 5
python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
python gridworld.py -a q -k 5 -m
python gridworld.py -a q -k 100
python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid