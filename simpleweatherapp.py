from tkinter import *
from tkinter.simpledialog import askstring
import ttkbootstrap as ttkb
import requests
import json
from PIL import ImageTk, Image

# MAIN WINDOW
root = ttkb.Window()
root.minsize(400, 150)
root.maxsize(400, 150)
canvas = Canvas(root ,width=400,height=150)
canvas.pack(fill="both")
root.title("Simple Weather App By Marouane")
root.iconbitmap("")
root.geometry('400x150')
# GET INPUT
location = askstring("City Name", "Please Enter A City Name")
try:
    # BACKGROUND API CALLS
    endpoint_background="https://pixabay.com/api/"
    api_key_background= "41945838-1cd48d9e692e35e97da341b9d"
    query_background= {"key":api_key_background, "q":location, "min_height":150 ,"min_width":400, "image_type":"photo", "orientation":"horizontal", "category":"places", "safesearch":"true" ,"page":1, "per_page":3}
    response_background= requests.get(endpoint_background, params=query_background)
    # LOAD BACKGROUND IMAGE
    urlbg = json.loads(response_background.text)["hits"][0]["largeImageURL"]
    bgimg = requests.get(urlbg, stream=True).raw
    # SET BACKGROUND AS PIC OF CITIES
    bgimg = Image.open(bgimg)
    resized_bg = bgimg.resize((400,150))
    resized_bg = ImageTk.PhotoImage(resized_bg)
    canvas.create_image(0,0, image=resized_bg, anchor="nw")
except KeyError:
    print("Image Not found!")
# WEATHER API CALLS
endpoint_weather="http://api.weatherapi.com/v1/current.json"
api_key_weather= "2db4000d85b94b10bc2204407241801"
try:
    query_weather= {"Key":api_key_weather, "q":location,"aqi":"yes"}
    response_weather= requests.get(endpoint_weather, params=query_weather)
    city = json.loads(response_weather.text)["location"]["name"]
    temp = json.loads(response_weather.text)["current"]["temp_c"]
    condition = json.loads(response_weather.text)["current"]["condition"]["text"]
    # LOAD ICON URL FROM THE API
    url = json.loads(response_weather.text)["current"]["condition"]["icon"]
    img = requests.get("".join(("https:",url)), stream=True).raw
except KeyError:
    print("city Not found!")

# ELEMENTS OF THE MAIN WINDOW
try:
    canvas.create_text(118,100,text=city.upper(),font=("Helvetica",25),fill="white")
    canvas.create_text(90,50,text=temp,font=("Helvetica",40),fill="white")
    canvas.create_text(160,30,text="PIC PROVIDED BY PIXABAY.COM",font=("Helvetica",9),fill="white")
    canvas.create_text(160,30,text=condition,font=("Helvetica",9),fill="white")
    # LOAD CONDITION ICON
    img = Image.open(img)
    resized_icon = img.resize((175,160))
    resized_icon = ImageTk.PhotoImage(resized_icon)
    canvas.create_image(225,0, image=resized_icon, anchor="nw")
except NameError or KeyError:
    print("No data Provided!")
root.mainloop()
