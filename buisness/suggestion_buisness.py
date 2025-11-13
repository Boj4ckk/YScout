from services import suggestion_service
import os
from services.csv_service import csvService
from services.json_service import jsonService
class SuggestionBuisness:

    def __init__(self):
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
        suggestions_list = {}
        csv_service = csvService("youtube_keywords.csv")
        keyword_list = csv_service.get_csv_keywords()
        used_indices = []

        for idx, keyword in enumerate(keyword_list[0:5]):  # use 8 keyword max
            try:
                suggestions = self.suggestion_service.get_suggestions_list(keyword)
                print(f"retrieve suggestions for keyword: {keyword}.\n Result : {suggestions}")
                if suggestions:
                    suggestions_list[suggestions[0]] = suggestions
                    suggestions_list[suggestions[0]].pop(0)
                used_indices.append(idx)
            except Exception as e:
                print(f"Erreur pour le mot-clé '{keyword}': {e}")

        # Supprime les lignes consommées du CSV
        # Attention : suppression en partant du plus grand index pour éviter le décalage
        for idx in sorted(used_indices, reverse=True):
            csv_service.remove_line_from_csv(idx)

        j_service = jsonService("youtube_suggestions_list.json")
        j_service.write(suggestions_list,'w')
