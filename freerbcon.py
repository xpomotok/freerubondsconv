# from dataclasses import dataclass
from builtins import str

params = 15  # 14
sep = ";"
endl = "\n"
in_file = "Data/2024-08-bonds.txt"
out_file = "Data/280824.csv"
header = ["Наименование", "Сектор", "ISIN", "Листинг", "Дата погашения",
          "ДЭ%", "Дюрация лет", "Цена %", "Тип купона", "Ставка купона %", "Количество купонов",
          "Объём торгов", "Вид обеспечения", "Рейтинг 1", "Рейтинг 2"]


class RawData:
    raw_string_list: list

    def __init__(self):
        self.string = ""

    def populate(self, in_file: str):
        try:
            f = open(in_file, "r", encoding="UTF-8")
        except FileNotFoundError:
            print("Converter: Input file doesn't exist!")
            return
        else:
            with f:
                self.string = f.read()

    def split(self):
        # TODO следующий вариант с базой для более удобной сортировки и фильтрации
        self.raw_string_list = self.string.split(endl)

        if len(self.raw_string_list) % params != 0:
            print("Converter: Raw data is unaligned!")
            return

    def get_data(self) -> list:
        return self.raw_string_list


class CsvData:

    def __init__(self, raw_string_list: list, params: int) -> None:
        self.records = 0
        self.bonds = []
        bond_builder = BondBuilder()

        """ зная, сколько полей на одну запись, делаем в выходном файле новую строку """
        for i in range(0, len(raw_string_list), params):
            raw_slice = raw_string_list[i:i + params]
            bond = bond_builder.set_title(raw_slice[0]) \
                .set_isin(raw_slice[1]) \
                .set_listing(raw_slice[2]) \
                .set_redemption_date(raw_slice[3]) \
                .set_de(raw_slice[4]).build()

            print(bond)
            self.bonds.append(bond)
            self.records += 1

    def get_bonds(self) -> list:
        return self.bonds

    def export(self, out_file: str, header: list):
        try:
            with open(out_file, "w") as f:
                f.write(form_record(header))
                for b in self.bonds:
                    f.write(str(b))

                # for i in range(0, len(raw_string_list), params):
                #     f.write(form_record(raw_string_list[i:i + params]))
                #     cnt += 1

            print("Converter: {} records have been written!".format(self.records))
            print(self.bonds)

        except PermissionError:
            print("Converter: Couldn't create output file!")


# @dataclass
class Bond:

    def __init__(self, builder):
        self.title = builder.title
        self.sector = builder.sector
        self.isin = builder.isin
        self.listing = builder.listing
        self.redemption_date = builder.redemption_date
        self.de = builder.de
        self.duration = builder.duration
        self.price = builder.price
        self.coupon_type = builder.coupon_type
        self.coupon_percent = builder.coupon_percent
        self.coupon_total = builder.coupon_total
        self.trading_volume = builder.trading_volume
        self.security = builder.security
        self.rating1 = builder.rating1
        self.rating2 = builder.rating2

    def __str__(self):
        return "{};{};{};{};{}{}".format(self.title, self.isin, self.listing, self.redemption_date, self.de, endl)


class BondBuilder:
    def __init__(self):
        self.title = ""
        self.isin = ""
        self.sector = ""
        self.listing = ""
        self.redemption_date = ""
        self.de = ""
        self.duration = ""
        self.price = "" #float
        self.coupon_type = ""
        self.coupon_percent = 0.0
        self.coupon_total = 0
        self.trading_volume = 0.0
        self.security = ""
        self.rating1 = ""
        self.rating2 = ""

    def set_title(self, title):
        self.title = title
        return self

    def set_isin(self, isin):
        self.isin = isin
        return self

    def set_listing(self, listing):
        self.listing = listing
        return self

    def set_redemption_date(self, redemption_date):
        self.redemption_date = redemption_date
        return self

    def set_de(self, de):
        self.de = de
        return self

    def build(self) -> Bond:

        return Bond(self)


def form_record(strings) -> str:
    out_string = sep.join(strings)
    out_string = "".join([out_string, endl])
    out_string = out_string.replace(".", ",")
    return out_string


if __name__ == "__main__":
    raw_bonds = RawData()
    raw_bonds.populate(in_file)
    raw_bonds.split()

    if raw_bonds is not None:
        csv_bonds = CsvData(raw_bonds.get_data(), params)
        print(csv_bonds.get_bonds())
