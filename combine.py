import pypdf

os.listdir()

wr = pypdf.PdfWriter()

files = ['handout-20230115.pdf', 'handout-20230115-2.pdf']

for f in files:
  with open(f, 'rb') as file:
    pr = pypdf.PdfReader(file)
    page = pr.pages[0]
    wr.add_page(page)

pdfOut = open('tmp.pdf', 'wb')
wr.write(pdfOut)
pdfOut.close()
