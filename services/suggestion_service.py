

import os

import requests


class SuggestionService:


    def __init__(self, suggestion_url, lang, country, client, ds, hl, gl ):
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

    def get_suggestions_list(self,keyword):
        params = {
            "client": self.client,
            "ds": self.ds,
            "hl": self.hl,
            "gl": self.gl,
            "q": keyword,
        }
     
        response = requests.get(self.suggestion_url, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data[1] if len(data) > 1 else []