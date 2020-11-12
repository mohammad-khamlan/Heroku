FROM python:3.8.1

WORKDIR /Microservice
COPY . /Microservice

RUN pip install -r requirements.txt

EXPOSE 5000/tcp
EXPOSE 5000/udp

ENTRYPOINT ["python", "house_price.py","-p","model.pickle"]

