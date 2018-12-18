import shodan
import json

api_key = ''

api = shodan.Shodan(api_key)

search_ip = api.host('86.12.150.19')
print(search_ip)
