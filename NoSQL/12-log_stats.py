"""
12-log_stats.py
A script to analyze logs in the nginx collection of MongoDB.

This script connects to the MongoDB database, retrieves log data from the 'nginx' collection,
and provides statistics on HTTP methods used in the logs. It also checks the state of the
collection and can stop the MongoDB server if needed.

Usage:
- Run the script to get statistics on the nginx log collection.
"""

from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']  # Connect to the 'logs' database
    collection = db['nginx']  # Access the 'nginx' collection

    # Check the number of documents in the collection
    count = collection.count_documents({})
    if count == 0:
        print("Collection nginx empty")
    elif count == 1:
        print("Collection nginx with 1 document")
    elif count == 10:
        print("Collection nginx with 10 documents")
    else:
        print("Collection nginx with a lot of documents")

    # Query to get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Query to get the count of HTTP methods
    methods_count = {
        "GET": collection.count_documents({"method": "GET"}),
        "POST": collection.count_documents({"method": "POST"}),
        "PUT": collection.count_documents({"method": "PUT"}),
        "PATCH": collection.count_documents({"method": "PATCH"}),
        "DELETE": collection.count_documents({"method": "DELETE"})
    }

    # Print the counts of each method
    for method, count in methods_count.items():
        print(f"method {method}: {count}")

    # Optional: Stop MongoDB server (ensure you have permissions)
    # Uncomment the following line if you want to stop MongoDB
    # client.admin.command('shutdown')

if __name__ == "__main__":
    main()
