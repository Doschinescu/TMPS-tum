class User:
    """Represents a user in the system."""
    def __init__(self, user_id, name, role="guest"):
        self.user_id = user_id
        self.name = name
        self.role = role

    def get_info(self):
        return f"User: {self.name}, Role: {self.role}"


class DataFetcher:
    """Fetches data from a database or external API."""
    def fetch_data(self):
        return "Sample data from external source"

class DataProcessor:
    """Processes data for business logic."""
    def process(self, data):
        processed_data = f"Processed {data}"
        return processed_data


class DataStorage:
    """Stores processed data."""
    def __init__(self):
        self._storage = []

    def save(self, data):
        self._storage.append(data)
        print(f"Data saved: {data}")

    def get_all_data(self):
        return self._storage