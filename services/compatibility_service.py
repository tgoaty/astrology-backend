import json
import requests
from bs4 import BeautifulSoup
from models import CompatibilityData


def get_compatibility_info(data: CompatibilityData):
    url = (f"https://gadalkindom.ru/sovmestimost/po_date_rozhdeniya.html"
           f"?f_day={data.f_day}"
           f"&f_month={data.f_month}"
           f"&f_year={data.f_year}"
           f"&m_day={data.m_day}"
           f"&m_month={data.f_month}"
           f"&m_year={data.m_year}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    chakra = soup.find("div", class_="sovmes-wrapper")
    for img in chakra.find_all('img'):
        img.decompose()
    result = {"title": chakra.find("h2").text.replace("\xa0", " ")}

    chakra_table = chakra.find('tbody')
    rows = chakra_table.find_all('tr')[2:]
    arr = []
    for row in rows:
        first_col, second_col = row.find_all('td')
        new_first_col = first_col.text[0]
        for i in range(1, len(first_col.text)):
            char = first_col.text[i]
            if char == char.upper() and first_col.text[i - 1] == first_col.text[i - 1].lower() and char.isalpha() and \
                    first_col.text[i - 1].isalpha():
                new_first_col = new_first_col + ' ' + char
            else:
                new_first_col = new_first_col + char

        first = new_first_col.replace("\xa0", " ")
        second = second_col.text.replace("\xa0", " ").replace("«", " «")
        arr.append([[" ".join(first.split(' ')[:5]), " ".join(first.split(' ')[5:])],
                    [" ".join(second.split(' ')[:4]), " ".join(second.split(' ')[4:])]])
    result["chakra"] = arr

    chakra_description = soup.find("section").find_all("div")[23]
    chakra_description_b = chakra_description.find_all("b")
    chakra_description_span = chakra_description.find_all("span")
    chakra_description_text = [{"title": chakra_description_b[i].text, "text": chakra_description_span[i].text} for i in
                               range(len(chakra_description_b))]
    result["chakraDescription"] = chakra_description_text

    return json.loads(json.dumps(result, ensure_ascii=False))
