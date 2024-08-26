# from Queue import Queue

params = 14
sep = ";"
in_file = "rusbonds.txt"
out_file = "rbondsconv.csv"

header = ["Наименование","Статус", "Дата погашения", "Дата окончания размещения",
 "ДЭ%", "Объём эмиссии", "Ставка купона%", "Листинг Мос.биржи", "Сектор эмитента",
  "Эмитент", "Дюрация лет", "Цена %", "К-во купонов в год", "Объём торгов"]


def convert():

	image = []
	# writeQueue = Queue()

	try:
		with open(in_file, "r", encoding="UTF-8") as f:
			string = f.read()

			image = string.split("\n")
			try:
				with open(out_file, "w") as f:
					cnt = 0

					for h in header:
						f.write(h)
						f.write(sep)

					f.write("\n")

					for i in image:
						i = i.replace(".", ",")
						f.write(i)
						f.write(sep)

						cnt += 1
						if cnt == params:
							cnt = 0
							f.write("\n")
				print("Written!")
			except FileNotFoundError:
				print("Converter: Couldn't create output file!")
	except FileNotFoundError:
		print("Converter: Input file doesn't exist!")



if __name__ == "__main__":
	convert()