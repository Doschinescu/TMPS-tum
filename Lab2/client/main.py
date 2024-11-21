from data_source import DataFetcher  
from utilities.adapter import DataFetcherAdapter, ExternalDataService  
from utilities.facade import DataFacade  
from utilities.decorator import DataFetcherLogger, CachedDataFetcher  

def main():
    fetcher = DataFetcher()
    external_service = ExternalDataService()  
    adapted_fetcher = DataFetcherAdapter(external_service)  

    print("Fetching data using DataFetcherAdapter:")
    print(adapted_fetcher.fetch_data())
    print("\nUsing DataFacade to fetch, process, and store data:")

    facade = DataFacade()
    record = facade.fetch_process_store_data()

    print(f"Fetched and processed record: {record}")
    print("\nUsing Decorators for logging and caching:")

    logged_fetcher = DataFetcherLogger(fetcher)
    cached_fetcher = CachedDataFetcher(logged_fetcher)

    print("\nFirst fetch (should be logged and cached):")
    data1 = cached_fetcher.fetch_data()
    print("\nSecond fetch (should use cached data):")
    data2 = cached_fetcher.fetch_data()

if __name__ == "__main__":
    main()
