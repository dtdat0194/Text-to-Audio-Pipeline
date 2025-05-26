# Script to test vlm on first frame of one of the dataset videos

from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
from PIL import Image
import requests
import cv2
import numpy as np

# read video frames into numpy array

frames = []

path = "test_video.mp4"
video_name = path[:len(path) - 4]
cap = cv2.VideoCapture(path)
ret = True
while ret:
    ret, img = cap.read()
    if ret:
        frames.append(img)
video = np.stack(frames, axis=0)
first_frame = video[0]

processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-34b-hf") 

# prepare image and text prompt, using the appropriate prompt template
image = Image.fromarray(first_frame)

# Define a chat histiry and use `apply_chat_template` to get correctly formatted prompt
# Each value in "content" has to be a list of dicts with types ("text", "image") 
conversation = [
    {

      "role": "user",
      "content": [
          {"type": "text", "text": "What is shown in this image?"},
          {"type": "image"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

inputs = processor(images=image, text=prompt, return_tensors="pt")

torch.cuda.empty_cache()

model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-34b-hf", torch_dtype=torch.float16, low_cpu_mem_usage=True, cache_dir='/fs/class-projects/fall2024/cmsc473/c473g000/hf_cache', device_map='auto')

# autoregressively complete prompt
output = model.generate(**inputs, max_new_tokens=100)

print(processor.decode(output[0], skip_special_tokens=True))
