import requests

url = (
  "https://www.yelp.com/search?find_desc={QUERY}&find_loc={LOC}&ns=1"
  ).format(**{
    "QUERY": "Restaurants",
    "LOC": "San+Francisco%2C+CA",
  })

if __name__ == "__main__":
  r = requests.post(url)
  print r.status_code
  print r.content
