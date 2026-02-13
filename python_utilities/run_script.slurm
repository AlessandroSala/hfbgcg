#!/bin/bash
#SBATCH --time=05:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=128
#SBATCH --mem=4G
#SBATCH --output=slurm-%j.out

INPUT=$1

./out $INPUT

