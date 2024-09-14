#!/usr/bin/env python3
"""0-simple_helper"""


def index_range(page, page_size):
    """ Returns a tuple of size two containing a start and
        end index matching the range
        of indexes to return a list for those
        pagination parameters.
    """
    if (page == 1):
        return (0, page_size)
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
