# cpp
Tools for analyzing the Controller Placement Problem in Software-Defined Networks.

# Environment Specification
```
Python 3.9.1

Package         Version
--------------- ---------
certifi         2020.12.5
chardet         4.0.0
click           7.1.2
cycler          0.10.0
decorator       4.4.2
httplib2        0.19.1
idna            2.10
kiwisolver      1.3.1
Mako            1.1.4
MarkupSafe      1.1.1
matplotlib      3.4.1
networkx        2.5.1
numpy           1.20.2
Pillow          8.2.0
pip             20.3.1
pyparsing       2.4.7
python-dateutil 2.8.1
requests        2.25.1
scipy           1.6.3
setuptools      51.0.0
six             1.16.0
topzootools     0.3.18
urllib3         1.26.3
wheel           0.36.1
```

# NOTE
### 1. choose topos
you can choose target topos to analyze by setting environment variable `TOPO` or `TOPOS`

```generate_all.sh
TOPO=os3e
EXT=pdf
#MAX=5  # add --max $MAX at the end of generate.py to debug only a few topos. 
#MAX='--max 2'
CS='10'
FORCE='-f'
MP='--no-multiprocess'
MP='--processes 4'
OPS='--operation_list metrics'
# Everything except metrics:
#OPS='--operation_list cdfs,ranges,pareto,cloud'
TOPOS='--all_topos'
#TOPOS='--topo Iris'

for C in ${CS}
do
  echo "writing all for num controllers ${C}"
  echo "*********************"
  python3 ./generate.py ${TOPO} --from_start ${C} --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
done
```
### 2. place topo file
if you analyze topology zoo networks you need to place original gml files on `./src/topo` directory.
(if you analyze os3e network you don't need to do)

