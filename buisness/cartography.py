from services.json_service import jsonService

from services.youtube_service import YoutubeService
from utils.cartography_utils import CartographyUtils

class CartographyAlgorithm:
    def __init__ (self,suggestion_file,youtube_service: YoutubeService, json_service:jsonService ):
        self.suggestion_file = suggestion_file
        self.youtube_service = youtube_service
        self.json_service = json_service
        self.cartography_utils = CartographyUtils()

    
    def seed_search(self):
   
        for key, values in self.json_service.read().items():
            print(self.cartography_utils.search_channel_by_keyword(key,self.youtube_service))
    
    def deep_search(self):
        for key, values in self.json_service.read().items():
            for value in values:
                print(self.cartography_utils.search_channel_by_keyword(value,self.youtube_service))




            
        
        


    
