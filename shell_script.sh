	cat get.out | tr ' ' '\n' | grep -e '20[0-9][0-9]-[0-9][0-9]-' | tac | awk '{print $0,NR}' >! dates-chron.txt
