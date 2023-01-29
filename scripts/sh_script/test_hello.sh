#!/bin/sh
echo "Hello Sir, what is your name"
read user_name
echo "Hello $user_name!"
echo "Finding the csv data source for you under this repo data dir..."
ls ../../data | grep csv
echo "Bye bye $user_name! I really hope you have a very good day."
