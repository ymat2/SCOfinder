import argparse
from util import fs

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--infile")
  parser.add_argument("-o", "--outfile")
  args = parser.parse_args()

  f = fs.fasta2dict(args.infile)
  f = amb2x(f)
  fs.write_fasta(f, args.outfile)


def amb2x(dct):
  dct_amb2x = dct
  amb_aa = ["B", "Z", "J", "U", "O"]
  for k in dct_amb2x:
    for chr in amb_aa:
      dct_amb2x[k] = dct_amb2x[k].replace(chr, "-")
  return dct_amb2x


if __name__ == "__main__":
  main()
