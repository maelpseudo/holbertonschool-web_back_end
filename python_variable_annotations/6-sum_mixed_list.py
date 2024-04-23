#!/usr/bin/env python3
# 6-sum_mixed_list.py
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of all elements in a list containing both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floating point numbers.

    Returns:
    float: The sum of all elements in the list, returned as a float.
    """
    return float(sum(mxd_lst))
