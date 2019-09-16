# -*- encode: utf-8 -*-
import re
import requests


def download_js_css(path, url):
    encoding = "utf-8"
    pattern  = "(?<=href=\")[^\"]+?.css(?=\")"
    response = requests.get(url)
    filename = path + "CV.js"
    cssname  = path + "CV.css"
    with open(filename, "w", encoding=encoding) as f:
        f.write(re.sub(pattern, "CV.css", response.text))
    response = requests.get(re.findall(pattern, response.text)[0])
    with open(cssname, "w", encoding=encoding) as f:
        f.write(response.text)

zh = "https://gist.github.com/Iydon/1bc138b5ebaa8fc6233af06c06368aa0.js"
en = "https://gist.github.com/Iydon/4489aa03ff00893bb1a01151d67b5afd.js"

download_js_css("./", zh)
download_js_css("en/", en)
