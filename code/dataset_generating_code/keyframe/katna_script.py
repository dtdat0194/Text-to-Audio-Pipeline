import pandas as pd
import numpy as np
import json
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
import cv2

YOUTUBE_URL_PREFIX = "https://www.youtube.com/watch?v="
BATCH_SIZE = 10

def clean_data_labels(data_path, label_json_path, output_path = None):
    def cleaning(label):
        label = label.replace('"', '').replace(' ', '')
        return ';'.join([id_label_map[i] for i in label.split(';')])

    df = pd.read_csv(data_path)

    with open(label_json_path, 'r') as file:
        data = json.load(file)

    id_label_map = {dictionary['id'] : dictionary['name'] for dictionary in data}

    df['positive_labels'] = df[' positive_labels'].apply(cleaning)

    if output_path:
        df.to_csv(output_path)
    return df


def cleaning(label, clean):
    label = label.replace('"', '').replace(' ', '')
    return ';'.join([clean[i] for i in label.split(';')])


def download_video(video_url):
    opts = {'paths': {'home': '/fs/class-projects/fall2024/cmsc473/c473g000/downloads'}}
    with YoutubeDL(opts) as yt:
        try: 
            yt.download(video_url)
            print(f"Downloaded video: {video_url}")
        except:
            print(f"Download failed: {video_url}")


def download_column(yt_ids, stop=None):
    # If stop is None, set it to the length of yt_ids
    stop = len(yt_ids) if stop is None else stop

    # Iterate through the specified number of items
    for yt_id in yt_ids[:stop]:
        download_video(YOUTUBE_URL_PREFIX + yt_id)

def download_column_2(yt_ids, start, stop=None):
    # If stop is None, set it to the length of yt_ids
    stop = len(yt_ids) if stop is None else stop

    # Iterate through the specified number of items
    for yt_id in yt_ids[start:start+stop]:
        download_video(YOUTUBE_URL_PREFIX + yt_id)


def get_timestamps(yt_ids, start, stop=None):
    # If stop is None, set it to the length of yt_ids
    stop = len(yt_ids) if stop is None else stop
    timestamps = []
    # Iterate through the specified number of items
    for yt_id in yt_ids[start:start+stop]:
        timestamps.append()

# Taken from https://www.scraperapi.com/blog/how-to-scrape-youtube/
## Downloading a YouTube Video
def download_video(video_url):
    opts = {'paths': {'home': '/fs/class-projects/fall2024/cmsc473/c473g000/downloads'}}
    with YoutubeDL(opts) as yt:
        try:
            yt.download(video_url)
            print(f"Downloaded video: {video_url}")
        except:
            print(f"Downloaded failed: {video_url}")


def main():
    df = clean_data_labels('/fs/class-projects/fall2024/cmsc473/c473g000/eval_segments_reg_clean.csv', '/fs/class-projects/fall2024/cmsc473/c473g000/ontology.json')
    df = pd.read_csv('/fs/class-projects/fall2024/cmsc473/c473g000/eval_segments_reg_clean.csv')
    # Path to your JSON file
    file_path = '/fs/class-projects/fall2024/cmsc473/c473g000/ontology.json'

    # Open the file and load the data
    with open(file_path, 'r') as file:
        data = json.load(file)

    clean = {dictionary['id'] : dictionary['name'] for dictionary in data}

    df['real'] = df[' positive_labels'].apply(cleaning, args=(clean,))

    print(df.columns)

    for i in range(0, len(df), BATCH_SIZE):
        yt_ids = []
        for j in range(i, i + BATCH_SIZE):
            yt_ids.append(df.iloc[j]['# YTID'])
        download_column_2(yt_ids, i)

        for file in os.listdir('/fs/class-projects/fall2024/cmsc473/c473g000/downloads'):
            filename = os.fsdecode(file)
            extension = filename.split(".")[1]
            row = df.loc[df['# YTID'] == (filename.split('['))[1].split(']')[0]]

            ffmpeg_extract_subclip(f"/fs/class-projects/fall2024/cmsc473/c473g000/downloads/{filename}", float(row[' start_seconds']), float(row[' end_seconds']), f"/fs/class-projects/fall2024/cmsc473/c473g000/cut/{filename.split('.')[0]}_cut.{extension}")
            # attempt at a opencv/numpy approach:
            '''frames = []

            cap = cv2.VideoCapture(f"/fs/class-projects/fall2024/cmsc473/c473g000/downloads/{filename}")
            ret = True
            while ret:
                ret, img = cap.read()
                if ret:
                    frames.append(img)
            print(np.shape(frames))
            video = np.stack(frames, axis=0)
            print(np.shape(video))
            print(row[' start_seconds'])
            print(row[' end_seconds'])
            fps = cap.get(cv2.CAP_PROP_FPS)
            print(fps)
            cut_video = video[int(fps * float(row[' start_seconds'])):int(fps * float(row[' end_seconds']))]
            print(np.shape(cut_video))
            out = cv2.VideoWriter(f"/fs/class-projects/fall2024/cmsc473/c473g000/cut/{filename.split('.')[0]}_cut.{extension}",
                    cv2.VideoWriter_fourcc(*'mp4v'), int(fps), (np.shape(cut_video)[2], np.shape(cut_video)[1]), False)
            for i in range(len(cut_video)):
                out.write(cut_video[i].astype('uint8'))
            out.release()'''

            vd = Video()
            no_of_frames_to_returned = 1
            # initialize diskwriter to save data at desired location
            diskwriter = KeyFrameDiskWriter(location="/fs/class-projects/fall2024/cmsc473/c473g000/selectedframes")

            # Video file path
            video_file_path = f'/fs/class-projects/fall2024/cmsc473/c473g000/cut/{filename.split(".")[0]}_cut.{extension}'

            # extract keyframes and process data with diskwriter
            vd.extract_video_keyframes(
                no_of_frames=no_of_frames_to_returned, file_path=video_file_path,
                writer=diskwriter)

            os.remove(f"/fs/class-projects/fall2024/cmsc473/c473g000/downloads/{filename}")
            os.remove(f'/fs/class-projects/fall2024/cmsc473/c473g000/cut/{filename.split(".")[0]}_cut.{extension}')


if __name__ == '__main__':
    main()
