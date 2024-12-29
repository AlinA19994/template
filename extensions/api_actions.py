from http.client import responses

import requests

header = {'Content-Type': 'applications/json'}


class APIActions:

    @staticmethod
    def get(path):
        response = requests.get(path)
        return response

    @staticmethod
    def extract_value_from_response(response, nodes):
        extract_value = None
        response_json = response.json()
        if len(nodes) == 1:
            extract_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extract_value = response_json[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extract_value = response_json[(nodes[0])][(nodes[1])][(nodes[2])]
        return extract_value


    @staticmethod
    def post(path, payload):
        response = requests.post(path, json=payload, headers=header)
        return response

    @staticmethod
    def put(path, payload):
        response = requests.put(path, json=payload, headers=header)
        return response

    @staticmethod
    def delete(path):
        response = requests.delete(path)
        return response.status_code
