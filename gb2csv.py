import sys

from Bio import SeqIO

inputPath = sys.argv[1]
outputPath = sys.argv[2]

gbk_filename = inputPath
csv_filename = outputPath

input_handle  = open(gbk_filename, "r")
output_handle = open(csv_filename, "w")

for gb_record in SeqIO.parse(input_handle, "genbank"):
    print("Dealing with GenBank record %s" % gb_record.id)
    output_handle.write('"%s","%s","%s"\n' % (
           gb_record.id,
           gb_record.description,
           gb_record.seq))

output_handle.close()
input_handle.close()

print("Done.")