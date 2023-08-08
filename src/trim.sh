#$ -S /bin/bash
#$ -t 1-19024:1
#$ -cwd
#$ -o /dev/null
#$ -e ./job/align_trim.log.e
#$ -tc 250


seq_ids=()
while read -r x; do
  seq_ids+=($x)
done < $1
seq_id=${seq_ids[$SGE_TASK_ID-1]}

[ ! -d ./trimal ] && mkdir ./trimal

if [ -s ./aln/${seq_id}.cds.aln.fa ]; then
	singularity exec /usr/local/biotools/t/trimal:1.4.1--0 trimal \
		-in aln/${seq_id}.pep.aln.fa \
		-out trimal/${seq_id}.pep.aln.trim.fa \
		-resoverlap 0.50 \
		-seqoverlap 95 \
		-strict
fi

if [ -s ./aln/${seq_id}.cds.aln.fa ]; then
	singularity exec /usr/local/biotools/t/trimal:1.4.1--0 trimal \
		-in aln/${seq_id}.cds.aln.fa \
		-out trimal/${seq_id}.cds.aln.trim.fa \
		-nogaps
fi
