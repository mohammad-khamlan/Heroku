FROM python:3.6-slim
WORKDIR /home/mohammad/ML/Microservice
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000/tcp
EXPOSE 5000/udp
CMD ["python", "./house_price.py","-p","model.pickle"]

