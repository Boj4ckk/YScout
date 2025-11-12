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

    ids = ",".join(YoutubeUtils.extract_channels_id_in_response("search_by_keyword_response.json"))
    y_service  = YoutubeService()
    response = y_service.get_channels_data_by_ids(ids)
    j_service = jsonService("channels_response.json")
    j_service.write(response,"a+")






    



   

if __name__ == "__main__":
    main()
