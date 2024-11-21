from factories.factory import DataFetcherFactory, DataProcessorFactory, DataStorageFactory
from models.data_models import DataRecord, DataLog

class DataFacade:
    def __init__(self):
        self.fetcher = DataFetcherFactory.create_data_fetcher()
        self.processor = DataProcessorFactory.create_data_processor()
        self.storage = DataStorageFactory.create_data_storage()
        self.log = DataLog()

    def fetch_process_store_data(self):
        raw_data = self.fetcher.fetch_data()
        processed_data = self.processor.process(raw_data)
        record = DataRecord(raw_data=raw_data, processed_data=processed_data)
        self.storage.save(record)
        self.log.add_record(record)
        
        return record

    def get_all_records(self):
        return self.log.get_all_records()
