import json
import operator
from pathlib import Path

from settings import AMT_OPERATIONS
from src.classes import Operation


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


def create_short_list(operations: list[dict]) -> list[dict]:
    """
    функция укорачивает список до заданного количества элементов
    :param operations: list[dict]
    :return: укороченный list[dict]
    """
    slice_list = slice(AMT_OPERATIONS)
    return operations[slice_list]


def get_operations_instances(operations: list[dict]) -> list[Operation]:
    """
    Создает экземпляр класса из списка со словарями
    :param operations: list[dict]
    :return: Список с экземплярами класса Operation
    """
    operations_instances = []
    for operation in operations:
        operations_instance = Operation(
            date=operation["date"],
            amount=operation["operationAmount"]["amount"],
            currency_name=operation["operationAmount"]["currency"]["name"],
            description=operation["description"],
            from_=operation.get("from"),
            to=operation["to"]
        )
        operations_instances.append(operations_instance)
    return operations_instances
