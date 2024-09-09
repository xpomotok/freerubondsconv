import csv
from builtins import str

params = 15  # 14
sep = ";"
endl = "\n"
in_file = "Data/bonds.txt"
out_file = "Data/bonds.csv"

headict = {
    "title": "Наименование",
    "sector": "Сектор",
    "isin": "ISIN", "listing": "Листинг", "redemption_date": "Дата погашения",
    "de": "ДЭ%", "duration": "Дюрация лет", "price": "Цена %", "coupon_type": "Тип купона",
    "coupon_percent": "Ставка купона %", "coupon_total": "Количество купонов",
    "trading_volume": "Объём торгов", "security": "Вид обеспечения", "rating1": "Рейтинг 1", "rating2": "Рейтинг 2"
}
dict
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
        return "{};{};{};{};{};{}".format(self.title, self.isin, self.listing, self.redemption_date, self.de, endl)


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


class FileController (object):
	
	def __init__(self):
		pass
		
	def read(self, in_file: str) -> str:
		try:
			f = open(in_file, "r", encoding="UTF-8")
		except FileNotFoundError:
			print("Converter: Input file doesn't exist!")
			return None
		else:
			with f:
				string = f.read()
				return string
	
	def write(self, out_file: str, string: str):
		try:
			with open(out_file, "w") as f:
				f.write(string)
		except PermissionError:
			print("Converter: Couldn't create output file!")


class RawData:
    raw_string_list: list

    def __init__(self, string):

        # TODO следующий вариант с базой для более удобной сортировки и фильтрации
        self.raw_string_list = string.split(endl)

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
        self.header = bond_builder.set_title(headict["title"]) \
                .set_isin(headict["isin"]) \
                .set_listing(headict["listing"]) \
                .set_redemption_date(headict["redemption_date"]) \
                .set_de(headict["de"])\
                .build()

        """ зная, сколько полей на одну запись, делаем в выходном файле новую строку """
        for i in range(0, len(raw_string_list), params):
            raw_slice = raw_string_list[i:i + params]

            bond = bond_builder.set_title(raw_slice[0]) \
                .set_isin(raw_slice[2]) \
                .set_listing(raw_slice[3]) \
                .set_redemption_date(raw_slice[4]) \
                .set_de(raw_slice[5])\
                .build()

            print(bond)
            self.bonds.append(bond)
            self.records += 1

    def get_bonds(self) -> list[Bond]:
        return self.bonds

    def get_strings(self) -> list[str]:
        s = []
        for b in self.bonds:
            s.append(str(b))
        return s

    def get_header(self) -> str:
        return str(self.header)


if __name__ == "__main__":

    fc = FileController()

    raw_bonds = RawData(fc.read(in_file))

    if raw_bonds is not None:
        csv_bonds = CsvData(raw_bonds.get_data(), params)
        #csv - class
        out_string = csv_bonds.get_header()

        fc.write(out_file, out_string + "".join(csv_bonds.get_strings()))

        print("Converter: done converting")