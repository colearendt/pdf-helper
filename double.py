#!/usr/bin/env python3

import pypdf
import os
import click

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), prompt='Input file', help='The input pdf')
@click.option('--suffix', '-s', default='final', help='The suffix to append to the filename')
def double(file, suffix):
    wr = pypdf.PdfWriter()

    fileName, ext = os.path.splitext(file)

    if ext != '.pdf':
        raise ValueError(f'Must provide a pdf as input. Instead got: {file}')

    outName = f'{fileName}-{suffix}.pdf'

    print(f'Doubling {file}...')
    files = [file, file]
    for f in files:
      with open(f, 'rb') as file:
        pr = pypdf.PdfReader(file)
        page = pr.pages[0]
        wr.add_page(page)

    print(f'Outputting filename: {outName}')
    pdfOut = open(outName, 'wb')
    wr.write(pdfOut)
    pdfOut.close()

if __name__ == '__main__':
    os.listdir()
    double()
