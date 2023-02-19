# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("pdf_name.pdf")

# get number of pages
NumPages = object.getNumPages()
print(NumPages)
# define keyterms
list_of_items = ['122140436021', '122137392000']


print(list_of_items)
# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i))
    Text = PageObj.extractText() 
    # print(Text)
    for item in list_of_items:
        ResSearch = re.search(item, Text)
        if re.search(item, Text):
            print(list_of_items.index(item), item+"   found")
            break
    print(ResSearch)