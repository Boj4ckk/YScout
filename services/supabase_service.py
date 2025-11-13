


import os
from supabase import create_client

class SupaBase:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")

        try:
            self.client = create_client(self.url, self.key)
        except Exception as e:
            print(f"Error while creating supabase client !  : {e} ")