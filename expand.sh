#!/bin/bash
while IFS='' read -r line || [ -n "$line" ]; do
	echo "started expanding :" $line
	python ./Query\ Expansion/getexp.py "$line" >> expanded_queries.txt
done < "$1"
