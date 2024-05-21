from src.utils import create_filtered_list, create_sorted_list, create_short_list


def test_create_filtered_list(initial_list, filtered_list):
    assert create_filtered_list(initial_list) == filtered_list


def test_create_sorted_list(filtered_list, sorted_list):
    assert create_sorted_list(filtered_list) == sorted_list


def test_create_short_list(sorted_list, short_list):
    assert create_short_list(sorted_list) == short_list
