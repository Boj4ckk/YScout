import base64
import json
import os
from pathlib import Path

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
from dotenv import load_dotenv


from services.youtube_service import YoutubeService
from utils.youtube_utils import YoutubeUtils

from services.json_service import jsonService






load_dotenv()
def main():
   
    """
    yt_service = YoutubeService()
    youtube_client = yt_service.youtube_client

    request = youtube_client.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()
    print(response)
    """
    suggestion_list = YoutubeUtils.get_youtube_suggestions_by_keywords()
    json_service = jsonService(os.getenv("JSON_FILE_NAME"))

    json_service.write(suggestion_list)



#class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"
    



   

if __name__ == "__main__":
    main()
