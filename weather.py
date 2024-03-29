from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    res = requests.get(
        f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    print("Loading...")

    soup = BeautifulSoup(res.text, 'html.parser')

    info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()

    print(info)

    with open('weather_info.txt', 'a') as f:
        f.write(info + '\n')
    
    print("finished.")
except Exception as ex:
    print(ex)

