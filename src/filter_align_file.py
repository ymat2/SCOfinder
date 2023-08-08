import argparse
import os
from util import fs

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-a", "--aln")
  parser.add_argument("--min_sp", type=int, default=3)
  parser.add_argument("--min_seqlen", type=int, default=10)
  args = parser.parse_args()

  aln = fs.fasta2dict(args.aln)
  seq = aln.get("Homo_sapiens", "NA")

  if len(aln) < args.min_sp:
    print("Number of species is less than %d." % (args.min_sp))
    os.remove(args.aln)

  if seq == "NA":
    print("This alignment lacks homo_sapiens sequens.")
  elif len(seq) < args.min_seqlen:
    print("Length of sequences is less than %d." % (args.min_seqlen))
    os.remove(args.aln)


if __name__ == "__main__":
  main()
