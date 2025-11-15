

import logging
import os

import requests

logger = logging.getLogger("app_log")
class SuggestionService:
    """
    Service class for fetching YouTube search suggestions using the public suggestion API.
    Handles request configuration, error logging, and result parsing.
    """

    def __init__(self, suggestion_url, lang, country, client, ds, hl, gl):
        """
        Initialize the SuggestionService with all required parameters for the API request.
        Args:
            suggestion_url (str): The URL of the suggestion API endpoint.
            lang (str): Language code for the request.
            country (str): Country code for the request.
            client (str): Client identifier for the API.
            ds (str): Data source parameter for the API.
            hl (str): Language parameter for the API.
            gl (str): Country parameter for the API.
        """
        self.lang = lang
        self.country = country
        self.client = client
        self.ds = ds
        self.hl = hl
        self.gl = gl
        self.suggestion_url = suggestion_url

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": f"{self.lang}-{self.country},{self.lang};q=0.9",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "DNT": "1"
        }
        logger.info(
            f"Initialized SuggestionService with parameters: "
            f"suggestion_url='{self.suggestion_url}', lang='{self.lang}', country='{self.country}', "
            f"client='{self.client}', ds='{self.ds}', hl='{self.hl}', gl='{self.gl}'"
        )

    def get_suggestions_list(self, keyword):
        """
        Fetches suggestion list for a given keyword from the suggestion API.
        Args:
            keyword (str): The keyword to fetch suggestions for.
        Returns:
            list: List of suggestions for the keyword, or an empty list if an error occurred.
        """
        params = {
            "client": self.client,
            "ds": self.ds,
            "hl": self.hl,
            "gl": self.gl,
            "q": keyword,
        }
        try:
            response = requests.get(self.suggestion_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Fetched suggestions list successfully for keyword: '{keyword}'.")
            return data[1] if len(data) > 1 else []
        except Exception as e:
            logger.error(f"Error occurred while fetching suggestion list from the API for keyword '{keyword}': {e}")
            return []