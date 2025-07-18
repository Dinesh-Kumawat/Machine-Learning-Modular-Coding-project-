from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys


app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():

    try:
        raise Exception("We are testing our Exception file") # error
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)

        logging.info("We are testing our  logging file ")

        return "Welcome to My code"


if __name__ == "__main__":
    app.run(debug = True)   # 5000 port number