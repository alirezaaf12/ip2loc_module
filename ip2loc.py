import requests
def ip2location():

	ip_finder = ("https://api.ipify.org")

	ip_geo_finder = ("https://api.ip2country.info/ip")

	response = requests.get(ip_finder)

	ip = (response.text)

	find_location = requests.get(ip_geo_finder, params=ip)

	location_found = find_location.json()["countryName"]

	print("The given IP address location is in  %s" % location_found)

if __name__ == '__main__':
	ip2location()