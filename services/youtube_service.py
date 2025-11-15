
import os
from dotenv import load_dotenv
import google_auth_oauthlib.flow
import googleapiclient.discovery
import logging

load_dotenv()
logger = logging.getLogger("app_log")

class YoutubeService:
    """
    Service class for accessing the YouTube Data API using OAuth2 authentication.
    Handles authentication, API client initialization, and provides methods for search and channel data retrieval.
    """

    def __init__(self):
        """
        Initialize the YouTube API client using OAuth2 credentials.
        Loads configuration from environment variables:
            - CLIENT_SECRET_FILE: Path to the OAuth2 client secrets file.
            - SCOPES: Comma-separated list of OAuth2 scopes.
            - API_SERVICE_NAME: Name of the YouTube API service.
            - API_VERSION: Version of the YouTube API.
        Raises:
            ValueError: If any required environment variable is missing.
            Exception: If authentication or client initialization fails.
        """
        required_env = ["CLIENT_SECRET_FILE", "SCOPES", "API_SERVICE_NAME", "API_VERSION"]
        for var in required_env:
            if os.getenv(var) is None:
                raise ValueError(f"{var} environment variable is undefined.")

        try:

            # Start OAuth2 flow and build the YouTube API client
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
            logger.info("Youtube service initiated successfully.")
        except Exception as e:
            # Log initialization errors
            logger.error(f"Error while initiating Youtube service: {e}")
        

    def search_by_keyword(self, keyword, max_result=1, part="snippet"):
        """
        Search for YouTube videos or channels by keyword.
        Args:
            keyword (str): The search query.
            max_result (int): Maximum number of results to return.
            part (str): The resource parts to include in the response (default: 'snippet').
        Returns:
            dict or None: The API response containing search results, or None if an error occurred.
        """
        try:
            request = self.youtube_client.search().list(
                part=part,
                maxResults=max_result,
                q=keyword
            )
            response = request.execute()
            logger.info(f"YouTube search successful for keyword: '{keyword}'.")
            return response
        except Exception as e:
            logger.error(f"Failed to search YouTube with keyword '{keyword}': {e}")
            return None
    
    def get_channels_data_by_ids(self, channels_id_query):
        """
        Retrieve detailed data for one or more YouTube channels by their IDs.
        Args:
            channels_id_query (str): Comma-separated list of channel IDs.
        Returns:
            dict or None: The API response containing channel details, or None if an error occurred.
        """
        try:
            request = self.youtube_client.channels().list(
                part="snippet,statistics",
                id=channels_id_query
            )
            response = request.execute()
            logger.info(f"Fetched channel data successfully for IDs: {channels_id_query}.")
            return response
        except Exception as e:
            logger.error(f"Failed to get channel data for IDs '{channels_id_query}': {e}")
            return None


