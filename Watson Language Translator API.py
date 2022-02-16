# -*- coding: utf-8 -*-
!pip install ibm_watson wget


from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/adccffce-b0f0-4639-98af-0479f16ddf66'
apikey_lt='LWqPzhPAW0thUgSMom8bru7__s0l3Qr3tMwG1S1Dbt1A'
version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

translation_response = language_translator.translate(
    text='this is an automatic translation', model_id='en-es').get_result()

print (translation_response)