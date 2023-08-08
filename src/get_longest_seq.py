import argparse
from util import fs, parsegtf

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--indir")
	parser.add_argument("-o", "--outdir")
	args = parser.parse_args()

	cds = args.indir+"/cds_from_genomic.fna"
	pep = args.indir+"/protein.faa"
	gtf = args.indir+"/genomic.gtf"

	longest_seq = gls(cds, pep, gtf)

	longest_pep = {}
	longest_cds = {}

	for gn in longest_seq:
		longest_pep[gn] = longest_seq[gn][0]
		longest_cds[gn] = longest_seq[gn][1]

	fs.write_fasta(longest_pep, args.outdir+".pep.fa")
	fs.write_fasta(longest_cds, args.outdir+".cds.fa")


def gls(cds_pth, pep_pth, gtf_pth):
	longest = {}
	cds_dict = fs.fasta2dict(cds_pth)
	cds_dict = {get_prot_id(k): v for k, v in cds_dict.items()}
	pep_dict = fs.fasta2dict(pep_pth)
	px2id = parsegtf.gtf2dict(gtf_pth)

	for line in pep_dict:
		prot_id = line.split(" ")[0]
		gene_id = px2id[prot_id]
		pep_seq = pep_dict[line]
		len_pep_seq = len(pep_seq)
		cds_seq = cds_dict[prot_id]
		sp = fs.get_sp_name(line)
		dict_key = gene_id+"_"+sp
		if dict_key not in longest:
			longest[dict_key] = [pep_seq, cds_seq]
		elif len_pep_seq > len(longest[dict_key][0]):
			longest[dict_key] = [pep_seq, cds_seq]

	return longest


def get_prot_id(line):
	if "protein_id" in line:
		new_key = line.split("[protein_id=")[1].split("]")[0]
	else:
		new_key = line.split(" ")[0]
	return new_key


if __name__ == "__main__":
	main()
