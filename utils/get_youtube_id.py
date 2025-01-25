from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import os,json


#Get secret key 
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file, 'r') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


def get_youtube_id_and_thumbnail (serach_word):
    results = []
    try:
        API_KEY = get_secret("YOUTUBE_DATA_API_KEY")
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        serach_response = youtube.search().list(
            q=str(serach_word), order="relevance", part="snippet", maxResults=3).execute()
        
        for i in range(3):
            videoId = serach_response['items'][i]['id']['videoId']
            title = serach_response['items'][i]['snippet']['title']
            thumbnail = serach_response['items'][i]['snippet']['thumbnails']['high']['url']

            musicAttr = {
                "videoId" : videoId,
                "title" : title,
                "thumbnail" : thumbnail
            }

            results.append(musicAttr)
        
        return results

    except:
        raise Exception()