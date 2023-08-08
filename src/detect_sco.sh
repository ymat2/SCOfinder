#$ -S /bin/bash
#$ -l s_vmem=16G
#$ -l mem_req=16G
#$ -o /dev/null
#$ -e ./job
#$ -cwd

[ ! -d ./sco/pep ] && mkdir -p ./sco/pep
[ ! -d ./sco/cds ] && mkdir -p ./sco/cds

python3 src/blast2sco.py \
  --directory blst \
  --reference GCF_000001405.40 \
  --table out/species.tsv \
  --minsp 3 \
  --output out/single_copy_orthologs.tsv

python3 src/separate_seq.py -f seq -t pep -l out/single_copy_orthologs.tsv -o sco/pep
python3 src/separate_seq.py -f seq -t cds -l out/single_copy_orthologs.tsv -o sco/cds
