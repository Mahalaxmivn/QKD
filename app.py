from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pickle
import pandas as pd
import numpy as np
from flask import session
import uuid
import json
from datetime import datetime
from dbconnect import *

import os

import hashlib
from datetime import datetime
import numpy as np
import random
import requests

from flask import Flask, send_file
import os
import datetime
import hashlib
import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def generate_random_bits(length):
    """Generate a list of random bits (0 or 1)."""
    return [random.randint(0, 1) for _ in range(length)]


def generate_random_bases(length):
    """Generate a list of random bases ('+' or 'x')."""
    return [random.choice(['+', 'x']) for _ in range(length)]


def encode_qubits(bits, bases):
    """Encode bits into qubits using the chosen bases."""
    return [(bit, base) for bit, base in zip(bits, bases)]


def measure_qubits(qubits, bases):
    """Measure qubits based on the receiver's bases."""
    measured_bits = []
    for (bit, base), recv_base in zip(qubits, bases):
        if base == recv_base:
            measured_bits.append(bit)
        else:
            measured_bits.append(random.randint(0, 1))
    return measured_bits


def compare_bases(sender_bases, receiver_bases):
    """Compare the sender's and receiver's bases to find matching indices."""
    return [i for i in range(len(sender_bases)) if sender_bases[i] == receiver_bases[i]]


def generate_key(bits, indices):
    """Generate the final key using bits at matching indices."""
 
    res= [bits[i] for i in indices]
    
   
    return res


def bits_to_bytes(bits):
    """Convert a list of bits into a bytes object."""
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte_chunk = bits[i:i+8]
        byte_array.append(int(''.join(map(str, byte_chunk)), 2))
    return bytes(byte_array)


def derive_aes_key(shared_key_bits):
    """
    Derive an AES key from the shared key bits.
    Convert the bits to bytes and hash them to get a 256-bit AES key.
    """
    shared_key_bytes = bits_to_bytes(shared_key_bits)
    return hashlib.sha256(shared_key_bytes).digest()  # Derive a 256-bit AES key


def aes_encrypt(message, key):
    """
    Encrypt a message using AES encryption.
    """
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC mode
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return cipher.iv, ciphertext


def aes_decrypt(iv, ciphertext, key):
    """
    Decrypt a ciphertext using AES decryption.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')
def save_to_file(filename, data):
    """Save binary data to a file."""
    with open(filename, 'wb') as file:
        file.write(data)


def load_from_file(filename):
    """Load binary data from a file."""
    with open(filename, 'rb') as file:
        return file.read()




app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memfileuploadencryptd'
app.config['SECRET_KEY'] = 'super secret key'



@app.route('/')
def hello():
    message= ''
    return render_template("login.html")

@app.route('/index')
def index():
    message= ''
    return render_template("login.html")

@app.route('/signup')
def signup():
    message= ''
    return render_template("register.html",message = message)

def inboxinfo():
    dataQuery = "select * from emailnfo where toemail='"+session['email']+"'"
    print(dataQuery)
    dataInfo = recoredselect(dataQuery)
    print(dataInfo)
    messages = []
    for i in dataInfo:
        data={}
        data["from"]=i[2]
        data["content"]=i[5]
        data["date"]=i[7]
        data["fileid"]=i[0]
        data["keyid"]=i[1]
        messages.append(data)

    return messages

@app.route('/inbox')
def inbox():
    return render_template("home.html",messages = inboxinfo(),name=session['name'])

@app.route('/send')
def send():
    dataQuery = "select * from emailnfo where useremail='"+session['email']+"'"
    print(dataQuery)
    dataInfo = recoredselect(dataQuery)
    print(dataInfo)
    messages = []
    for i in dataInfo:
        data={}
        data["from"]=i[3]
        data["content"]=i[5]
        data["date"]=i[7]
        data["fileid"]=i[0]
        data["keyid"]=i[1]
        messages.append(data)

    message= ''
    return render_template("send.html",messages = messages,name=session['name'])


@app.route('/decrypt',methods=['GET','POST'])
def decrypt():
    file_id=request.args.get('id')
    key_id=request.args.get('fileid')
    
    enfile="Encrypt/"+str(file_id)+"ciphertext.bin"
    ivfile="IV/"+str(file_id)+"iv.bin"
    loaded_iv = load_from_file(ivfile)
    loaded_ciphertext = load_from_file(enfile)
    filename="key/"+str(key_id)+".pkl"
    with open(filename, 'rb') as fp:
       aes_key = pickle.load(fp)


    decrypted_message = aes_decrypt(loaded_iv, loaded_ciphertext, aes_key)
    print(decrypted_message)
    

    return render_template('decryptedmessage.html',message= decrypted_message, name=session['name'])



@app.route('/signin')
def signin():
    message= ''
    return render_template("login.html",message = message)
import pickle
def keygeneration(filename):
    key_length = 128  # Length of the raw key
    # Step 1: Sender generates random bits and bases
    sender_bits = generate_random_bits(key_length)
    sender_bases = generate_random_bases(key_length)
    # Step 2: Receiver generates random bases
    receiver_bases = generate_random_bases(key_length)

    # Step 3: Sender encodes qubits and receiver measures them
    qubits = encode_qubits(sender_bits, sender_bases)
    receiver_measured_bits = measure_qubits(qubits, receiver_bases)

    # Step 4: Compare bases and generate the shared key
    matching_indices = compare_bases(sender_bases, receiver_bases)
    sender_key = generate_key(sender_bits, matching_indices)
    aes_key = derive_aes_key(sender_key)
    with open("key/"+filename, "wb") as file:
        pickle.dump(aes_key, file)
   
    

@app.route('/register', methods=["POST"])
def register():
    if request.method == 'POST':
        birthday = request.form["birthday"]
        gender = request.form["gender"]
        email = request.form["email"]
        password= request.form["password"]
        username= request.form["username"]
        dataQuery="SELECT id FROM account ORDER BY id DESC LIMIT 1"
        dataInfo = recoredselect(dataQuery)
        print(dataInfo)
        id=1
        if(len(dataInfo)>0):
            id=dataInfo[0][0]+1
        filename=str(id)+".pkl"
        keygeneration(filename)
        sql1='insert into account(username,email,password,birthday,gender,sender_key) values("%s","%s","%s","%s","%s","%s")' % \
                    (username,email,password,birthday,gender,filename)
        print(sql1)
        inserquery(sql1)

        message=email+" account Created Sucessfully"
    return render_template('login.html', message =message)

@app.route('/authorised',methods = ["GET","POST"])
def authorised():
    message= '' 
    email= request.form["email"]
    password= request.form["password"] 
    print("-----------------------------")
    print(email)
    dataQuery = "select * from account where email='"+email+"' && password='"+password+"'"
    print(dataQuery)
    dataInfo = recoredselect(dataQuery)
    print(dataInfo)
    if(dataInfo):
        session['id'] = dataInfo[0][0]
        session['name'] = dataInfo[0][1]
        session['email'] = dataInfo[0][2]
        return render_template("home.html",messages = inboxinfo(),name=session['name'])
    else:
        return render_template('index.html', message =message)
from datetime import datetime

@app.route('/emailcomposed')
def emailcomposed():
    return render_template("emailcompose.html",name=session['name'])

@app.route('/emailcompose', methods=["POST"])
def emailcompose():
    if request.method == 'POST':
        toemail = request.form["toemail"]
        subject = request.form["subject"]
        messageinfo = request.form["message"]
        filename="key/"+str(session['id'])+".pkl"
        with open(filename, "rb") as file:
            loaded_data = pickle.load(file)
        iv, ciphertext = aes_encrypt(messageinfo, loaded_data)
        dataQuery="SELECT id FROM emailnfo ORDER BY id DESC LIMIT 1"
        dataInfo = recoredselect(dataQuery)
        print(dataInfo)
        id=1
        if(len(dataInfo)>0):
            id=dataInfo[0][0]+1
        filenameiv=str(id)+"iv.bin"
        filenameciper=str(id)+"ciphertext.bin"
        print("Ciphertext:             ", ciphertext)
        save_to_file("IV/"+filenameiv, iv)
        save_to_file("Encrypt/"+filenameciper, ciphertext)
        dataQuery = "select * from account where email='"+toemail+"'"
        print(dataQuery)
        current_date = datetime.now()
        formatted_date = current_date.strftime("%m/%d/%Y")
        dataInfo = recoredselect(dataQuery)
        print(dataInfo)
        message=""
        if(dataInfo):
            sql1='insert into emailnfo(userid,useremail,toemail,toname,subject, message, date) values("%s","%s","%s","%s","%s","%s","%s")' % \
                        (session['id'],session['email'],toemail,dataInfo[0][1],subject,filenameciper,formatted_date)
            print(sql1)
            inserquery(sql1)
            message="Message Send Sucessfully"
        else:
            message="Invalid Email Id"
       
    return render_template("home.html",messages = inboxinfo(),message=message, name=session['name'])

@app.route('/home')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)