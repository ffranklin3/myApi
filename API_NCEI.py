import requests
print("got it")

PATH = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USC00457180&format=json"

response = requests.get(PATH)
print(response.content)

print("done")
print
