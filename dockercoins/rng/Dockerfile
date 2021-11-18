FROM python:alpine
LABEL author="anderson.furtado"
RUN apk update && apk upgrade ; apk add pip ; pip install Flask
ADD . /dockercoins/rng/
WORKDIR /dockercoins/rng/
EXPOSE 80
CMD ["python", "rng.py"]