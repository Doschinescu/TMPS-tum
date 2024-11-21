import json

class DataFetcher:
    def __init__(self, data_file="data/data_source.json"):
        self.data_file = data_file

    def load_data(self):
        with open(self.data_file, "r") as file:
            data = json.load(file)
        return data

    def fetch_users(self):
        data = self.load_data()
        return data["users"]

    def fetch_data_records(self):
        data = self.load_data()
        return data["data_records"]

    def fetch_logs(self):
        data = self.load_data()
        return data["logs"]

