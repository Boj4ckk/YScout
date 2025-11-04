
import os
from dotenv import load_dotenv
import google_auth_oauthlib.flow
import googleapiclient.discovery

load_dotenv()
class YoutubeService:
    """
    Service for accessing the YouTube API using OAuth2 authentication.
    """

    def __init__(self):
        """

        Initializes the YouTube client with OAuth2 credentials.
        Reads configuration from environment variables:
            - CLIENT_SECRET_FILE: Path to the OAuth2 client secrets file.
            - SCOPES: Comma-separated list of OAuth2 scopes.
            - API_SERVICE_NAME: Name of the YouTube API service.
            - API_VERSION: Version of the YouTube API.
        Raises:
            Exception: If authentication or client initialization fails.

        """
        required_env = ["CLIENT_SECRET_FILE" ,"SCOPES", "API_SERVICE_NAME","API_VERSION"]
        for var in required_env:
            if os.getenv(var) == None:
                raise ValueError(f"{var} environement variable is undefined.")
    
        try:         
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                os.getenv("CLIENT_SECRET_FILE"),
                os.getenv("SCOPES").split(","),
            )
            credentials = flow.run_local_server(port=8080)
            self.youtube_client = googleapiclient.discovery.build(
                os.getenv("API_SERVICE_NAME"),
                os.getenv("API_VERSION"),
                credentials=credentials
            )
        except Exception as e:
            # In case where the initalization fail.
            print(f"Error while initating Youtube service :{e}")




