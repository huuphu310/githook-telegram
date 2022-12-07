FROM python:3.7-alpine
RUN apk update && apk upgrade
RUN apk add --no-cache bash\
                       gcc \
		       musl-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
