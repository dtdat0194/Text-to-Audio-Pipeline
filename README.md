# Text-to-Audio Dataset Creation Pipeline

This project provides an **automated pipeline for creating text-to-audio datasets** for mundane sounds, combining video download, keyframe extraction, vision-language modeling, audio captioning, and dataset evaluation.

---

## Features

- **Automated video and audio download** from YouTube using CSV metadata.
- **Keyframe extraction** from videos for visual context.
- **Vision-Language Model (VLM)** to generate descriptions from keyframes.
- **Audio Captioning** using the GAMA model for audio-based descriptions.
- **Dataset evaluation** using standard metrics (BLEU, ROUGE, METEOR, CIDEr, SPICE).
- **Well-documented and modular codebase** for easy extension.

---

## Pipeline Overview

1. **Prepare CSV Metadata**  
   - Format: `youtube_id`, `start_seconds`  
   - See `code/clean_vlm_pipeline/csv_to_vlm.ipynb` for details.

2. **Download Videos & Extract Keyframes/Audio**  
   - Run the notebook:  
     `code/clean_vlm_pipeline/csv_to_vlm.ipynb`  
   - Outputs: Keyframes and audio clips for each video.

3. **Generate Visual Descriptions (VLM)**  
   - Script:  
     `code/dataset_generating_code/vlm/runVLM.py`  
   - Produces: Textual descriptions for each keyframe.

4. **Audio Captioning (GAMA Model)**  
   - See `code/gama/README.md` for setup.  
   - Batch inference:  
     `code/gama/GAMA_API_TEST.py`  
   - Produces: Audio captions for each audio clip.

5. **Dataset Evaluation**  
   - See `code/evaluation/README.md` for instructions.  
   - Converts outputs to evaluation format and computes metrics.

6. **Dataset Structure**  
   - See `dataset/README.md` for details on generated files and formats.

---

## Project Structure

```
code/
  clean_vlm_pipeline/
    csv_to_vlm.ipynb         # Main notebook for video/audio/keyframe extraction
  dataset_generating_code/
    vlm/
      runVLM.py              # VLM inference script
      runVLM.sbatch          # Example SLURM batch script
  gama/
    GAMA_API_TEST.py         # Batch inference for audio captioning
    README.md                # GAMA usage instructions
  evaluation/
    README.md                # Evaluation instructions and scripts
dataset/
  README.md                  # Dataset file descriptions
  audiocaps_generated_captions/
  audioset_generated_captions/
```

---

## Setup & Usage

1. **Clone this repository**
   ```bash
   git clone https://github.com/dtdat0194/Text-to-Audio-Pipeline.git
   cd Text-to-Audio-Pipeline
   ```

2. **Install dependencies**  
   - See each submodule's README for environment setup.
   - Main requirements: `yt_dlp`, `katna`, `ffmpeg`, `GAMA` (see [GAMA repo](https://github.com/Sreyan88/GAMA)), and evaluation metrics ([eval4imagecaption](https://github.com/Aldenhovel/bleu-rouge-meteor-cider-spice-eval4imagecaption/tree/main)).

3. **Follow the pipeline steps above** for your dataset creation and evaluation.

---

## Credits

This project was originally developed as a group project for CMSC473/673 at UMD.  
Contributors: [Your Group Names Here]

---

## For Developers

- The original technical README is available as `README-dev.md` for detailed references.
