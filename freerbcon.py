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


# @dataclass
class Bond():
    # title: str
    # sector: str
    # isin: str
    # listing: str
    # redemtion_date: str
    # de: str
    # duration: float
    # price: str #float
    # coupon_type: str
    # coupon_percent: float
    # coupon_total: int
    # trading_volume: float
    # security: str
    # rating1: any
    # rating2: any

    def __init__(self, bond_builder):
        self.title = builder.title
        self.sector= builder.sector
        self.isin = builder.isin
        self.listing= builder.listing
        self.redemtion_date= builder.redemption_date
        self.de= builder.de
        self.duration= builder.duration
        self.price= builder.price
        self.coupon_type= builder.coupon_type
        self.coupon_percent= builder.coupon_percent
        self.coupon_total= builder.coupon_total
        self.trading_volume= builder.trading_volume
        self.security= builder.security
        self.rating1= builder.rating1
        self.rating2= builder.rating2

    def __str__(self):
        return "{} {}".format(self.title, self.isin)

class BondBuilder():
    def __init__(self):
        self.title = ""
        self.isin = ""
        self.sector = ""
        self.listing = ""
        self.redemtion_date = ""
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

    def build(self) -> Bond:

        return Bond(self);

james: Bond

builder = BondBuilder()
james = builder.set_isin("Hello").set_title("World").build()
print(james)

def form_record(strings) -> str:
    out_string = sep.join(strings)
    out_string = "".join([out_string, endl])
    out_string = out_string.replace(".", ",")
    return out_string


def convert():
    try:
        f = open(in_file, "r", encoding="UTF-8")
    except FileNotFoundError:
        print("Converter: Input file doesn't exist!")
        return
    else:
        with f:
            string = f.read()

    # TODO следующий вариант с базой для более удобной сортировки и фильтрации
    raw_string_list = string.split(endl)

    if len(raw_string_list) % params != 0:
        print("Converter: Raw data is unaligned!")
        return

    # bonds = []

    # for i in range(0, len(raw_string_list), params):
    # 	bond = Bond(raw_string_list[i:params])
    # 	bonds.append(bond)
    # 	print(bond)

    try:
        with open(out_file, "w") as f:

            f.write(form_record(header))
            cnt = 0
            bonds = []
            """ зная, сколько полей на одну запись, делаем в выходном файле новую строку """
            for i in range(0, len(raw_string_list), params):
                slice = raw_string_list[i:i + params]
                # bond = Bond(title=slice[0], sector=slice[1], isin=slice[2],
                #             listing=slice[3],
                #             redemtion_date=slice[4],
                #             de=slice[5],
                #             duration=float(slice[6]),
                #             price=slice[7], #float(slice[7]),
                #             coupon_type=slice[8],
                #             coupon_percent=float(slice[9]),
                #             coupon_total=int(slice[10]),
                #             trading_volume=float(slice[11].replace(" ", "")),
                #             security=slice[12],
                #             rating1=slice[13],
                #             rating2=slice[14]
                #             )
                # bonds.append(bond)
                f.write(form_record(raw_string_list[i:i + params]))
                cnt += 1

        print("Converter: {} records have been written!".format(cnt))
        print(bonds)

    except PermissionError:
        print("Converter: Couldn't create output file!")


if __name__ == "__main__":
    convert()
