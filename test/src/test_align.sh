#$ -S /bin/bash
#$ -t 1-5:1
#$ -cwd
#$ -o /dev/null
#$ -e ./job/


seq_ids=()
while read -r x; do
  seq_ids+=($x)
done < $1
seq_id=${seq_ids[$SGE_TASK_ID-1]}

[ ! -d ./test/aln ] && mkdir ./test/aln

python3 src/concat.py \
	-p sco/pep/${seq_id}.pep.fa \
	-c sco/cds/${seq_id}.cds.fa \
	-o test/aln/${seq_id}.concat.fa

singularity exec /usr/local/biotools/m/mafft:7.520--h031d066_2 mafft \
	--auto --anysymbol --quiet \
	test/aln/${seq_id}.concat.fa > test/aln/${seq_id}.concat.aln.fa

python3 test/src/test_pal2nal.py \
	-a test/aln/test/aln/${seq_id}.concat.aln.fa \
	-c sco/cds/${seq_id}.cds.fa \
	-o test/aln/${seq_id}

rm test/aln/${seq_id}.concat.fa
