#!/bin/bash

name=$1

my_path=$(pwd)
today=$(date)

echo "Hello $name, you are now in the directory of $my_path, have a nice day!"

sleep 2

echo "Hey $name, do you want to show the date? (y/n)"
read answer

if [[ $answer == "y" ]]; then
	echo "Okay, today is $today, I love you with all my heart!!!"
else
	echo "Bye $name!!!"
fi
