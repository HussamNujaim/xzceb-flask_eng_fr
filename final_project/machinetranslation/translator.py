import json 
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'
print(apikey)
print(url)
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version 
                        ,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
        Written by: Husam Nujaim
    """
    translation = language_translator.translate(
    text=englishText, model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """
        Written by: Husam Nujaim
    """
    translation = language_translator.translate(
    text=frenchText, model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText


frenchText = englishToFrench("Hello, how are you today?")
englishText = frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?")
print(5*'*')
print('Translation EN = ', frenchText)
print(5*'*')
print('Translation FR = ', englishText)


def frenchToEnglish(frenchText):
    #write the code here
    return englishText
