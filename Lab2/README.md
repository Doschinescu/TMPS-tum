**Structural Design Patterns**
*Author: Doschinescu Dan*


*Introduction/Theory*

In modern software development, design patterns are essential to providing solutions to common software design problems.
They provide templates that help solve problems in a reusable and flexible way. 
In this laboratory work, I explored and implemented several creational and structural design patterns,
particularly focusing on Builder, Factory, Facade, Decorator, and Adapter patterns.


**Implementation & Explanation**
*Creational Patterns: Builder and Factory*

*Builder Pattern*

The Builder Pattern is used to construct a complex object step by step. 
It allows for creating different representations of an object using the same construction process.

In my implementation, I used the Builder pattern to create a User object.
 The UserBuilder class allows for step-by-step customization of the user object, 
 ensuring that the required fields are properly set before the user object is created. 
 This is especially useful when creating complex user profiles with various optional fields like email and phone.

*Code Snippet*

```python
class UserBuilder:
    def __init__(self):
        self.user_id = None
        self.name = "Guest"
        self.role = "guest"
        self.email = None
        self.phone = None

    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
```

*Main Idea & Motivation*
The Builder pattern ensures flexibility in creating User objects without having to deal with a complicated constructor. 
It is especially useful when the object being created has many optional attributes.

*Factory Pattern*

The Factory Pattern provides an interface for creating objects in a super class,
 but allows subclasses to alter the type of objects that will be created. In my implementation,
the factory pattern is used to create various objects like User, DataFetcher, and DataProcessor.

*Code Snippet:*

```python
class UserFactory:
    @staticmethod
    def create_user(user_id, name, role="guest"):
        return User(user_id, name, role)

class DataFetcherFactory:
    @staticmethod
    def create_data_fetcher():
        return DataFetcher()
```

*Main Idea & Motivation:* 
The Factory pattern simplifies object creation by encapsulating the instantiation logic,
 allowing for easier maintenance and the addition of new object types in the future. 
 It promotes loose coupling between client code and object creation.


**Structural Patterns: Facade, Adapter, Decorator**

*Facade Pattern*
The Facade Pattern provides a simplified interface to a complex subsystem. 
In my implementation, the DataFacade class acts as a facade, 
providing a simplified method to fetch, process, and store data using multiple components 
under the hood (data fetcher, processor, and storage).

*Code Snippet:*

```python
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
```

*Main Idea & Motivation:*
 The Facade pattern is used to reduce the complexity of interacting with multiple subsystems. 
 Instead of calling each subsystem directly, the DataFacade provides a simple method for users to fetch, process, and store data.

*Adapter Pattern*
The Adapter Pattern is used to allow two incompatible interfaces to work together. 
In this case, I created an adapter class to adapt the ExternalDataService to work with the DataFetcher class.

*Code Snippet:*

```python
class ExternalDataService:
    def retrieve_data(self):
        return "Data from an external service"

class DataFetcherAdapter(DataFetcher):
    def __init__(self, external_service):
        self.external_service = external_service

    def fetch_data(self):
        return self.external_service.retrieve_data()
```


*Main Idea & Motivation:* 
The Adapter pattern is essential when integrating external systems or third-party services. 
It allows the DataFetcher to use ExternalDataService without changing its interface.

*Decorator Pattern*
The Decorator Pattern adds functionality to an object dynamically. 
In my implementation, I used the decorator pattern to log data fetching operations and cache the fetched data.

*Code Snippet:*

```python
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
```

*Main Idea and Motivation:* 
The Decorator pattern is used to dynamically add new functionality to an object without altering its core structure.
 In this case, logging and caching are added to the data fetching process.


**Results/Conclusions**
*Results*
The implementation of the design patterns has proven effective in structuring the software in a modular and flexible way.
 Each pattern provided significant benefits in terms of flexibility and maintainability.

*Conclusions*
This laboratory work has demonstrated the power of design patterns in improving software design.
 By using patterns like Builder, Factory, Facade, Decorator, and Adapter, 
 I was able to create a modular system that is easy to extend and maintain. 
 Each pattern plays a key role in managing complexity, improving code reusability, and reducing the coupling between components.