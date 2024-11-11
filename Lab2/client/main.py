from utilities.adapter import DataSource, DataSourceAdapter
from utilities.facade import DataFacade
from utilities.decorator import BaseFunctionality, FeatureDecorator

def main():
    data_source = DataSource()
    adapter = DataSourceAdapter(data_source)
    facade = DataFacade(adapter)
    result = facade.fetch_and_process_data()
    print(result)

    base = BaseFunctionality()
    decorated = FeatureDecorator(base)
    print(decorated.operation())

if __name__ == "__main__":
    main()
