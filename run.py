
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from dotenv import load_dotenv

from services.youtube_service import YoutubeService


load_dotenv()
def main():
   

    yt_service = YoutubeService()
    youtube_client = yt_service.youtube_client()

    request = youtube_client.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()
    print(response)

   

if __name__ == "__main__":
    main()
