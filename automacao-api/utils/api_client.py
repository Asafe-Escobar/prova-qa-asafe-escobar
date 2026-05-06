import requests
from config import BASE_URL, TIMEOUT, DEFAULT_HEADERS

class ApiClient:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, timeout=TIMEOUT)

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=payload, timeout=TIMEOUT)

    def put(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, json=payload, timeout=TIMEOUT)

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, timeout=TIMEOUT)
