
from dotenv import load_dotenv
from services.json_service import jsonService
from buisness.suggestion_buisness import SuggestionBusiness
from buisness.cartography import CartographyAlgorithm
from config.logging_config import setup_logging
from services.youtube_service import YoutubeService


load_dotenv()
setup_logging()

def main():
   
   
    s_b = SuggestionBusiness()
    s_b.get_youtube_suggestions_by_keywords()
    y_service = YoutubeService()
    j_service = jsonService("youtube_suggestions_list.json")
    c_a = CartographyAlgorithm("data/youtube_suggestions_list.json",y_service,j_service)
    c_a.deep_search()
    

if __name__ == "__main__":
    main()
