import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.korcham.net/nCham/Service/EconBrief/appl/ProspectBoardList.asp"

all_data = []

for page_number in range(1, 171):  
    
    url = f"{base_url}?board_type=1&pageno={page_number}&daybt=OldNow&m_OldDate=20130509&m_NowDate=20230904"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table")

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        all_data.append(row_data)

df = pd.DataFrame(all_data)

print(df)