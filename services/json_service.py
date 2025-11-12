
import json
import os
from pathlib import Path
class jsonService:
    def __init__(self,json_file_name):
        self.json_file_path = Path(os.getenv("DATA_FOLDER_PATH")) / json_file_name
        self.json_file_path.parent.mkdir(parents=True,exist_ok=True)

    
    def write(self,content,mode):
        with self.json_file_path.open(mode,encoding=os.getenv('ENCODING')) as f:
            try:
                json.dump(content,f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Error while writing in json file :{e} ")


    def read(self):
        with self.json_file_path.open("r",encoding=os.getenv('ENCODING')) as f:
            data = json.load(f)
        return data

