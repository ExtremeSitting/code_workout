#! /bin/bash
for i in {1..100}; do echo $i "ID:"$(uuidgen) "power: "$(shuf -i 1-100 -n 1) "access: "$(date -uRd @$(shuf -i 0-$(date +'%s') -n 1)); done | column -t
