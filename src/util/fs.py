from Bio import SeqIO


def fasta2dict(fasta):
	id2seq = {}
	desc2seq = {}
	for record in SeqIO.parse(fasta, "fasta"):
		_id, _desc, _seq = record.id, record.description, record.seq
		id2seq[_id] = str(_seq)
		desc2seq[_desc] = str(_seq)
	return desc2seq


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
