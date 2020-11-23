import pyttsx3
import PyPDF2

file = input('Which pdf do you want to read?')
if len(file) < 1: file = "whichever pdf you want to default to.pdf"
pdf = open(file,'rb')

#Finds and tracks the # of pages
pdfReader = PyPDF2.PdfFileReader(pdf)
pages = pdfReader.numPages
print(pages)
print(pdfReader.isEncrypted)
#Speaks the contents of the pdf
reader = pyttsx3.init()
page = int(input("Enter the page you want to start from:"))
stopPage = int(input("Enter the page you want to stop on:"))
for num in range(page, stopPage):
    pageRead = pdfReader.getPage(num)
    if len(pageRead) > pages:
        print("The page(s) that you have requested does not exist")
        exit()
    content = pageRead.extractText()
    print(content)
    reader.say(content)
    reader.runAndWait()
