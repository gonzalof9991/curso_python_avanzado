import os
import webbrowser

from fpdf import FPDF
from filestack import Client
from flatmates.flat import Bill


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill: Bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate1))
        pdf.add_page()
        # Add Icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)
        pdf.set_font(family="Times", size=14, style='B')
        # Insert Period label and value
        pdf.cell(w=100, h=40, txt='Period: ', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.set_font(family="Times", size=12)
        # Insert name and pay
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and pay
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0)
        # Change directory to files, generate and open PDF
        os.chdir("files")
        # Output PDF
        pdf.output(self.filename)

        # Open PDF in Browser
        webbrowser.open(self.filename)


class FileSharer:
    def __init__(self, filepath, api_key='ADEJVxigJSpabxfbFBoKrz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
