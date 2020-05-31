import requests
import ast

class XkcdClient():


    def api_call(self, url):
        self.urls = url

        r = requests.get(url = self.urls)
        byte_str = r.content
        dict_str = byte_str.decode("UTF-8")
        my_data = ast.literal_eval(dict_str)
        return my_data


client = XkcdClient()
response = client.api_call('https://xkcd.com/info.0.json')
print(response)
