from domain.core_classes import DataFetcher

class ExternalDataService:
    def retrieve_data(self):
        return "Data from an external service"

class DataFetcherAdapter(DataFetcher):
    def __init__(self, external_service):
        self.external_service = external_service

    def fetch_data(self):
        return self.external_service.retrieve_data()
