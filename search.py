import shodan
import json

api_key = 'zFsD5kmLPIzJxpg0B2dXx1bfQ1cy9Je1'

api = shodan.Shodan(api_key)

search_ip = api.host('86.12.150.19')
print(search_ip)
