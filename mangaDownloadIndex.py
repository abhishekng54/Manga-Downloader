import pyperclip, sys, pageReader, pdfConverter

if len(sys.argv) > 1:
	term = ' '.join(sys.argv[1:])
else:
	term = pyperclip.paste()

cha = input("And the chapter?")
c = cha.split()


url = 'http://mangakakalot.com/search/' + "_".join(term.split())               # starting url

#print(url)
sell2 = '.item-name a'

soup2 = pageReader.page(url)
mangaElem2 = pageReader.mangaElement(soup2, sell2)
url2 = pageReader.selector(mangaElem2, term)

sell3 = '.manga-info-chapter .chapter-list .row a'
soup3 = pageReader.page(url2)
mangaElem3 = pageReader.mangaElement(soup3, sell3 )
ch = pageReader.selected(mangaElem3, c)
#print(url3)

soup4 = pageReader.page(ch.attrs.get('href'))
mangaElem4 = pageReader.mangaElement(soup4, '#vungdoc img')
pageReader.imag(mangaElem4, term, c)
pdfConverter.pdfMaker(term, c)