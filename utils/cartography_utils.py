





import json
import os
import random
import string
import time
import requests
from services.json_service import jsonService
from services.youtube_service import YoutubeService


class CartographyUtils:
    
    @staticmethod
    def extract_channels_id_in_response(response):
      
        channels_id_list = []
        # response doit être un dict, on accède à la clé 'items'
        for item in response.get("items", []):
            item_channel_id = item["snippet"]["channelId"]
            channels_id_list.append(item_channel_id)
        return channels_id_list
        
    @staticmethod
    def search_channel_by_keyword(keyword,youtube_service: YoutubeService):
        search_response = youtube_service.search_by_keyword(keyword)

        channels_id_query = ",".join(CartographyUtils.extract_channels_id_in_response(search_response))
        channels_data_response = youtube_service.get_channels_data_by_ids(channels_id_query)
        return channels_data_response





    
    
       






