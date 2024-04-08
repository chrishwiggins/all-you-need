# Makefile

# Define the command for Python interpreter
local_python=/usr/bin/python3

.PHONY: all clean

all: plot

get.out: get.py
	$(local_python) get.py > get.out

dates-chron.txt: get.out shell_script.sh
	sh shell_script.sh

plot: dates-chron.txt plot.py
	$(local_python) plot.py

clean:
	rm -f get.out dates-chron.txt

