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


from services.json_service import jsonService


from buisness.suggestion_buisness import SuggestionBuisness

from buisness.cartography import CartographyAlgorithme




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
    s_b = SuggestionBuisness()
    s_b.get_youtube_suggestions_by_keywords()
    y_service = YoutubeService()
    j_service = jsonService("youtube_suggestions_list.json")
    c_a = CartographyAlgorithme("data/youtube_suggestions_list.json",y_service,j_service)
    c_a.deep_search()



   





    



   

if __name__ == "__main__":
    main()
