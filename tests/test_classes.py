def test_operation_init(operation):
    assert operation.from_ == ""


def test_operation_convert_date(operation):
    assert isinstance(operation.convert_date(), str)
    assert operation.convert_date() == "26.08.2019"


def test_operation_str(operation):
    assert str(operation) == ("26.08.2019 Перевод организации\n"
                              "Счет **9589\n"
                              "31957.58 руб.\n")
