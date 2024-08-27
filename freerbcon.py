# from Queue import Queue
from builtins import str

params = 14
sep = ";"
endl = "\n"
in_file = "rusbonds.txt"
out_file = "rbondsconv.csv"

header = ["Наименование", "Статус", "Дата погашения", "Дата окончания размещения",
          "ДЭ%", "Объём эмиссии", "Ставка купона%", "Листинг Мос.биржи", "Сектор эмитента",
          "Эмитент", "Дюрация лет", "Цена %", "К-во купонов в год", "Объём торгов"]


def form_header(header_list) -> str:
	head = sep.join(header_list)
	head = "".join([head, endl])
	return head


def form_record(string) -> str:
	out_string = string.replace(".", ",")
	out_string = "".join([out_string, sep])
	return out_string


def convert():
	# writeQueue = Queue()

	try:
		with open(in_file, "r", encoding="UTF-8") as f:
			string = f.read()

			# TODO следующий вариант с базой для более удобной сортировки и фильтрации
			image = string.split(endl)
	except FileNotFoundError:
		print("Converter: Input file doesn't exist!")
		return

	try:
		with open(out_file, "w") as f:
			cnt = 0

			f.write(form_header(header))
			""" зная, сколько полей на одну запись, делаем в выходном файле новую строку """
			for i in image:
				f.write(form_record(i))
				cnt += 1
				if cnt == params:
					cnt = 0
					f.write(endl)
		print("Converter: All records have been written!")
	except FileNotFoundError:
		print("Converter: Couldn't create output file!")


if __name__ == "__main__":
	convert()
