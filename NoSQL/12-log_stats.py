#!/usr/bin/env python3
"""
12-log_stats.py

This script connects to a MongoDB database and analyzes the logs stored in the
'nginx' collection. It provides the following statistics:

1. The total number of log entries.
2. The count of HTTP methods (GET, POST, PUT, PATCH, DELETE) used in the logs.
3. The number of GET requests specifically targeting the '/status' endpoint.

Usage:
    Run the script in an environment where MongoDB is accessible, and the 
    'logs' database contains the 'nginx' collection.

Dependencies:
    - pymongo: The MongoDB driver for Python. Install via pip if not already installed.
"""

from pymongo import MongoClient

def main():
    """
    Main function to execute log analysis.
    
    Connects to the MongoDB database, retrieves log statistics, and prints
    them to the console.
    """
    # Establish a connection to the MongoDB server
    client = MongoClient()
    
    # Access the 'logs' database
    db = client.logs
    
    # Get the total number of logs in the 'nginx' collection
    total_logs = db.nginx.count_documents({})
    print(f"{total_logs} logs")  # Adjusted output to match expected format

    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    
    # Count and display the number of documents for each method
    for method in methods:
        count = db.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")  # Adjusted method case to lowercase
    
    # Count GET requests to the '/status' path
    status_check_count = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")  # Adjusted output to match expected format

if __name__ == "__main__":
    main()
