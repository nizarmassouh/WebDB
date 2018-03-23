#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
		echo "started expanding :" $line
		python ./Query Expandion/getexp.py "$line" >> expandedqueries.txt
done < "$1"
