
import logging
import os
from supabase import create_client
logger = logging.getLogger("app_log")
class SupaBase:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")

        try:
            self.client = create_client(self.url, self.key)
        except Exception as e:
            logger.error(f"Failed to initiate Supabase DB - Make sure to have the right api_key in .env. :{e}")