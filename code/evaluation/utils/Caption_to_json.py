import json
#This file changes a txt caption file (following the format mentioned in readme), into a json file, to be fed into evaluation metrices.


#Change filename accordingly
f = open("Audioset_GAMA_captions.txt","r")
existing_caption = f.readlines()

#Caption_dict make sure no duplicate data exist.
caption_dict = {}
index = 0
while index < len(existing_caption):
    caption_dict[existing_caption[index][:-1]] = existing_caption[index+1][:-1] #last char is '\n'.
    index+=3 #Follows the format of txt file, one data point takes three lines
f.close()

#print(len(caption_dict))


#Change the dict into a json file that can be put into evaluation metrics
json_list = []
for image_id in caption_dict.keys():
    temp = {}
    temp["image_id"] = image_id
    temp["caption"] = caption_dict[image_id]
    
    
    json_list.append(temp)
real_json = json.dumps(json_list)

#Change filename accordingly
f = open("Audiocaps_GAMA_captions.json","w")
f.write(real_json)
f.close()


