from domain.core_classes import User, DataFetcher, DataProcessor, DataStorage

class UserFactory:
    @staticmethod
    def create_user(user_id, name, role="guest"):
        return User(user_id, name, role)

class DataFetcherFactory:
    @staticmethod
    def create_data_fetcher():
        return DataFetcher()

class DataProcessorFactory:
    @staticmethod
    def create_data_processor():
        return DataProcessor()

class DataStorageFactory:
    @staticmethod
    def create_data_storage():
        return DataStorage()
