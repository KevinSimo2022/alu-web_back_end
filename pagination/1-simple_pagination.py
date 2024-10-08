#!/usr/bin/env python3
"""1-simple_pagination"""

import csv
from typing import List


def index_range(page, page_size):
    """ returns a tuple of size two containing a start and
        end index corresponding to the range
        of indexes to return in a list for those
        pagination parameters.
    """
    if (page == 1):
        return (0, page_size)
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """A Server class paginates a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """A cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets the page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        page_info = index_range(page=page, page_size=page_size)
        data = self.dataset()
        if page_info[1] > len(data):
            return []
        return data[page_info[0]:page_info[1]]
