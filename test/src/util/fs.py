import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input")
	parser.add_argument("-o", "--output")
	args = parser.parse_args()

	id2seq = fasta2dict(args.input)
	write_fasta(id2seq, args.output)


def fasta2dict(fp):
	dct = {}
	with open(fp) as f:
		tid = ""
		for line in f:
			if line[0] == ">":
				tid = line.rstrip("\n")[1:]
				dct[tid] = ""
			else:
				dct[tid] += line.rstrip()
	return dct


def get_sp_name(string):
	sp_name = string.rstrip("\n")
	sp_name = sp_name.split("[")[-1]
	sp_name = sp_name.rstrip("]")
	sp_name = sp_name.replace(" ", "_")
	return sp_name


def write_fasta(dct, pth):
	with open(pth, "w") as f:
		for id in dct:
			seq = dct[id]
			f.write(">"+id+"\n")
			f.write(seq+"\n")


if __name__ == "__main__":
	main()
