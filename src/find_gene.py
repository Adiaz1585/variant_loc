import sys
import pandas as pd
from time import sleep
from random import random
from tqdm import tqdm
from multiprocessing import Process
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def read_dat(filename, sep = ','):
	dat = pd.read_csv(filename,sep=sep)
	return dat

# This function iterates through each variant located in the specific
# chromosome. A different function will be called to find specific genes
# that variant might live within.
def set_chrm(gchr,exon_chroms,found_genes,chrm):
	# print(gchr)
	for var in gchr["position"]:
		change = gchr.loc[gchr['position'] == var,'variant']
		find_gene(var, exon_chroms, found_genes, chrm, change)


	# 	print(var)
	# 	print(gchr['Chrom'].iat[0], len(gchr))

# This function will search for genes that the variant will live in.
# it is not guaranteed that a variant lives with any gene.
def find_gene(variant, exon_chroms,found_genes,chrm,change):
	gene_name_ind = exon_chroms.columns.get_loc("gene_name")
	start_ind 	  = exon_chroms.columns.get_loc("Start")
	end_ind 	  = exon_chroms.columns.get_loc("End")

	for row in exon_chroms.values:
		if variant >= int(row[start_ind]) and variant <= int(row[end_ind]):
			# print(variant)
			temp = pd.DataFrame({'chr': [chrm],'gene' : [row[gene_name_ind]], 'position': [variant], 'variant': [change], 'start': [row[start_ind]],'end': [row[end_ind]]})
			found_genes.append(temp)


def main():
	gwas_path 	= "/media/austin/local2/girirajan_rotation/practice/practice/data/depression_gwas.csv"
	exon_path 	= "/media/austin/local2/girirajan_rotation/practice/practice/data/filtered_regions.csv"
	gwas_df 	= read_dat(gwas_path)
	exons_df 	= read_dat(exon_path)

	gwas_df.rename(columns={'chr':'Chrom'},inplace=True)
	#print(gwas_df.columns)
	# print(int("chr12".split("r")[-1]))

	chromes 	= gwas_df["Chrom"].unique()
	# this will sort only if numbered chromosomes are present.
	# next steps would be to seperate the numbered chr from lettered then sort then append lettered
	# chromes = sorted(chromes, key=lambda x:int(x.split("r")[-1]))
	
	# print(chromes)

	found_genes_dict = {'chr': [],'gene' : [], 'position': [], 'variant': [], 'start': [],'end': []}
	found_genes 	 = pd.DataFrame(data = found_genes_dict)

	processes = []
	for chrm in chromes:
		exon_chroms = exons_df.loc[exons_df['Chrom'] == chrm]
		gchr 		= gwas_df.loc[gwas_df['Chrom'] 	 ==  chrm]

		processes.append(Process(target=set_chrm, args=(gchr,exon_chroms,found_genes,chrm,)))

	for process in processes:
		process.start()
	for process in tqdm(processes):
		process.join()
	print()	
	print('done',flush=True )

	found_genes.to_csv("/media/austin/local2/girirajan_rotation/practice/practice/data/found_genes.csv")

	# print(chr1)
	# print(gchr1)





	#current_chrom = 

	#exon_merge = pd.merge(exons_df,gwas_df, how='inner',on="Chrom")


	#print(exon_merge.head())

if __name__ == '__main__':
	main()