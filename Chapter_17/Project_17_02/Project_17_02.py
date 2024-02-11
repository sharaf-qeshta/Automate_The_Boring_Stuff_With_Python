"""
Scheduled Web Comic Downloader
Write a program that checks the websites of several web comics and automatically
 downloads the images if the comic was updated since the program’s
  last visit. Your operating system’s scheduler (Scheduled Tasks on
Windows, launchd on macOS, and cron on Linux) can run your Python
program once a day. The Python program itself can download the comic
and then copy it to your desktop so that it is easy to find. This will free you
from having to check the website yourself to see whether it has updated.
(A list of web comics is available at https://nostarch.com/automatestuff2/.)

@author Sharaf Qeshta
"""

from bs4 import *
import requests
import os

FOLDER_NAME = "Images"
URL = "https://nostarch.com/automatestuff2/"


def main():
    # creating the folder
    images_in_folder = os.listdir(FOLDER_NAME)
    try:
        os.mkdir(FOLDER_NAME)
    except FileExistsError:
        pass  # folder is already exist

    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')

    # find all images in URL
    images = soup.findAll('img')

    # start downloading the images
    for image in images:
        try:
            image_link = image["src"]
            image_request = requests.get(image_link).content
            try:
                # make sure that the link only contains an image
                string = str(image_request, 'utf-8')
            except UnicodeDecodeError:  # this means that we tried to convert the content to str but the programme
                # failed doing this so the content is image
                link_content = str(image_link).split("/")
                image_file_name = link_content[-1]
                if link_content[-1].__contains__("?"):
                    end_index = link_content[-1].rfind("?")
                    image_file_name = link_content[-1][:end_index]

                if image_file_name not in images_in_folder:
                    image_file = open(f"{FOLDER_NAME}/{image_file_name}", "wb+")
                    image_file.write(image_request)
                    image_file.close()
        except Exception:
            print(f"could not locate {image['src']}")
            pass


main()
