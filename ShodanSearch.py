import shodan
import json

from flatten_json import flatten

def ShodanSearch(apiKey,ip):
	api = shodan.Shodan(apiKey)
	search_ip = api.host(ip)
	json_str = json.dumps(search_ip)
	string = json.loads(json_str)
	flat = flatten(string)

	for k,v in flat.items():
			print(k)
			print(v)
