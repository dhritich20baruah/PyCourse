import PyPDF2
a = PyPDF2.PdfFileReader('rrbclerk.pdf')
str = ""
for i in range(1,50):
    str += a.getPage(i).extractText()

with open("rrbclerk.doc", "w", encoding="utf-8") as f:
    f.write(str)