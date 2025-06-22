import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return as bytes to pass the test

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # Return as parsed Python list/dict
