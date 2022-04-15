import requests
from bs4 import BeautifulSoup
import argparse

def get_by_bs4(term):

	URL = "https://www.urbandictionary.com/define.php?term="
	f_URL = URL + term 
	page = requests.get(f_URL)
	soup = BeautifulSoup(page.content, "html.parser")
	definition = soup.find("div",class_="meaning mb-4")
	return definition.get_text()

def get_by_json(term):

	URL = "https://api.urbandictionary.com/v0/define?term="
	f_URL = URL + term
	page = requests.get(f_URL)
	results = page.json()
	definitions = results.get("list")
	return definitions[0]["definition"]

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--term", type=str, required=True, help="term to be defined")
	parser.add_argument("--get_by_bs4", help="scrap definition by beautifulsoup", action="store_true")
	parser.add_argument("--get_by_json", help="scrap definition by json", action="store_true")
	args = parser.parse_args()

	if args.get_by_bs4:
		definition = get_by_bs4(args.term)
		print(definition)
	elif args.get_by_json:
		definitions = get_by_json(args.term)
		print(definitions)
	else:
		print("No method specified")

if __name__ == '__main__':
	main()




