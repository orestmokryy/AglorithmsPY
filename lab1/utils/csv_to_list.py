from model.printer import Printer
import csv


def csv_to_list():
    final_list = []
    with open('utils/printer.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for line in csv_reader:
            final_list.append(Printer(name=str(line[0]),
                                       price_in_UAH=int(line[1]),
                                       speed_in_pages_per_minute=int(line[2])))
    return final_list
