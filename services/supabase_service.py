
import logging
import os
from supabase import create_client
logger = logging.getLogger("app_log")
class SupaBase:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")

        try:
            self.supabase = create_client(self.url, self.key)
        except Exception as e:
            logger.error(f"Failed to initiate Supabase DB - Make sure to have the right api_key in .env. :{e}")
    

    def insert_data(self, table, data):
        try:
            response = (
                self.supabase.table(table)
                .insert(data)
                .execute()
            )
            logging.info(f"Inserted into supabase : {response}")
        except Exception as e:
            logger.error(f"Failed to insert data into {table} for the given data: {data}. {e}")