# Code_practice

1. read the peptide column from psm.tsv
2. map all the peptides to the protein they belong (using the fasta file)
3. also, create a frequency coverage map of each identified protein (use bargraph from bokeh)
4. crate a dict which protein uniprot_id as key, and all the identified psm as value
output_dict['P11276'] = ['XXXX', 'XXXX', 'XXXX']
5. write a fasta processing script to create reverse sequence using rev_ as prefix, give three options for reverse (A) whole sequence reverse (B)segmented reverse based on cut site (KR) (C) random rearrangement

use pyahocorasick library
https://pypi.org/project/pyahocorasick/

try to write concise and modular code
do not use any other python package other than the python default and bokeh/matplotlib/numpy/pandas


# Pytorch practice 1
use the HeLa_200ng_1_20221004214655.pin file, split randomly for 80/20% training/testing
pytorch, first thing, create a peptide classifier
will be able to differentiate forward and reverse sequence based on hyperscore
you can use all the numbers from column exp_mass till peptide_length to predict the label column
the training target is about 1% error rate
