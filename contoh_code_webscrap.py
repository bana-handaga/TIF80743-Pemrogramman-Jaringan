UMS_Forlap_link = 'https://forlap.ristekdikti.go.id/perguruantinggi/detail/NkQxMjQxNDItRTc5OC00RjYyLTg3NEItQ0U0MzVCNTQwOUYx'

from bs4 import BeautifulSoup4 as bs
import urllib3
L = urllib3.PoolManager()
html = L.request('GET', UMS_Forlap_link)

if html.status == 200:
	Ums_html = bs(html.data, 'html.parser')
	print( ums_html.prettify() )
