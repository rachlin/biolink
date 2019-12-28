#!/bin/bash
# need this script as piping < > doesn't seem to work when called in python subprocess run method
sqlite3 -header -csv $1 < $2 > $3