import requests, json

def eval_weather(city):
    api_key = "2064d8cdd91f5d50c461dad141683165"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "q=" + city + "&appid=" + api_key

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        current_temp = x["main"]["temp"] - 273

        current_pres = x["main"]["pressure"]

        current_hum = x["main"]["humidity"]

        weather_desc = x["weather"][0]["description"]
    
        print(weather_desc)
        print("Temprature (C): " + str(current_temp))
        print("Atmospheric Pressure (hPa): " + str(current_pres))
        print("Humidity (%): " + str(current_hum))

    else:
        print("City Not Found!!")
    


city_name =input("Enter city name: ")
eval_weather(city_name)
