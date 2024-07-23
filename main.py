import requests
import selectorlib
import smtplib
import ssl
import os
import time

from datetime import datetime

URL = 'https://programmer100.pythonanywhere.com/'


def scrape(url):
    """Scrape the pagr source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

# If you want to send email remove the "#" sign below
# def send_email(message):
    #  host = "smtp.gmail.com"
    # port = 465
    # username = "rishil13123@gmail.com"
    # password = "lkiwaktwxjxutjom"
    # receiver = "rishils162@gmail.com"
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL(host, port, context=context) as server:
    # server.login(username, password)
    # server.sendmail(username, receiver, message)
    # print("Email was sent!")


def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", 'a') as file:
        line = f"{now}, {extracted}"
        file.write(line + "\n")


# can be used along with send email so that the file name is not repeated in data.txt while searching for tours
# def read(extracted):
    # with open("data.txt", 'r') as file:
    #   return file.read()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        # content = read(extracted)
        # if extracted != "No upcoming tours":
        #   if extracted not in content:
        #       store(extracted)
        #       send_email(message="Hey, New event was found!")
        time.sleep(2)
