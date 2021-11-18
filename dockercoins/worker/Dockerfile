FROM python:alpine
LABEL author="anderson.furtado"
RUN apk update && apk upgrade ; pip install redis; pip install requests
ADD . /dockercoins/worker/
WORKDIR /dockercoins/worker/
CMD ["python", "worker.py"]