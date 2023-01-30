#!/bin/bash

echo "Hello sir, what is your name?"
read name

echo "Hello $name, what do you want to do next?"

read input_action
if [[ $input_action == "q" ]]; then
	echo "Bye bye $name!!!"
	exit 1
else
	echo "So you want to $input_action next? (y/n)"
fi


