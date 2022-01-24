import pandas
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

url = "https://www.yoigo.com/tarifas-moviles"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
table = soup.find('tbody') # in html table is represented by the tag <table>
ofertas_Movil_data =  pandas.DataFrame(columns=["Datos", "llamas", "precio"])

for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    if (cols != []):
        datos = cols[0].text
        llamadas = cols[1].text
        precio = cols[2].text
        ofertas_Movil_data=ofertas_Movil_data.append({"Datos":datos,"llamas":llamadas,"precio":precio},ignore_index=True)

print(ofertas_Movil_data)
var = '01234567'
print( '1:2,3:4'.split(':'))
mylist = ["apple", "banana", "cherry"]
mylist.sor
