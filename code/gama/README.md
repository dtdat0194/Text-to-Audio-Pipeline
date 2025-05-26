The GAMA model can be found at https://github.com/Sreyan88/GAMA

Follow the instruction there to set up the environment

Make sure to follow the error messages to change all the model directories in the code.

Instead of running:
	
	python gama_inf.py

The script used in our project is:
	
	python inference_gradio_gama.py

"GAMA_API_TEST.py" is the code for batch inference. 

Be aware that sometimes ffmpeg would not be able to recognize the language in the file name, i.e. Russian and Japanese, causing the batch inference to be stopped. In our project, these files are manually removed and renamed.
