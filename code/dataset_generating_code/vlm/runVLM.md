# How to Run the Code for Image Descriptions

This guide will help you run the code to generate auditory-focused descriptions for images stored in the `images` folder and save the output in a CSV file.

---

## **Steps to Run the Code**

### 1. **Connect to the Cluster**
   - Use your terminal to connect to the cluster:
     ```bash
     ssh <your_username>@<cluster_address>
     ```

### 2. **Navigate to the Project Directory**
   - Once connected, navigate to the project folder:
     ```bash
     cd /fs/class-projects/fall2024/cmsc473/c473g000
     ```

### 3. **Request a GPU**
   - To request GPU resources, run the following command:
     ```bash
     srun --partition=class --account=class --qos=<node_priority> --gres=gpu:<gpu_type>:<number_of_gpus> --pty bash
     ```
   - Example Fill-ins:
   - Replace placeholders as needed before running.
      - <node_priority>: default, medium, etc.
      - <gpu_type>: rtxa5000, a100, etc.
      - <number_of_gpus>: Number of GPUs to request, e.g., 1, 2.
      

### 4. **Test GPU Access**
   - Verify that the requested GPUs are accessible:
     ```bash
     nvidia-smi
     ```

   - You should see a list of available GPUs and their utilization stats. If not, confirm your allocation or request again.

### 5. **Run the Code**
   - To execute the script, ensure the `images` folder is populated with your images and the `runCSV.py` script is in the same directory.
   - Run the script using Python:
     ```bash
     python runCSV.py
     ```

### **What the Code Does**
- The script processes each image in the `images` folder.
- For each image:
  - It generates a detailed auditory description based on the visual content.
  - The output is saved in a CSV file named `image_descriptions.csv`.
- The CSV file includes:
  - **Column 1**: Image name (e.g., `dog.jpg`).
  - **Column 2**: Generated description (e.g., `"The sound of a dog barking amidst rustling leaves"`).

---

## **Output Location**
- After the script completes, the `image_descriptions.csv` file will be available in the same directory.

---

## **Troubleshooting**
1. **Permission Issues**:
   - Ensure you have the correct permissions for the cluster and the project directory.
2. **No GPU Detected**:
   - Confirm your allocation with `srun` and re-run `nvidia-smi`.
3. **Invalid Images**:
   - Ensure the images in the `images` folder are valid and supported formats (`.jpg`, `.png`, `.jpeg`).

---
EOL
