import os
from gradio_client import Client
#This file do batch inference with gradio


directory = "/fs/class-projects/fall2024/cmsc473/c473g000/audio" # Folder for source audio to be infered
client = Client("https://7232c6ac0cffc5feda.gradio.live") #Change when a new gradio link is provided by GAMA code

# Change directory as needed
# output txt file is read first so existing file_id won't be inferenced again
# If error occurs, try to construct the .txt file before running the code
f = open("Audio_Captions_for_audiocaps_extra.txt","r")
existing_caption = f.readlines()
test_existing_caption = []



caption_dict = {}
count = 0
index = 0

# According to the format of txt file, one data point takes 3 lines.
while index < len(existing_caption):
    count+=1
    if existing_caption[index] == "":
        print("index",index)
    caption_dict[existing_caption[index][:-1]] = existing_caption[index+1][:-1]
    index+=3
f.close()

# Change directory as needed
f = open("Audio_Captions_for_audiocaps_extra.txt","a")

# This functions takes a filename, and output the file_id. Be aware that "[" and "]" sometimes appears in filename, so the search is done from end to start.
def obtain_file_id(name):
    length = len(name)
    start_index = length-1
    end_index = length-1
    index = length-1

    # flags for "[" and "]"
    flag0 = 0
    flag1 = 0
    while flag0 != 1 or flag1 != 1:
        character = name[index]
        if character == ']':
            end_index = index
            flag1 = 1
        if character == '[':
            start_index = index
            flag0 = 1
        index -=1
    return name[start_index+1:end_index]


'''
list1 = os.listdir(directory)
list2 = caption_dict.keys()
for i in range(len(list1)):
    list1[i] =  obtain_file_id(list1[i])
#print(list1)
#print(os.listdir(directory))
for elements in list2:
    if elements not in list1:
        #print("",end = '')
        print(elements)
'''

count = 0
first_element_flag = 0 # Do not print '\n' when the element is the first element in the txt file
if len(existing_caption) ==0:
    first_element_flag = 1

leng = len(os.listdir(directory))
for current_file_name in os.listdir(directory):
    file_id = obtain_file_id(current_file_name)
    if file_id in caption_dict.keys():
        # Skipping existing file_id
        count+=1
        continue
    print(count,"/",leng)
    print("current_file_name:",current_file_name)
    count += 1
    current_file_dir = os.path.join(directory,current_file_name)
    result = client.predict(
                current_file_dir,  # your audio file in 16K
                "Describe the audio.",    # your question
    )

    # Do not print '\n' when the element is the first element in the txt file
    if first_element_flag == 0:
        f.write("\n")
    else:
        first_element_flag = 0
    f.write(file_id)
    f.write("\n")
    f.write(result[1])
    f.write("\n")
f.close()
