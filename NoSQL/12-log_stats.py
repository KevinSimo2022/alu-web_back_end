#!/usr/bin/env python3
"""Python script to gather statistics from Nginx logs stored in MongoDB."""
from pymongo import MongoClient

# List of HTTP methods to track in the logs.
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """
    Displays statistics about Nginx logs from a MongoDB collection.

    If an HTTP method is provided as 'option', it prints the count of logs
    matching that method. Otherwise, it prints the total number of logs,
    individual counts for each HTTP method, and the number of status check
    requests (i.e., requests to the '/status' path).
    """
    items = {}  # Empty filter to fetch all log entries.

    if option:
        # Count and print the number of logs matching the specified method.
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}}
        )
        print(f"\tmethod {option}: {value}")
        return

    # Print the total number of logs in the collection.
    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    
    print("Methods:")
    # Recursively call log_stats to display counts for each HTTP method.
    for method in METHODS:
        log_stats(nginx_collection, method)

    # Count and print the number of status check requests.
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to the MongoDB server and access the 'nginx' collection.
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    
    # Call the log_stats function to display log statistics.
    log_stats(nginx_collection)
