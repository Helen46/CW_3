from settings import OPERATIONS
from src.utils import load_data, create_filtered_list, create_sorted_list, create_short_list, get_operations_instances


def main():
    """
    функция основоного кода
    :return: None
    """
    operations = load_data(OPERATIONS)
    filtered_operations = create_filtered_list(operations)
    operations = create_sorted_list(filtered_operations)
    sorted_operations = create_short_list(operations)
    show_operations = get_operations_instances(sorted_operations)
    for operation in show_operations:
        print(operation)


if __name__ == "__main__":
    main()
