from bs4 import BeautifulSoup

from google.cloud import storage

from google.oauth2 import service_account

import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "sincere-charmer-382223",
  "private_key_id": "b7712d85f8fd7161ac29aac61256fbb7e7516d8d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDjbWkCE22/jPQT\niCd8IB+tlqFQi9Aqf+9EuQatsd1QZd/UbRORT7m+8Oq5nBF+WRjXvtPXh5x05++2\nVJFKrZ0iMs/FwJgR46stSeIkPR3b2vWi1LEqC433bysKmG62u/NdbEWf1GNupxs4\nLwyx1Gw0ma57mOhrVfMQ9mwc5WkFCBRBcBZeyT05THckoaNIedLUi6XI3/U/oObz\nXRKq4nehYncOTsNzXJ0Pk4DY6Qt6qvUud5cpl3oy7nm+E3/m0aRIEsl8vHOIpi5y\n78Oy3WmQUYO0DonO9762aUQaZ4q3aNAMyjivNcKr8AMoFhqH0JsrKmAESp1Mhm1Y\nH97IuyiRAgMBAAECggEAOImfQIMcdjFgDwf6yuaAgYqwDSJIzHvz+zllIeKU8nL0\n/y3jnqz7b+6b56sXBTo4jQ/VQaAmosBzDPh+ixpYdSM9GDvuAgp/aDmVFK214c1P\n4dwus9VeBFxYTqDA60ATus6bC2YFFwHHaEL4DLBSewwWfobvhpl+HOIp09ArOLLG\nv+VHcVZ0US6HSlrmXGqUXVO1pe/rWaXwKXSwfCowW0MzVvj+eL47RY6WvHvRm+Y0\nuQ4yRAm/y7EW6BbN0CMmMeOkqpjG2Dsirx+3PnBROozSOyrTDOi8iLAIrVxNeFVj\nj5Xx3v17gUsy+wM4oGKsvMX0vwLkPPjSIqdMeHLu3QKBgQDx90kRhI4sNyI1eoQs\nknhxtUkxSIyecbDNeLcLKCFeiFIHuhavQOlBaOshb/iBZ8/qkdE9sR7oSMmf8CD/\nQp0W11lluRUlJJ1qCx/wtcqCLCX9Hp1tdcciGdjswXGn5EjDL1i9sn6rMETfBBrF\nZ6aMhFBeA3txs2SvCDpS/5PchQKBgQDwnkF5bOG3TAK9H5IWCSXPOXm92+da2Xd5\nT3S0CKpgcIiaMPk3TNNbNuCu9rKK0w9TE30J9o1CPShRYahq0yoGBG3JKAx1o0R/\nX8/Ba0SiAz1eCVwRT255hpGJmm3ScRgT25HFc7pLF4zLih3yMOfaP++yBEWVW0ra\n0d4iqnavnQKBgFJ6/QlfqicgVCTusoePFkeMiHqoRGbuUlp4P80pzNYwmeXQZVMw\nSVLmtOAdDxTtkk5fjnf9HJAJ39EJRfY9etcCaZLnWHHk3VP8ntKq5XEiI4D5Iqjh\ncRQKw4tRFbEpfDQsu49OfSdVuORcvdN01a0onUyu2zGS+UtA/sC0Jm8RAoGBAIid\nshsZQQbrd1qeBDnSs872mTK9GpywgG82N9LIYMQk4Mp7J+TID/DoNaXhl/nOYBMR\nK5tui0Giq7OZOSB+CIwmE5d0z64zJv8TDUiKeQtrv3oW4llJujXxu8xfDB/B6qPL\ntPZhANMF6gDeyKXsMpfuWU+/sSpeDSA0rGUOWBjZAoGBAOYi8p/8LoOXApX88urQ\n5L+c3MHxgunflwypNMfEpxVH7CqE7IHahqc0u5vLJKrGZ5GN7gnnew/kZSBIDEQ3\nJZGl930lN88uKviyjRaIp8OEWAP1k1zHWNsQzFlhVFVt9ucX7gveROQA5RsOIpA4\nJssFXM84n16gUEm+LvhB2jC8\n-----END PRIVATE KEY-----\n",
  "client_email": "1050258850049-compute@developer.gserviceaccount.com",
  "client_id": "102970204787444409043",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/1050258850049-compute%40developer.gserviceaccount.com"
}

try:
    res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    print("Loading...")

    soup = BeautifulSoup(res.text, 'html.parser')
    
    info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
    
    print(info)
    
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('weather_dataops')
    blob = bucket.blob('weather_info_actions.txt')
    blob.upload_from_string(info + '\n')
    
    print('File uploaded.')
    
    print("Finished.")
except Exception as ex:
    print(ex)
