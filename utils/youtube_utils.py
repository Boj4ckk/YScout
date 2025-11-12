





import json
import os
import random
import string
import time
import requests


class YoutubeUtils:

    
    @staticmethod
    def get_youtube_suggestions_list(keyword, lang=os.getenv("LANG"), country=os.getenv("COUNTRY"), use_proxy=None):
        
        params = {
            "client": os.getenv("CLIENT"),
            "ds": os.getenv("DS"),
            "hl": os.getenv("LANG"),
            "gl": os.getenv("COUNTRY"),
            "q" : keyword,
    
        }
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": f"{lang}-{country},{lang};q=0.9",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "DNT": "1"
        }

        response = requests.get(os.getenv("YOUTUBE_SUGGESTION_URL"), params=params,headers=headers, proxies=use_proxy)
        response.raise_for_status()
        data = response.json()
        
        return data[1] if len(data) > 1 else []
    

    @staticmethod
    def get_youtube_suggestions_by_keywords():
        suggestions_list = {}
        keyword_list = os.getenv("KEYWORD_LIST", "")
        keyword_list = [kw.strip() for kw in keyword_list.split(",") if kw.strip()]

        for keyword in keyword_list:
            suggestions_list[YoutubeUtils.get_youtube_suggestions_list(keyword)[0]] = YoutubeUtils.get_youtube_suggestions_list(keyword)
            suggestions_list[YoutubeUtils.get_youtube_suggestions_list(keyword)[0]].pop(0)

        return suggestions_list
    
    
       






