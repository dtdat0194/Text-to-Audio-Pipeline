10/8/2024
Jacob: Setup python environment to ensure consistency accross all groupmates. Ran into issues installing pyenv, so the group resorted to conda.

10/10/2024
Ayush: installed ffmpeg, got video -> audio conversion working

Jacob: Explored the shape of Audioset data. Identified formatting issues in label column. Resolved them to enable easy pandas integration.
TODO next: add python code to read audio into array

10/15/2024
Xinchen Yu: Setting up environment for audio captioning model

Dat Dao: Setting up image captioning model.

Aishani: Cleaning AudioSet of Speech and Music and requested access to feature embeddings

Jacob: Explored VLM options available on hugging space. Used Colab to get a toy example up and running.

10/17/2024
Xinchen Yu: API is not a good choice because queue is long. Seems like other users are doing their research. Trying to implement the model locally. For Nexus Pytorch implementation, a missing package may block the usage.

Jacob: Began install of Llava-32B model. Encountered issues relating to space and getting model downloaded on nexus.

10/22/2024
Xinchen Yu: Doing conda setups.

Dat Dao: Setup env on the server + Research on the recent model for Image Captioning (pixtral/molmo)

Aishani: Eval and Balanced sets cleaned of speech and music erasing half of data from 20k to around 11k

Jacob: Resolved Llava download challenge by properly caching in shared folder. Learned how to request access to GPU resources to run model.

10/24/2024
Xinchen Yu: It seems like conda virtual environment is constructed successfully. The API for LTU-AS works, trying to do the local inference. Need to find a way to convert sample rate to 16khz. Then cross-validation methods.

Jacob: Tested performance of Llava model on nexus. Found that runtime was far too slow. Worked with Sean to implement speedups.

10/29/2024
Xinchen Yu: Trying to understand how gradio work, and how LTU-AS inference script work.

Jacob: Continued testing Llava speedups, but nothing made a significant difference. The code was successfully running and we were able to generate output from the model.

10/31/2024
Aishani: Received access to AudioSet feature tar but need to examine how to read tfrecords and audio embeddings
https://github.com/google/youtube-8m/blob/master/readers.py
https://stackoverflow.com/questions/46204992/how-can-i-extract-the-audio-embeddings-features-from-google-s-audioset

Jacob: Transitioned to new model. Molmo-7B proved to be the most promising, began preparing to feed data to the model (scraping).

11/5/2024
Jacob: Shifted focus to preparing data for Molmo. Explored keyframe extraction options and landed on Katna.

11/7/2024
Jacob: Utilized Katna to validate our approach of Keyframe extraction. Katna can select a variable number of keyframes. Confirmed that when selecting a single keyframe, it was not just selected the "first" keyframe that appeared chronologically. 

11/12/2024
Xinchen Yu: LTU-AS can run now, --mem=64G is needed to load all the models. The gradio page can be created now. However, it fails to give output. Need further debug to make it work. A bad news is that both the APIs for LTU and LTU-AS are dead. ERROR is shown on the huggingface gradio page. The UI of local inference gradio is different from the UI of the demo page LTU-AS (in my memory, since the page is down for some reason). Hopefully the models are the same.

Jacob: Began writing a script to do all of the pre-VLM processing. This includes cleaning the Audioset data (filtering unwanted categories like speech and music out), scraping the Youtube videos, cuting them, extracting the audio and keyframes.

11/14/2024 Xinchen Yu: LTU-AS requires ffmpeg for whisper feature extracting. However, the NEXUS server does not have packages for easy ffmpeg installation. ffmpeg python package is not working as well, since it looks like the whisper feature extracting code use local installed ffmpeg instead of a package. Manually extracting whisper feature also requires a lot of time for composing a json file for dataset. The next step is to try to implement GAMA.

Jacob: Continued writing pre-VLM processing script.

11/19/2024 Xinchen Yu: GAMA successfully deployed on NEXUS server.

Jacob: Focused on extracting audio while Ayush focuses on keyframe extraction. Getting ffmpeg installed properly on the nexus server proves to be an issue.

11/26/2024 Xinchen Yu: aac-metrics package requires some strange depency of JAVA, I cannot understand how to utilize it. Switching to other SPICE matrix github program.

Jacob: Built ffmpeg from source on nexus. Enabled extracting audio on the cluster.

11/26/2024 Xinchen Yu: Evaluation matrix ready to go.
