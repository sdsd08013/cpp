#!/bin/sh
# Simple test case to validate that ranges generation is working.
EXT=pdf
CS='1'
MP='--no-multiprocess'
OPS='--operation_list pareto'
TOPOS='--topo os3e'
FORCE='--force'

#for C in ${CS}
#do
  #python3 ./generate.py ${TOPOS} --from_start ${C} --lat_metrics -w -e ${EXT} ${FORCE} ${MP} ${OPS}
#done
python3 ./generate.py ${TOPOS} --from_start 1 --lat_metrics -w -e ${EXT} ${FORCE} ${MP} ${OPS}
python3 ./generate.py ${TOPOS} --from_start 2 --lat_metrics -w -e ${EXT} ${FORCE} ${MP} ${OPS}
python3 ./generate.py ${TOPOS} --from_start 3 --lat_metrics -w -e ${EXT} ${FORCE} ${MP} ${OPS}
python3 ./generate.py ${TOPOS} --from_start 4 --lat_metrics -w -e ${EXT} ${FORCE} ${MP} ${OPS}
python3 ./generate.py ${TOPOS} --from_start 5 --lat_metrics -w -e ${EXT} ${FORCE} ${MP} ${OPS}
