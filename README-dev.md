# audio-group-CMSC473-673-project

Here we present our deliverables for our Automated Pipeline for Text-to-Audio Dataset Creation for Mundane Sound.

# The Code
All code has been properly commented/documented:

A notebook to download the videos from the CSV and extract the keyframes/audio to be inputted to the VLM and Audio Captioning Model can be found at `audio-group-CMSC473-673-project/code/clean_vlm_pipeline/csv_to_vlm.ipynb`. Instructions on how to run this notebook to achieve the desired result are present at the top of the notebook.

A script to run the VLM on the keyframes extracted from the previous step can be found at `audio-group-CMSC473-673-project/code/dataset_generating_code/vlm/runVLM.py`. Comments are present throughout the code explainig the steps of the script, and an sbatch script to run the job on nexus is present in the same directory.

Code to run GAMA (the Audio Captioning model that we used) can be found, along with it's own README documentation in `audio-group-CMSC473-673-project/code/gama`.

Code that we used to evaluate our dataset can be found, along with it's own README documentation in `audio-group-CMSC473-673-project/code/evaluation`.

# The Dataset
Our dataset deliverables can be found, along with it's own README documentation in `audio-group-CMSC473-673-project/dataset` 