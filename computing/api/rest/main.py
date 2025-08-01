#!/usr/bin/env python3
"""
This file is part of the Knowledge Journal
See https://github.com/augustodamasceno/knowledge-journal/
"""
__author__ = "Augusto Damasceno"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2025, Augusto Damasceno."
__license__ = "All rights reserved"


import requests
import json


class ApiClient:
    def __init__(self, url):
        # URL: 
        # [API_URL]/[ENDPOINT]
        # [PROTOCOL/HOST/API_VERSION]/[RESOURCE/IDENTIFIER] 
        self.api_url = url.rstrip('/')
        self.session = requests.Session()

    def __str__(self):
        return f"{self.api_url}"

    def __repr__(self):
        return f"{self.api_url}"

    def __getitem__(self, endpoint):
        return self.get(endpoint)

    def _send_request(self, 
                      method, 
                      endpoint, 
                      json=None, 
                      params=None, 
                      **kwargs):
        endpoint_strip = endpoint.lstrip('/')
        url = self.api_url + '/' + endpoint_strip
        try:
            response = self.session.request(method,
                                            url, 
                                            json=json, 
                                            params=params, 
                                            **kwargs)
            response.raise_for_status()
            
            if response.status_code == 204: 
                return None
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - {response.text}")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
        return None

    def get(self, endpoint, params=None, **kwargs):
        return self._send_request('GET', 
                                  endpoint, 
                                  json=None, 
                                  params=params, 
                                  **kwargs)

    def post(self, endpoint, json, **kwargs):
        return self._send_request('POST', 
                                  endpoint,
                                  json=json,
                                  params=None, 
                                  **kwargs)

    def put(self, endpoint, json, **kwargs):
        return self._send_request('PUT',
                                   endpoint,
                                   json=json,
                                   params=None, 
                                   **kwargs)

    def patch(self, endpoint, json, **kwargs):
        return self._send_request('PATCH', 
                                  endpoint, 
                                  json=json,
                                  params=None, 
                                  **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._send_request('DELETE',
                                  endpoint, 
                                  params=None, 
                                  **kwargs)


def print_section(title, subsection=False):
    repeat_char = '-' if subsection else '*'
    width = 10 if subsection else 20
    sec_String = repeat_char*width
    print(f"\n{sec_String} {title} {sec_String}\n")


if __name__ == "__main__":
    print_section("Samples using jsonplaceholder")

    print_section("POST", subsection=True)
    client_jsonplaceholder = \
        ApiClient(url="https://jsonplaceholder.typicode.com")
    post_data = {
        'title': 'Sample Post',               
        'body': 'This is a sample post.',   
        'views': 123,                   
        'rating': 4.5,                      
        'published': True,                   
        'tags': ['python', 'api', 'demo'],   
        'metadata': {
            'author': 'Jane Doe',
            'length': 350
        },
        'created_at': '2025-08-01T10:00:00Z', 
        'attachments': None
    }
    post_response = \
        client_jsonplaceholder.post(endpoint='posts', json=post_data)
    print(json.dumps(post_response, indent=4, ensure_ascii=False))

    print_section("GET", subsection=True)
    get_response = \
        client_jsonplaceholder.get(endpoint='posts/1')
    print(json.dumps(get_response, indent=4, ensure_ascii=False))

    print_section("PUT", subsection=True)
    put_data = {
        'title': 'Updated Title',
        'body': 'Updated body.',
        'userId': 1
    }
    put_response = \
        client_jsonplaceholder.put(endpoint='posts/1', json=put_data)
    print(json.dumps(put_response, indent=4, ensure_ascii=False))

    print_section("PATCH", subsection=True)
    patch_data = {
        'title': 'Patched Title'
    }
    patch_response = \
        client_jsonplaceholder.patch(endpoint='posts/1', json=patch_data)
    print(json.dumps(patch_response, indent=4, ensure_ascii=False))

    print_section("DELETE", subsection=True)
    delete_response = \
        client_jsonplaceholder.delete(endpoint='posts/1')
    print(json.dumps(delete_response, indent=4, ensure_ascii=False))

    print_section("Sample using Open-Meteo")
    client_open_meteo = \
        ApiClient(url="https://api.open-meteo.com/v1")

    print_section("GET Weather Forecast", subsection=True)
    weather_params = {
        'latitude': -12.9012459,
        'longitude': -38.7316989,
        'current_weather': True
    }
    weather_headers = {
        'User-Agent': 'KnowledgeJournal/1.0',
        'Accept': 'application/json'
    }
    weather_response = client_open_meteo.get(endpoint='forecast', 
                                             params=weather_params,
                                             headers=weather_headers)
    print(json.dumps(weather_response, indent=4, ensure_ascii=False))
