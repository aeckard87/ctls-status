FROM joyzoursky/python-chromedriver:3.8-selenium

RUN pip3 install requests

COPY ["status.py", "/"]
