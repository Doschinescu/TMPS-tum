from domain.core_classes import DataFetcher

class DataFetcherLogger:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def fetch_data(self):
        data = self.fetcher.fetch_data()
        print(f"[LOG] Data fetched: {data}")
        return data

class CachedDataFetcher:
    def __init__(self, fetcher):
        self.fetcher = fetcher
        self.cache = None

    def fetch_data(self):
        if self.cache is None:
            self.cache = self.fetcher.fetch_data()
            print("[CACHE] Data fetched and cached.")
        else:
            print("[CACHE] Returning cached data.")
        return self.cache
