from flask import Flask


app = Flask(__name__)
app.super_secret_key = 'super secret key'