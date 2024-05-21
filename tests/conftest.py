import pytest

from src.classes import Operation


@pytest.fixture
def initial_list():
    return [
        {
            "state": "EXECUTED",
            "date": "2023-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2022-07-03T18:35:29.512364",
        },
        {
            "state": "CANCELED",
            "date": "2021-06-30T02:08:58.425572",
        },
        {
            "state": "EXECUTED",
            "date": "2021-03-23T10:45:06.972075",
        },
        {},
        {
            "state": "EXECUTED",
            "date": "2020-04-04T23:20:05.206878",
        },
        {
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
        },
        {
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
        },
        {
            "state": "EXECUTED",
            "date": "2024-07-12T20:41:47.882230",
        }
    ]


@pytest.fixture
def filtered_list():
    return [
        {
            "state": "EXECUTED",
            "date": "2023-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2022-07-03T18:35:29.512364",
        },
        {
            "state": "EXECUTED",
            "date": "2021-03-23T10:45:06.972075",
        },
        {
            "state": "EXECUTED",
            "date": "2020-04-04T23:20:05.206878",
        },
        {
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
        },
        {
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
        },
        {
            "state": "EXECUTED",
            "date": "2024-07-12T20:41:47.882230",
        }
    ]


@pytest.fixture
def sorted_list():
    return [
        {
            "state": "EXECUTED",
            "date": "2024-07-12T20:41:47.882230",
        },
        {
            "state": "EXECUTED",
            "date": "2023-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2022-07-03T18:35:29.512364",
        },
        {
            "state": "EXECUTED",
            "date": "2021-03-23T10:45:06.972075",
        },
        {
            "state": "EXECUTED",
            "date": "2020-04-04T23:20:05.206878",
        },
        {
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
        },
        {
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
        }
    ]


@pytest.fixture
def short_list():
    return [
        {
            "state": "EXECUTED",
            "date": "2024-07-12T20:41:47.882230",
        },
        {
            "state": "EXECUTED",
            "date": "2023-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2022-07-03T18:35:29.512364",
        },
        {
            "state": "EXECUTED",
            "date": "2021-03-23T10:45:06.972075",
        },
        {
            "state": "EXECUTED",
            "date": "2020-04-04T23:20:05.206878",
        }
    ]


@pytest.fixture
def operation():
    return Operation(
            date="2019-08-26T10:50:58.294041",
            amount="31957.58",
            currency_name="руб.",
            description="Перевод организации",
            from_=None,
            to="Счет 64686473678894779589"
    )


@pytest.fixture
def operations():
    return [
        Operation(
            date="2019-08-26T10:50:58.294041",
            amount="31957.58",
            currency_name="руб.",
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589"
        ),
        Operation(
            date="2018-07-11T02:26:18.671407",
            amount="79931.03",
            currency_name="руб.",
            description="Открытие вклада",
            from_=None,
            to="Счет 72082042523231456215"
        ),
        Operation(
            date="2018-11-29T07:18:23.941293",
            amount="3348.98",
            currency_name="USD",
            description="Перевод с карты на карту",
            from_="MasterCard 3152479541115065",
            to="Visa Gold 9447344650495960"
        )

    ]