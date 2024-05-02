def index_range(page, page_size):
    """
    Calculate the start and end index for pagination.

    Parameters:
    page (int): The current page number (1-indexed).
    page_size (int): The number of items each page contains.

    Returns:
    tuple: A tuple containing the start index and end index for the items to be displayed on the page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

# Example usage:
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
