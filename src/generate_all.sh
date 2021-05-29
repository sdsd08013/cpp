#!/bin/sh
# Generate everything for all topologies that we can geocode.
# To run: time ./generate_all.sh > generate_all_log &
# To view: tail -n20 -f generate_all_log
TOPO=os3e
EXT=pdf
#MAX=5  # add --max $MAX at the end of generate.py to debug only a few topos. 
#MAX='--max 2'
CS='5'
FORCE='-f'
MP='--no-multiprocess'
MP='--processes 4'
OPS='--operation_list metrics'
# Everything except metrics:
#OPS='--operation_list cdfs,ranges,pareto,cloud'
TOPOS='--all_topos'
#TOPOS='--topo Iris'

#for C in ${CS}
#do
  #echo "writing all for num controllers ${C}"
  #echo "*********************"
  #python3 ./generate.py ${TOPO} --from_start ${C} --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
#done
echo "writing all for num controllers 1"
echo "*********************"
python3 ./generate.py ${TOPO} --from_start 1 --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
echo "writing all for num controllers 2"
echo "*********************"
python3 ./generate.py ${TOPO} --from_start 2 --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
echo "writing all for num controllers 3"
echo "*********************"
python3 ./generate.py ${TOPO} --from_start 3 --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
echo "writing all for num controllers 4"
echo "*********************"
python3 ./generate.py ${TOPO} --from_start 4 --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
echo "writing all for num controllers 5"
echo "*********************"
python3 ./generate.py ${TOPO} --from_start 5 --lat_metrics -w --write_dist --write_combos -w -e ${EXT} ${FORCE} ${MP} ${OPS} ${MAX}
