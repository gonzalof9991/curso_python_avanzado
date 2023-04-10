from flatmates.flat import Bill, Flatmate
from flatmates.reports import PdfReport, FileSharer

amount = float(input("Hey user, enter the bill amout: "))
period = input("What is the bill period? E.g December 2020: ")
name1 = input("What is your name?: ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period ?: "))

name2 = input("What is the name of the other flatmate?: ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period ?: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

# Principios de OOP -> responsabilidad unica
file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
