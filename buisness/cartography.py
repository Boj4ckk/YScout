import logging
from services.json_service import jsonService
from services.youtube_service import YoutubeService
from utils.cartography_utils import CartographyUtils

logger = logging.getLogger("app_log")

class CartographyAlgorithm:
    """
    Business logic class for performing cartography operations on YouTube channel suggestions.
    Provides methods for seed-based and deep keyword-based channel searches using the YouTube API.
    """

    def __init__(self, suggestion_file, youtube_service: YoutubeService, json_service: jsonService):
        """
        Initialize the CartographyAlgorithm with required services and utilities.
        Args:
            suggestion_file (str): Path to the suggestion JSON file.
            youtube_service (YoutubeService): Instance of YoutubeService for API calls.
            json_service (jsonService): Instance of jsonService for reading suggestions.
        """
        self.suggestion_file = suggestion_file
        self.youtube_service = youtube_service
        self.json_service = json_service
        self.cartography_utils = CartographyUtils()

    def seed_search(self):
        """
        Performs a search for each seed keyword found in the suggestion JSON file.
        Logs the result of each channel search.
        """
        for key, values in self.json_service.read().items():
            result = self.cartography_utils.search_channel_by_keyword(key, self.youtube_service)
            logger.info(f"Seed search for keyword '{key}': {result}")

    def deep_search(self):
        """
        Performs a deep search for each suggestion keyword found in the suggestion JSON file.
        Logs the result of each channel search for every suggestion.
        """
        for key, values in self.json_service.read().items():
            for value in values:
                result = self.cartography_utils.search_channel_by_keyword(value, self.youtube_service)
                logger.info(f"Deep search for suggestion '{value}' (seed '{key}'): {result}")




            
        
        


    
