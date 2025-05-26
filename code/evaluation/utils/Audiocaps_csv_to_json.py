import csv
import json
#This file converts Audiocaps csv file into a json file that can be read by Evaluation metrics.

Audiocap_csv = [] 
with open('train.csv', encoding='utf8',mode ='r')as file: #Audiocaps csv file directory
  csvFile = csv.reader(file)
  for lines in csvFile:
        Audiocap_csv.append(lines)

id_list = []
caption_list = []
for i in Audiocap_csv: #Audiocaps csv is formated with second column containing youtube_id, fourth column containing caption
    id_list.append(i[1])
    caption_list.append(i[3])

#This session make sure that no duplicate data would be taken. Be aware that there are duplicated data points in val.csv for audiocaps
non_duplicate_dict = {}
for index in range(len(id_list)):
    non_duplicate_dict[id_list[index]] = caption_list[index]



image_id_list = []
annotation_list = []
#This session convert the non_duplicate_dict into the format that can be put into evaluation metrics, after being dumped into json file.
for file_id,caption in non_duplicate_dict.items():
    temp_dict = {}
    temp_dict["id"] = file_id
    image_id_list.append(temp_dict)

    temp_dict = {}
    temp_dict["id"] = file_id
    temp_dict["image_id"] = file_id
    temp_dict["caption"] = caption
    annotation_list.append(temp_dict)

json_dict = {}
json_dict["images"] = image_id_list
json_dict["annotations"] = annotation_list


#Dump the json, change the name of targeted filename when necessary
real_json = json.dumps(json_dict)
f = open("Audiocaps_train_and_val.json","w")
f.write(real_json)
f.close()
