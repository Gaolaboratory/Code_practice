with open(r"C:\Users\bathy\Desktop\Coding_training\UniProt_Human.fasta") as fin:
    split_list = [protein for protein in fin.read()[1:].split('\n>')]

split_line = split_list[0].split('\n')
uniprot_id = split_line[0].split('|')[1]
seq = "".join(split_line[1:])
seq_rev = seq[::-1]
