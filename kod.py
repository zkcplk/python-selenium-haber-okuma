#	Haber Okuma Programı v1
#	26.10.2019 - github.com/zkcplk

from selenium import webdriver
import time
import random

print("-----", "Haber Okuma Programı v1", "-----")

liste = {}
driver = webdriver.Firefox()


def git():
    global liste
    if 0 not in liste.values():
        driver.get('https://www.ensonhaber.com/son-dakika')
        links = driver.find_elements_by_class_name('news-item')

        for i in links:
            temp = i.get_attribute('href')
            if "videonuz.ensonhaber.com" not in temp:
                if temp not in liste:
                    liste[temp] = 0
        # print(liste)

    temp_liste = [k for k,v in liste.items() if v == 0]
    sec = random.choice(temp_liste)

    print("Gidilen Sayfa >>> " + sec)
    driver.get(sec)
    liste[sec] = 1
    time.sleep(1)

    sayac = 200
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, " + str(sayac) + ");var lenOfPage=document.body.scrollHeight-1111;return lenOfPage;")

    match = False
    while not match:
        sayac += 101
        time.sleep(0.777)
        driver.execute_script("window.scrollTo(0, " + str(sayac) + ");return true;")

        if sayac > lenOfPage:
            match = True

    time.sleep(1)
    git()


git()
