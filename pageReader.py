import requests, bs4, os, sys
def page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
	res = requests.get(url,headers = headers)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	return soup

def mangaElement(soup, sell):
	mangaElem = soup.select(sell)
	return mangaElem
	
	
def selector(mangaElem, term):
	if mangaElem == []:
		print('%s named manga doesn\'nt exists. Check it\'s spelling or try it\'s alternate name.'%(term))
		sys.exit(1)
	else:
		mangaUrl = mangaElem[0].get('href')
		print("5% completed.")
		return(mangaUrl)

def selected(mangaElem2, c):
	counter = 0
	ch = ''
	for chap in mangaElem2:
		if(("Chapter "+c[counter]+" " in chap.getText()+" ") or ("chapter "+c[counter]+" " in chap.getText()+" ") or ("Chapter "+c[counter]+":" in chap.getText()+" ") or ("chapter "+c[counter]+":" in chap.getText()+" ")):
			ch = chap
			break
	if(ch == ''):
		print("Chapter No %s has not been released yet. Have patience. Just like One Piece fans have."%(c[0]))
		sys.exit(1)
	print(ch.getText())
	return ch
	
	
def imag(mangaElem4, term, c):
	for pages in mangaElem4:
		manga = pages.get('src')
		print('Downloading image %s...' % (manga))
		rested = requests.get(manga)
		rested.raise_for_status()
		os.makedirs("Chapter " + c[0], exist_ok=True)    # store mangas in ./term
		#print(os.path.join( term, os.path.basename(manga)))
		imageFile = open(os.path.join( "Chapter " + c[0], os.path.basename(manga)), 'wb')
		for chunk in rested.iter_content(100000):
			#print(manga)
			imageFile.write(chunk)
		imageFile.close()
