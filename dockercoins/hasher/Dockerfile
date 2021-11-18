FROM ruby:alpine
LABEL author="anderson.furtado"
RUN apk update && apk upgrade; gem install digest ; gem install sinatra ; gem install thin ; gem install puma ; gem install reel ; gem install HTTP ; gem install webrick
ADD . /dockercoins/hasher/
WORKDIR /dockercoins/hasher/
EXPOSE 80
CMD ["ruby", "hasher.rb"]