from datetime import datetime

class UserProfile:
    def __init__(self, user_id, name, role="guest", email=None, phone=None):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone

    def __str__(self):
        return (f"UserProfile(id={self.user_id}, name={self.name}, role={self.role}, "
                f"email={self.email}, phone={self.phone})")

class DataRecord:
    def __init__(self, raw_data, processed_data=None, timestamp=None):
        self.raw_data = raw_data
        self.processed_data = processed_data
        self.timestamp = timestamp if timestamp else datetime.now()

    def mark_processed(self, processed_data):
        self.processed_data = processed_data
        self.timestamp = datetime.now()

    def __str__(self):
        return (f"DataRecord(raw_data='{self.raw_data}', processed_data='{self.processed_data}', "
                f"timestamp={self.timestamp})")

class DataLog:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        if isinstance(record, DataRecord):
            self.records.append(record)
            print(f"Added record: {record}")
        else:
            raise ValueError("Only DataRecord instances can be added to the DataLog")

    def get_all_records(self):
        return self.records

    def __str__(self):
        return f"DataLog with {len(self.records)} records"