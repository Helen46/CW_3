from _datetime import datetime


class Operation:

    def __init__(
            self,
            date: str,
            amount: str,
            currency_name: str,
            from_: str | None,
            description: str,
            to: str
    ):
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.from_ = from_ if from_ is not None else ""
        self.description = description
        self.to = to

    def convert_date(self):
        """
        преобразует str в date
        :return: str в заданом формате date
        """
        the_date = datetime.fromisoformat(self.date)
        return the_date.strftime("%d.%m.%Y")

    def mask_payment_info(self, payment_info: str):
        """
        маскирует часть str
        :param payment_info: строка с номером карты или счета
        :return: строка с замаскироваными данными
        """
        info: list[str] = payment_info.split(" ")
        num_card = info.pop(-1)
        if payment_info == "":
            mask_card = ""
        elif payment_info.startswith("Счет"):
            mask_card = "**" + num_card[-4:]
        else:
            mask_card = (f"{num_card[0:4]} {num_card[4:6]}** "
                         f"**** {num_card[-4:]}")
        info.append(mask_card)
        return " ".join(info)

    def __str__(self):
        from_ = self.mask_payment_info(self.from_)
        to_ = self.mask_payment_info(self.to)
        pointer = " -> " if from_ else ""
        return (
            f"{self.convert_date()} {self.description}\n"
            f"{from_}{pointer}{to_}\n"
            f"{self.amount} {self.currency_name}\n"
        )
