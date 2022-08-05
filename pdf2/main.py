import PyPDF2
a = PyPDF2.PdfFileReader('ibpsPOmain.pdf')
str = ""
for i in range(1,2):
    str += a.getPage(i).extractText()

with open("text.txt", "w") as f:
    f.write(str)