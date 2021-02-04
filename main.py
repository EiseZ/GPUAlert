import time
import requests
from bs4 import BeautifulSoup
import smtplib, ssl

port = 465
password = input("Type your password and press enter: ")

context = ssl.create_default_context()

URLs = ["https://megekko.nl/product/1963/1129229/Nvidia-Videokaarten/ASUS-Dual-RTX3060TI-8G-MINI-NVIDIA-GeForce-RTX-3060-Ti-8-GB-GDDR6-Videokaart", "https://megekko.nl/product/1963/1129230/Nvidia-Videokaarten/ASUS-Dual-RTX3060TI-O8G-MINI-NVIDIA-GeForce-RTX-3060-Ti-8-GB-GDDR6-Videokaart", "https://megekko.nl/product/1963/296051/Nvidia-Videokaarten/Asus-GeForce-RTX-3060-Ti-DUAL-RTX3060TI-8G-Videokaart", "https://megekko.nl/product/1963/296069/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3060-Ti-AORUS-MASTER-8G-Videokaart", "https://megekko.nl/product/1963/295477/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3070-AORUS-MASTER-8G-Videokaart", "https://megekko.nl/product/1963/296915/Nvidia-Videokaarten/MSI-GeForce-RTX-3060-Ti-GAMING-X-TRIO-Videokaart", "https://megekko.nl/product/1963/296073/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3060-Ti-EAGLE-8G-Videokaart", "https://megekko.nl/product/1963/296072/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3060-Ti-EAGLE-OC-8G-Videokaart", "https://megekko.nl/product/1963/296050/Nvidia-Videokaarten/Asus-GeForce-RTX-3060-Ti-DUAL-RTX3060TI-O8G-Videokaart", "https://megekko.nl/product/1963/296071/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3060-Ti-GAMING-OC-8G-Videokaart", "https://megekko.nl/product/1963/296917/Nvidia-Videokaarten/MSI-GeForce-RTX-3060-Ti-VENTUS-3X-OC-Videokaart", "https://megekko.nl/product/1963/296070/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3060-Ti-GAMING-OC-PRO-8G-Videokaart", "https://megekko.nl/product/1963/297540/Nvidia-Videokaarten/MSI-GeForce-RTX-3060-Ti-VENTUS-2X-OCV1-Videokaart", "https://megekko.nl/product/1963/293967/Nvidia-Videokaarten/Gigabyte-GeForce-RTX-3070-GAMING-OC-8G-Videokaart"]

while True:
    for URL in URLs:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        print(soup.find_all("div", class_="pricecontainer"))
        if "PRIJS IS NOG NIET BEKEND" in soup.find_all("div", class_="pricecontainer").__str__():
            print("Niet op voorraad")
        else:
            print(URL.__str__() + "IS OP VOORRAAD!")
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("eiscomania@gmail.com", password)
                server.sendmail("eiscomania@gmail.com", "eise.zimmerman@outlook.com", URL.__str__() + "IS OP VOORRAAD!!!")
            URLs.pop(URLs.index(URL))
    time.sleep(10)