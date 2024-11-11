class User:
    def __init__(self, user_id, name, role="guest"):
        self.user_id = user_id
        self.name = name
        self.role = role

    def get_info(self):
        return f"User: {self.name}, Role: {self.role}"


class DataFetcher:
    def fetch_data(self):
        return

class DataProcessor:
    def process(self, data):
        processed_data = f"Processed {data}"
        return processed_data


class DataStorage:
    def __init__(self):
        self._storage = []

    def save(self, data):
        self._storage.append(data)
        print(f"Data saved: {data}")

    def get_all_data(self):
        return self._storage