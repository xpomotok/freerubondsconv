from dataclasses import dataclass
from builtins import str


params = 15 #14
sep = ";"
endl = "\n"
in_file = "Data/2024-08-bonds.txt"
out_file = "Data/280824.csv"
header = ["Наименование", "Сектор",  "ISIN", "Листинг", "Дата погашения",
 	"ДЭ%", "Дюрация лет", "Цена %", "Тип купона", "Ставка купона %", "Количество купонов",
    "Объём торгов", "Вид обеспечения", "Рейтинг 1", "Рейтинг 2"]


@dataclass
class Bond():
	title: str
	sector: str
	isin: str
	listing: str
	redemtion_date: str
	de: float
	duration: float
	price: float
	coupon_type: str
	coupon_percent: float
	coupon_total: int
	trading_volume: float
	security: str
	rating1: str
	rating2: str


def form_record(strings) -> str:
	out_string = sep.join(strings)
	out_string = "".join([out_string, endl])
	out_string = out_string.replace(".",",")
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
			""" зная, сколько полей на одну запись, делаем в выходном файле новую строку """
			for i in range(0, len(raw_string_list), params):
				f.write(form_record(raw_string_list[i:i+params]))
				
		print("Converter: All records have been written!")

	except PermissionError:
		print("Converter: Couldn't create output file!")


if __name__ == "__main__":
	convert()
