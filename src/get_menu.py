import requests
import bs4


def get_site_data(url):
    req = requests.get(url)

    return req.text


def parse_html(text):
    soup = bs4.BeautifulSoup(text, "lxml")
    day = soup.find("p").text
    menu_text = soup.find("figure", {"class": "wp-block-table"}).text

    breakfast = "-" + menu_text.rsplit("ALMOÇO")[0].rsplit("MANHÃ")[1].replace("  ", "\n-").rstrip("-")
    lunch = "-" + menu_text.rsplit("JANTAR")[0].rsplit("ALMOÇO")[1].replace("  ", "\n-").rstrip(" ").rstrip("-")
    dinner = "-" + menu_text.rsplit("JANTAR")[1].replace("  ", "\n-").rstrip("-")

    return {"day": day, "breakfast": breakfast, "lunch": lunch, "dinner": dinner}


def generate_menu():

    url = "https://pra.ufpr.br/ru/ru-centro-politecnico/"

    text = get_site_data(url)
    data = parse_html(text)

    with open("daily_menu.txt", "w") as file:
        file.write(data["day"])
        file.write("\n")
        file.write("\n")
        file.write("Café da Manhã")
        file.write("\n")
        file.write(data["breakfast"])
        file.write("\n")
        file.write("\n")
        file.write("Almoço")
        file.write("\n")
        file.write(data["lunch"])
        file.write("\n")
        file.write("\n")
        file.write("Janta")
        file.write("\n")
        file.write(data["dinner"])

