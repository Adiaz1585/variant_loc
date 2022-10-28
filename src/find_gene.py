import sys
import pandas as pd

def read_dat(filename, sep = ','):
	dat = pd.read_csv(filename,sep=sep)
	return dat


def main():
	gwas_path 	= "/media/austin/local2/girirajan_rotation/practice/practice/data/depression_gwas.csv"
	exon_path 	= "/media/austin/local2/girirajan_rotation/practice/practice/data/gencode.v19.parsed.exons.csv"
	gwas_df 	= read_dat(gwas_path)
	exons_df 	= read_dat(exon_path)

	gwas_df.rename(columns={'chr':'Chrom'},inplace=True)
	print(gwas_df.columns)
	

	exon_merge = pd.merge(exons_df,gwas_df, how='inner',on="Chrom")


	print(exon_merge.head())

if __name__ == '__main__':
	main()