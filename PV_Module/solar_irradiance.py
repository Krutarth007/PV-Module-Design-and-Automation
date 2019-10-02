import urllib.request
from bs4 import BeautifulSoup
la = 28.7041
lo = 77.1025

url_path = 'https://eosweb.larc.nasa.gov/cgi-bin/sse/retscreen.cgi?email=rets%40nrcan.gc.ca&step=2&lat={}&lon={}&submit=Submit'.format(la,lo)

response = urllib.request.urlopen(url_path)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
cnt = -1


info = list(soup.children)[2]
info = str(info).split("\n")
data = 0
for i in info:
	if i == '<td align="left"><b>  <br/>Annual</b></td>':
		cnt = 0
	if cnt >= 0:
		cnt =  cnt + 1
	if cnt == 4:
		data = i.split("<hr/>")[1].split("<")[0]
		break

data = float(data.strip())
print (data)

