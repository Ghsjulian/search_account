import time
import sys
import mechanize
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)




@app.route('/',methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    value = request.form['name']
    return render_template('index.html',msg = Attack (value))
    #Attack (value)
 
  return render_template('index.html')

def saveFile(get_data):
  f = open("index.html","r+")
  f.write(get_data)
  f.close()


def Attack (get_value):
  post_url='https://web.facebook.com/login/identify/?ctx=recover&from_login_screen=0'

  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',}

  browser = mechanize.Browser()
  browser.addheaders = [('User-Agent',headers['User-Agent'])]
  browser.set_handle_robots(False)
  response = browser.open(post_url)
  browser.select_form(nr=0)
  browser.form['email'] = get_value
  response = browser.submit()
  response_data = response.read()
  data = response_data.decode()
  #saveFile(data)
  if 'Try entering your password' in data:
    saveFile(data)
    return "Account Found Successfully ! Please Open 'index.html' File On Your Browser"

  elif 'Choose your account' in data:
    saveFile(data)
    return "The Name Has Multiple Account Please Cheak Your HTML File !"
    
  elif 'We can send you a login code' in data:
    saveFile(data)
    return "Account Found With OTP !"
  else:
    saveFile(data)
    return "No Account Found !"




app.run(debug= True , use_reloader = True , host="0.0.0.0")