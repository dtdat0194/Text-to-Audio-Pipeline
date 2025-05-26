#!/bin/bash
# Lines that begin with #SBATCH specify commands to be used by SLURM for scheduling
#SBATCH --job-name=temp

#SBATCH --qos=default
#SBATCH --partition=class
#SBATCH --account=class

#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32gb
#SBATCH --time=24:00:00

#SBATCH --mail-user=asood12@terpmail.umd.edu
#SBATCH --mail-type=FAIL,ARRAY_TASKS

module load Python3/3.11.2
python3 test.py
