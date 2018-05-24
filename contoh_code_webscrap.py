UMS_Forlap_link = 'https://forlap.ristekdikti.go.id/perguruantinggi/detail/NkQxMjQxNDItRTc5OC00RjYyLTg3NEItQ0U0MzVCNTQwOUYx'


from bs4 import BeautifulSoup as bs
import urllib3
L = urllib3.PoolManager()
html = L.request('GET', UMS_Forlap_link)

if html.status == 200:
	
	ums_html = bs(html.data, 'html.parser')
	# cetak dokumen HTML di layar
	print( ums_html.prettify() )
	
	T1 = ums_html.select('table')[0]
	nama_pt = T1.select('tr')[1].select('td')[2]
	print ("OUTPUT=================")
	# cetak nama pt di layar
	print (nama_pt.string)
