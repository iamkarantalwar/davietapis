import urllib.request
y = urllib.request.urlopen("http://dataservice.accuweather.com/forecasts/v1/daily/1day/195139?apikey=F2CTaJaifzwwQjIsCYpCA67xJEY55pja%20")

s = y.read().decode("utf-8")
d = json.loads(s)
print(d["DailyForecasts"][0]["Temperature"])
