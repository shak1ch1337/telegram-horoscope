import requests
from bs4 import BeautifulSoup
from data.database.db_requests import get_all_signs, update_sign_content
from time import sleep


async def parsing():
    signs = await get_all_signs()
    for sign in signs:
        url = f"https://horo.mail.ru/prediction/{sign[2]}/today/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        scrap_content = soup.findAll("div", class_ = "b6a5d4949c e45a4c1552")
        format_content = ""
        for content in scrap_content:
            format_content += f"\n{content.text}"
        await update_sign_content(sign[0], format_content)
        sleep(1)
    return True