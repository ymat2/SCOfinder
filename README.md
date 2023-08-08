# Single Copy Ortholog Finder

## Requirements
### General
- Unix-like environment
- python3 (>= 3.9.0)

### Bioinformatics tools
- blast (>= 2.11.0+)
- [NCBI Datasets command line tools](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/)
- [mafft](https://mafft.cbrc.jp/alignment/software/) (>= 7.487)
- [trimAl](http://trimal.cgenomics.org/) (>= 1.4.1)

### Python libraries
- biopython

### Input file
- textfile with a column of NCBI accession ID


## Pipeline

```sh
## get sequences from NCBI
qsub src/get_seq.sh out/accession.list

## run vs_human blastp
qsub src/make_blast_db.sh accession.list
qsub src/run_blast.sh accession.list GCF_000001405.40
bzip2 blst/*.pep.fa.*

## identify SCO from blastp
qsub src/detect_sco.sh

## alignment and trimming
ls sco/pep/ | awk -F '.' '{print $1}' > out/sco.list
qsub src/align.sh out/sco.list
qsub src/trim.sh out/sco.list
```
