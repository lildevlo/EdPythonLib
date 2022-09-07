import subprocess
import sys
import tkinter
from tkinter import *
import http.client
import json
import os
import ctypes


def prenom(username, password, storeityesorno, storeityesemplacement):
    if os.path.exists(storeityesemplacement):
        os.remove(storeityesemplacement)

    print("e")
    uName = username
    uPass = password

    print(uName)
    print(uPass)

    with open('C:/Users/Public/uName.txt', 'w') as f:
        f.write(uName)
    with open('C:/Users/Public/uPass.txt', 'w') as f:
        f.write(uPass)

    with open('C:/Users/Public/uName.txt', encoding="utf-8") as f:
        username = f.read()
    with open('C:/Users/Public/uPass.txt', encoding="utf-8") as f:
        password = f.read()

    conn = http.client.HTTPSConnection("api.ecoledirecte.com")
    payload = 'data={"identifiant":' + f'"{username}"' + ',"motdepasse":' + f'"{password}"' + '}'

    headers = {
        'authority': 'api.ecoledirecte.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-gpc': '1',
        'origin': 'https://www.ecoledirecte.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.ecoledirecte.com/',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    conn.request("POST", "/v3/login.awp", payload, headers)
    res = conn.getresponse()
    data = res.read()

    prenom = json.loads(data.decode("utf-8"))['data']['accounts'][0]['prenom']
    print(prenom)

    if storeityesorno == "yes":
        with open(storeityesemplacement, 'w') as f:
            f.write(prenom)


def nom(username, password, storeityesorno, storeityesemplacement):
    if os.path.exists(storeityesemplacement):
        os.remove(storeityesemplacement)
    print("e")
    uName = username
    uPass = password

    print(uName)
    print(uPass)

    with open('C:/Users/Public/uName.txt', 'w') as f:
        f.write(uName)
    with open('C:/Users/Public/uPass.txt', 'w') as f:
        f.write(uPass)

    with open('C:/Users/Public/uName.txt', encoding="utf-8") as f:
        username = f.read()
    with open('C:/Users/Public/uPass.txt', encoding="utf-8") as f:
        password = f.read()

    conn = http.client.HTTPSConnection("api.ecoledirecte.com")
    payload = 'data={"identifiant":' + f'"{username}"' + ',"motdepasse":' + f'"{password}"' + '}'

    headers = {
        'authority': 'api.ecoledirecte.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-gpc': '1',
        'origin': 'https://www.ecoledirecte.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.ecoledirecte.com/',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    conn.request("POST", "/v3/login.awp", payload, headers)
    res = conn.getresponse()
    data = res.read()

    nom = json.loads(data.decode("utf-8"))['data']['accounts'][0]['nom']
    print(nom)
    if storeityesorno == "yes":
        with open(storeityesemplacement, 'w') as f:
            f.write(nom)


def email(username, password, storeityesorno, storeityesemplacement):
    if os.path.exists(storeityesemplacement):
        os.remove(storeityesemplacement)
    print("e")
    uName = username
    uPass = password

    print(uName)
    print(uPass)

    with open('C:/Users/Public/uName.txt', 'w') as f:
        f.write(uName)
    with open('C:/Users/Public/uPass.txt', 'w') as f:
        f.write(uPass)

    with open('C:/Users/Public/uName.txt', encoding="utf-8") as f:
        username = f.read()
    with open('C:/Users/Public/uPass.txt', encoding="utf-8") as f:
        password = f.read()

    conn = http.client.HTTPSConnection("api.ecoledirecte.com")
    payload = 'data={"identifiant":' + f'"{username}"' + ',"motdepasse":' + f'"{password}"' + '}'

    headers = {
        'authority': 'api.ecoledirecte.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-gpc': '1',
        'origin': 'https://www.ecoledirecte.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.ecoledirecte.com/',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    conn.request("POST", "/v3/login.awp", payload, headers)
    res = conn.getresponse()
    data = res.read()

    email = json.loads(data.decode("utf-8"))['data']['accounts'][0]['email']
    print(email)

    if storeityesorno == "yes":
        with open(storeityesemplacement, 'w') as f:
            f.write(email)


def classe(username, password, storeityesorno, storeityesemplacement):
    if os.path.exists(storeityesemplacement):
        os.remove(storeityesemplacement)
    print("e")
    uName = username
    uPass = password

    print(uName)
    print(uPass)

    with open('C:/Users/Public/uName.txt', 'w') as f:
        f.write(uName)
    with open('C:/Users/Public/uPass.txt', 'w') as f:
        f.write(uPass)

    with open('C:/Users/Public/uName.txt', encoding="utf-8") as f:
        username = f.read()
    with open('C:/Users/Public/uPass.txt', encoding="utf-8") as f:
        password = f.read()

    conn = http.client.HTTPSConnection("api.ecoledirecte.com")
    payload = 'data={"identifiant":' + f'"{username}"' + ',"motdepasse":' + f'"{password}"' + '}'

    headers = {
        'authority': 'api.ecoledirecte.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-gpc': '1',
        'origin': 'https://www.ecoledirecte.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.ecoledirecte.com/',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    conn.request("POST", "/v3/login.awp", payload, headers)
    res = conn.getresponse()
    data = res.read()

    classe = json.loads(data.decode("utf-8"))['data']['accounts'][0]['profile']['classe']['libelle']
    print(classe)

    if storeityesorno == "yes":
        with open(storeityesemplacement, 'w') as f:
            f.write(classe)



