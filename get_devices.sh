#!/bin/bash             
for i in {10..255}
do
	nmap -sn 10.1.$i.0/24 -oG output.txt && grep -oP '\d+\.\d+\.\d+\.\d+' output.txt > 10.1.$i.txt
done
