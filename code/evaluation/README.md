Please first go to https://github.com/Aldenhovel/bleu-rouge-meteor-cider-spice-eval4imagecaption/tree/main to download the code for evaluation metrics.

	pip install pycocoevalcap
	python main.py

The input file should be in the same format as "captions_example.json" and "references_example.json" in example folder.
For readability I took part of the data in these two example and constructed two smaller file in the example folder in this repository.

captions_format_example.json
references_format_example.json

In "utils" folder, three files are provided for converting the .txt files in dataset folder into evaluable json files.

	"Caption_to_json.py"  changes automated generated caption .txt file to a json file that can input to Evaluation_matrics.
	
	"Audiocaps_csv_to_json.py"  changes the original audiocaps dataset .csv file to a json file that can input to evaluation_matrics.

Be aware that the result json file of these two .py are different. The evaluation matrics takes caption and reference in different format.
For some reason, captions from VLM may requires " encoding='ISO-8859-1' " to read and write with. 
SPICE metrics evaluation on VLM is not success, it is unknown that whether the length of VLM captions causing extra long time to evaluate the similarity, or SPICE metrics package enters deadlock when encountering this specific encoding.

It seems like GitHub erases the last '\n' line of the .txt files. Make sure to add them so that the codes can read the .txt files normally.

	"match_data_tobe_evaluated.py" compares the file_ids in both the reference and caption json file. This is necessary when there are data points appear in either reference or caption but not both. 
The output of the code are two "temp" json files that are ready to be put inside evaluation matrices.

In all the .py files, please change the input and output file names according to the need.
