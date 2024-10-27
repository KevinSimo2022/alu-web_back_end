#!/usr/bin/env python3
from pymongo import MongoClient

def main():
    """
    Analyzes logs in the 'nginx' collection of MongoDB.
    
    Prints the total number of logs, the count of different HTTP methods,
    and the count of GET requests to the '/status' endpoint.
    """
    # Establish a connection to the MongoDB server
    client = MongoClient()
    
    # Access the 'logs' database
    db = client.logs
    
    # Get the total number of logs in the 'nginx' collection
    total_logs = db.nginx.count_documents({})
    print(f"Total logs: {total_logs} logs")

    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    
    # Count and display the number of documents for each method
    for method in methods:
        count = db.nginx.count_documents({"method": method})
        print(f"\tMethod {method}: {count}")
    
    # Count GET requests to the '/status' path
    status_check_count = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"GET requests to /status: {status_check_count} status check")

if __name__ == "__main__":
    main()
