import json
import operator
from pathlib import Path

from settings import AMT_OPERATIONS


def load_data(path: Path) -> list[dict]:
    """
    Загружает файл в формате json
    :param path: Path
    :return: Информацию из файла
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def create_filtered_list(operations: list[dict]) -> list[dict]:
    """
    фильтрует список по заданому парамеру
    :param operations: list[dict]
    :return: отфильтрованый list[dict]
    """

    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]


def create_sorted_list(operations: list[dict]) -> list[dict]:
    """
    Функция сортирует список по заданому параметру
    :param operations: list[dict]
    :return: отсортированный list[dict]
    """
    return sorted(
        operations, key=operator.itemgetter("date"),
        reverse=True
    )
    # filtered_list, key=lambda x: x.get("date")


def create_short_list(operations: list[dict]) -> list[dict]:
    """
    функция укорачивает список до заданного количества элементов
    :param operations: list[dict]
    :return: укороченный list[dict]
    """
    slice_list = slice(AMT_OPERATIONS)
    return operations[slice_list]
