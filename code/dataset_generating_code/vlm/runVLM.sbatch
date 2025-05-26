#!/bin/bash
# Lines that begin with #SBATCH specify commands to be used by SLURM for scheduling
#SBATCH --job-name=temp

#SBATCH --qos=medium
#SBATCH --partition=class
#SBATCH --account=class

#SBATCH --gres=gpu:rtxa5000:2
#SBATCH --cpus-per-task=4
#SBATCH --mem=32gb
#SBATCH --time=24:00:00

python3 runCSV.py
