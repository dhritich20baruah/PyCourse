import PyPDF2
a = PyPDF2.PdfFileReader('ibpsPOmain.pdf')
str = ""
for i in range(1,25):
    str += a.getPage(i).extractText()

with open("rrbclerk.doc", "w", encoding="utf-8") as f:
    f.write(str)