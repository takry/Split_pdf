# -*- coding: utf-8 -*-
import fitz
from PyPDF2 import PdfReader, PdfWriter
import argparse
import os

""" lllllllllllllllllllllllllllllllllllllililllllll]lllllllllllllllllllll 4
l il!lш llш |lпl ll!l i ll lll Illl| illll lшll lllll llll l ll lll lllll ll|l llll\n 1
lllIllIl|lll|lllllllllllllllllllllllllllllllllllllllllllllllшllllllll\n 3
l lillш lllll lllil llll l ll lll llllI lllll lllll lllll llll l ll !ll lllll llll lll 5
l lillш lllll llll| llll l |l lll lllll lllll |l|ll lllll |lll l ll |ш lllIl llll llll 6
l llllш illш illfi ilIl l ll lil lllll lllll llшl lllll llll l lI lll lllш llll llll 7
nllllll !|lll lllll llll l ll lll lllll lllll lllll lllll llll l ll lll lllш illl llll 8
i llilш lllш lllll llll l ll lll lllll Illll lllll lllll шll шl lll ilшл llil llll 9
lllllшlllllllIlIllllllllllllllllllllllllllllllllllllIllllllllllllllll 11
l l!!ifi lllш liп| llll l ll lll lllll lшll llшl lllш llll i ll lll lllil llll пll 12 
       """
img_rg_1 = 'шll'
img_rg_2 = 'llll'
name_fonts = "ABCDEE+IDAutomationHC39M"
delimiter = ','

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f')
args = parser.parse_args()

pdf_document = args.f


def start(pdf_document):
    dir = os.path.dirname(os.path.abspath(pdf_document))

    doc = fitz.open(pdf_document)
    pdf = PdfReader(pdf_document)

    print(f"number of pages: {doc.page_count}")
    pages_ = []
    q = 0
    for page in range(doc.page_count):
        q=q+1
        a = doc.load_page(page).get_fonts()
        b = doc.load_page(page).get_text_blocks()
 
        for i in b:
            if delimiter.join([str(value) for value in i]).find(img_rg_1) != -1 or delimiter.join([str(value) for value in i]).find(img_rg_2) != -1:
                pages_.append(page)

        if [item for item in a if name_fonts in item]:
            pages_.append(page)

    pages_.append(doc.page_count)
    for i in range(len(pages_)-1):
        pdf_writer = PdfWriter()
        for page in range(pages_[i], pages_[i+1]):

            pdf_writer.add_page(pdf.pages[page])
        outputFilename = f"{dir}\example-page-{page+1}.pdf"
        with open(outputFilename, "wb") as out:
            pdf_writer.write(out)
            print("created", outputFilename)


start(pdf_document)
