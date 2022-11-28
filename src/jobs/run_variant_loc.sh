#!/bin/bash
#SBATCH --account=girirajan
#SBATCH --partition=girirajan
#SBATCH --job-name=pract
#SBATCH -o out.log
#SBATCH -e error.log
#SBATCH --time=4:00:00
#SBATCH --cpus-per-task=20
#SBATCH --mem-per-cpu=256000
#SBATCH --chdir /data5/austin/work/variant_loc/variant_loc/src
#SBATCH --nodelist ramona
#SBATCH --ntasks 1
#SBATCH --nodes 1
python find_gene.py
