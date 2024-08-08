import os
import requests
from requests.exceptions import HTTPError


Path = 'data'


class APIRequester:
    base_url = 'https://swapi.dev/api'
    page = {'page': 1}

    def __init__(self, url=base_url):
        self.url = url

    def get(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except HTTPError:
            response = requests.get('https://www.swapi.tech/')
            return response
        else:
            if response.status_code == 200:
                return response


class SWRequester(APIRequester):

    def __init__(self, url):
        super().__init__(url)

    def get_sw_categories(self):
        # response = get(f'{self.url}api')
        response = requests.get('https://swapi.dev/api/')
        dict_sw_categories = response.json().keys()
        return dict_sw_categories

    def get_sw_info(self, sw_type: str):
        self.encoding = 'utf-8'
        sw_type_text = requests.get(f'{self.base_url}/{sw_type}/').text
        return sw_type_text


def save_sw_data():

    swapi = SWRequester()
    os.makedirs(Path, exist_ok=True)
    for i in swapi.get_sw_categories():
        # name_file = Path(Dir, f'{i}.txt')
        with open(f'{Path}/{i}.txt', 'w') as f:
            f.write(swapi.get_sw_info(i))


if __name__ == '__main__':
    save_sw_data()
