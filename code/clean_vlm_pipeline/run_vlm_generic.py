import os
import csv
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
import torch
import time

# Define the folder where images are stored
image_folder = ""
output_file = ""

# Get the total number of images in the folder
image_files = [filename for filename in os.listdir(image_folder) if filename.endswith((".jpg", ".png", ".jpeg"))]
total_images = len(image_files)


# Load the processor and model
with torch.no_grad():
    processor = AutoProcessor.from_pretrained(
        'allenai/Molmo-7B-O-0924',
        trust_remote_code=True,
        torch_dtype="auto",
        device_map='auto'
    )
    model = AutoModelForCausalLM.from_pretrained(
        'allenai/Molmo-7B-O-0924',
        trust_remote_code=True,
        torch_dtype="auto",
        device_map='auto'
    )

    # Open the CSV file
    with open(output_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # If the file is new, add a header row
        if os.stat(output_file).st_size == 0:
            writer.writerow(["Image Name", "Description"])
        
        # Loop through each file in the sliced folder
        for count, filename in enumerate(image_files, start=start_index + 1):
            image_path = os.path.join(image_folder, filename)
            
            # Try opening the file as an image
            try:
                with Image.open(image_path).convert("RGB") as image:
                    print(f"Processing image {count}/{total_images}: {filename}")
                    start = time.time()

                    # Process the image and text
                    inputs = processor.process(
                        images=[image],
                        # Testing different prompts.
                        text=(
                            "Analyze the provided image and describe it in such a way that someone who cannot see the image can vividly imagine what it might sound like. Focus on the actions, atmosphere, and elements in the scene that suggest specific sounds or an ambiance. Avoid directly referencing visual details but instead translate them into auditory impressions. Your description should evoke a clear sense of the sounds and the mood of the scene."
                        )
                    )

                    # Move inputs to the correct device
                    inputs = {k: v.to(device=model.device).unsqueeze(0) for k, v in inputs.items()}

                    # Generate output with max 200 new tokens, stop when "<|endoftext|>" is reached
                    output = model.generate_from_batch(
                        inputs,
                        GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
                        tokenizer=processor.tokenizer
                    )

                    # Only get generated tokens; decode them to text
                    generated_tokens = output[0, inputs['input_ids'].size(1):]
                    generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

                    # Write the image name and description to the CSV file
                    writer.writerow([filename, generated_text])

                    # Print the generated text and time taken
                    print(f"{filename}: {generated_text}")
                    print("Time taken:", time.time() - start)
            
            except (IOError, Image.UnidentifiedImageError):
                # Skip if the file is not a valid image
                print(f"Skipping file {filename}: not a valid image.")

    print(f"Descriptions saved to {output_file}")
