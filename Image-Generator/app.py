# app.py
from flask import Flask, request, jsonify, render_template, Markup, redirect

from bs4 import BeautifulSoup
import requests
import re
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap
import time
import base64
from io import BytesIO,StringIO
import sys
import math

def transform(text):
    finalText = ''
    for i, char in enumerate(text):
        if i % 2 != 0:
            char = char.replace(char, char.upper())
            finalText += char
        else:
            finalText += char

    return finalText

def trinsfirm(text):
    finalText = ''
    consonant = ['a', 'u', 'e', 'o','A', 'U', 'E', 'O']
    for char in text:
        if char in consonant:
            char = char.replace(char, 'i')
            finalText += char
        else:
            finalText += char

    return finalText




app = Flask(__name__, static_url_path='/static')


@app.route('/result', methods=['POST'])
def result():
	mode=str(request.form['mode'])
	print(mode, file=sys.stderr)
	if(request.form['texturl']=="" and request.form['text']==""):
		return redirect("/")
	elif(request.form['texturl']==""):
		modeinput=2
	elif(request.form['text']==""):
		modeinput=1
	if(modeinput==1):
	    alamat=request.form['texturl']
	    response = requests.get(alamat)
	    soup = BeautifulSoup(response.text, "html.parser")
	    a=soup.find('span', {'class' : 'message-text'})
	    text2=a.text
	    if(text2==""):
	        hasil=soup.find('title')
	        text=hasil.text
	        text=re.sub(r"http\S+", "", text)
	        text=re.sub(r".+?(?=: \")", "", text)
	        text=text[3:-1]
	        text=re.sub(r"…", "", text)
	    else:
	        text="Gagal"
	elif(modeinput==2):
	    text = request.form['text']
	  
	    
	if(mode=="1"):
		print(request.form['ukuran'], file=sys.stderr)
		ukuran=str(request.form['ukuran'])
		if(request.form['ukuran']==""):
			ukuran="square"
		if(ukuran=="square"):
			url = 'https://picsum.photos/480/500/?random'
		else:
			url = 'https://picsum.photos/480/853/?random'
		r = requests.get(url=url)
		image = Image.open(BytesIO(r.content))
		image = ImageEnhance.Brightness(image)
		image = image.enhance(0.5)
		draw = ImageDraw.Draw(image)
		(x, y) = (40, 70)
		color = 'rgb(255, 255, 255)'
		font = ImageFont.truetype('Roboto-Light.ttf', size=22)
		text = textwrap.fill(text, width=40)
		draw.text((x, y), text=text, fill=color, font=font)

		font = ImageFont.truetype('Roboto-Light.ttf', size=15)
		if(ukuran=="square"):
			draw.text((10, 480), text='twitter.com/pakdhe_girang', font=font)
		else:
			draw.text((10, 830), text='twitter.com/pakdhe_girang', font=font)
	if(mode=="5"):
		print(request.form['ukuran'], file=sys.stderr)
		ukuran=str(request.form['ukuran'])
		if(request.form['ukuran']==""):
			ukuran="square"
		if(ukuran=="square"):
			url = 'https://picsum.photos/480/500/?random'
		else:
			url = 'https://picsum.photos/480/853/?random'
		r = requests.get(url=url)
		image = Image.open(BytesIO(r.content))
		image = ImageEnhance.Brightness(image)
		image = image.enhance(0.5)
		draw = ImageDraw.Draw(image)
		(x, y) = (40, 70)
		color = 'rgb(255, 255, 255)'
		font = ImageFont.truetype('DK Combustible.otf', size=52)
		text=text.title()
		text = textwrap.fill(text, width=10)
		draw.text((x, y), text=text, fill=color, font=font)

		font = ImageFont.truetype('Roboto-Light.ttf', size=15)
		if(ukuran=="square"):
			draw.text((10, 480), text='twitter.com/pakdhe_girang', font=font)
		else:
			draw.text((10, 830), text='twitter.com/pakdhe_girang', font=font)    
	elif(mode=="2" or mode=="3" or mode=="4"):
	    if(mode=="2"):
	        text=transform(text)
	        urlgambar="static/image/meme_new.png"
	    elif(mode=="3"):
	        text=trinsfirm(text)
	        urlgambar="static/image/meme_khaleesi.png"
	    elif(mode=="4"):
	        text=trinsfirm(text)
	        urlgambar="static/image/meme_sd.png"
	    image = Image.open(urlgambar)
	    draw = ImageDraw.Draw(image)
	    
	    color = 'rgb(255, 255, 255)'
	    color2 = 'rgb(0, 0, 0)'
	    font = ImageFont.truetype("impact.ttf", 42)
	    text = textwrap.fill(text, width=46)
	    #print(round(len(text)/46))
	    text_width, text_height = draw.textsize(text, font)
	    (x, y) = ((890-text_width)/2, 420-text_height)
	    draw.text((x-2, y-2), text, font=font, fill=color2,align="center")
	    draw.text((x+2, y-2), text, font=font, fill=color2,align="center")
	    draw.text((x-2, y+2), text, font=font, fill=color2,align="center")
	    draw.text((x+2, y+2), text, font=font, fill=color2,align="center")
	    
	    draw.text((x, y), text=text, fill=color, font=font,align="center")
	    font = ImageFont.truetype('Roboto-Light.ttf', size=15)
	    draw.text((700,10), text='twitter.com/pakdhe_girang', font=font)
	    # thicker border
	buffered = BytesIO()
	image.save(buffered, format="JPEG")
	myimage = buffered.getvalue()                     
	imgstr=base64.b64encode(myimage).decode('ascii')
	return render_template('result.html',image=imgstr)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.debug = True
    app.run(threaded=True, port=5000)