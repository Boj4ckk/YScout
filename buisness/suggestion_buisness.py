import logging
from services import suggestion_service
import os
from services.csv_service import csvService
from services.json_service import jsonService

logger = logging.getLogger("app_log")
class SuggestionBusiness:
    """
    Business logic class for handling YouTube keyword suggestions.
    Uses SuggestionService to fetch suggestions, manages CSV keyword consumption, and writes results to JSON.
    """

    def __init__(self):
        """
        Initialize the SuggestionBusiness with a configured SuggestionService instance.
        """
        self.suggestion_service = suggestion_service.SuggestionService(
            lang=os.getenv("LANG"),
            country=os.getenv("COUNTRY"),
            client=os.getenv("CLIENT"),
            hl=os.getenv("LANG"),
            gl=os.getenv("COUNTRY"),
            ds=os.getenv("DS"),
            suggestion_url=os.getenv("YOUTUBE_SUGGESTION_URL")
        )

    def get_youtube_suggestions_by_keywords(self):
        """
        Fetches YouTube suggestions for keywords from a CSV file, removes used keywords, and writes results to a JSON file.
        Returns:
            dict: Dictionary of suggestions grouped by the first suggestion for each keyword.
        """
        suggestions_list = {}
        csv_service = csvService("youtube_keywords.csv")
        keyword_list = csv_service.get_csv_keywords()
        used_indices = []

        # Limit to 5 keywords per run to avoid API rate limits or being flagged as abusive
        for idx, keyword in enumerate(keyword_list[0:5]):
            try:
                logger.info(f"Fetching suggestions for keyword: '{keyword}'...")
                suggestions = self.suggestion_service.get_suggestions_list(keyword)
                if suggestions:
                    suggestions_list[suggestions[0]] = suggestions
                    suggestions_list[suggestions[0]].pop(0)
                used_indices.append(idx)
            except Exception as e:
                logger.error(f"Error occurred while injecting CSV keyword into SuggestionService: {e}")

        # Remove consumed lines from the CSV file
        # Note: Remove from highest index to lowest to avoid shifting indices
        for idx in sorted(used_indices, reverse=True):
            csv_service.remove_line_from_csv(idx)

        # Write the suggestions to a JSON file
        j_service = jsonService("youtube_suggestions_list.json")
        j_service.write(suggestions_list, 'w')
