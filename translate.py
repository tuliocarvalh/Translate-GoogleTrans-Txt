from cgitb import text
from googletrans import Translator
import json
import traceback

text_trans = open("text_to_translate.txt", "a")

def trans():
    urls = ["translate.google.com", "translate.google.com.ar", "translate.google.com.br",]
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    return Translator(service_urls=urls, user_agent=user, raise_exception=False, timeout=None)

text_ = text_trans

print(trans().translate(text_, dest='pt'))
