#!/usr/bin/env python3
from pymongo import MongoClient

def main():
    client = MongoClient()
    db = client.logs
    # Get the total number of logs
    total_logs = db.nginx.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = db.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    # Count GET requests to /status
    status_check_count = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
if __name__ == "__main__":
    main()
                        
