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
    try:
        API_KEY = get_secret("YOUTUBE_DATA_API_KEY")
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        serach_response = youtube.search().list(
            q=str(serach_word), order="relevance", part="snippet", maxResults=2).execute()
        
        videoId = serach_response['items'][0]['id']['videoId']
        thumbnail = serach_response['items'][0]['snippet']['thumbnails']['high']['url']

        musicAttr = {
            "videoId" : videoId,
            "thumbnail" : thumbnail
        }
        
        return musicAttr

    except:
        raise Exception()
    
