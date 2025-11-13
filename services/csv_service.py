


import csv
import os


class csvService:
    def __init__(self,csv_file):
        self.csv_file = csv_file


    
    def get_csv_keywords(self):
        keywords = []
        with open(f'{os.getenv("DATA_FOLDER_PATH")}/{self.csv_file}', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                keywords.append(row['keyword'])

        return keywords

    def remove_line_from_csv(self, index):
        # reads all lines
        with open(f'{os.getenv("DATA_FOLDER_PATH")}/{self.csv_file}', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # ignore first line 
        data_lines = lines[1:]
        if index < 0 or index >= len(data_lines):
            raise IndexError("Index hors limites")
        # delete chosen line
        del data_lines[index]
        # print if no data left
        if not data_lines:
            print("The csv file is now empty.")
        # re write all others lines
        with open(f'{os.getenv("DATA_FOLDER_PATH")}/{self.csv_file}', 'w', encoding='utf-8') as file:
            file.write(lines[0])  # entête
            file.writelines(data_lines)
        