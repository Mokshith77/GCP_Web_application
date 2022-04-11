FROM python:3.7-alpine
WORKDIR /myapp
COPY . /myapp
RUN pip3 install -U -r requirements.txt
RUN pip3 install yfinance --upgrade --no-cache-dir
EXPOSE 443
CMD ["python" , "app.py"]