import argparse
import re

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input")
	parser.add_argument("-o", "--output")
	args = parser.parse_args()
	px2ids = gtf2dict(args.input)
	with open(args.output, "w") as fout:
		for k in px2ids:
			fout.write(k+"\t")
			fout.write("\t".join(px2ids[k])+"\n")

def gtf2dict(fl):
	ln = set()
	prot2ids = {}
	with open(fl) as fin:
		for line in fin:
			attribute = line.rstrip().split("\t")[-1]
			ln.add(re.sub(r"; exon_number.+", "", attribute))
	for l in ln:
		attribute = l.split("; ")
		att = {k.split(" ")[0]: k.split(" ")[-1].strip("\"") for k in attribute}
		gene_id = att.get("gene", "NA")
		prot_id = att.get("protein_id", "NA")
		if prot_id not in prot2ids:
			prot2ids[prot_id] = gene_id
	return prot2ids

if __name__ == "__main__":
	main()
