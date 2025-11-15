
import os
import logging
from services.supabase_service import SupaBase


class DatabaseBuisness:
    """
    Business logic for formatting and inserting YouTube channel data into the database.
    """
    def __init__(self, db_client: SupaBase):
        """
        Initialize DatabaseBuisness with a SupaBase client.
        """
        self.db_client = db_client
        self.channel_table_name = os.getenv("CHANNEL_TABLE_NAME")

    def insert_channel_into_db(self, channels_data):
        """
        Format and insert each channel from channels_data into the database.
        Logs success and error for each insert operation.
        """
        for channel in channels_data["items"]:
            try:
                channel_snippet = channel["snippet"]
                channel_statistics = channel["statistics"]
                data = {
                    "channelId": channel["id"],
                    "publishedAt": channel_snippet["publishedAt"],
                    "title": channel_snippet["title"],
                    "description": channel_snippet["description"],
                    "customUrl": channel_snippet.get("customUrl"),
                    "thumbnail": channel_snippet["thumbnails"]["default"]["url"],
                    "country": channel_snippet.get("country"),
                    "viewCount": channel_statistics["viewCount"],
                    "subscriberCount": channel_statistics["subscriberCount"],
                    "videoCount": channel_statistics["videoCount"],
                }
                self.db_client.insert_data(self.channel_table_name, data)
                logging.info(f"Inserted channel {data['channelId']} into table {self.channel_table_name}.")
            except Exception as e:
                logging.error(f"Failed to insert channel {channel.get('id', 'unknown')}: {e}")
        

            
