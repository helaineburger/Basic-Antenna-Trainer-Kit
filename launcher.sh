#!/bin/bash

commands () {
	cd /home/user/Documents/Research/Final/Basic-Antenna-Trainer-Kit-main
	python hyflex.pyw
	$SHELL
}

export -f commands

lxterminal -e "bash -c 'commands'"
