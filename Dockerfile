FROM python:3.7-alpine

LABEL maintainer="Amin Vakil <info@aminvakil.com>"

COPY requirements.txt /usr/local/src/

RUN pip install --no-cache-dir -r /usr/local/src/requirements.txt --upgrade

COPY modules /usr/local/src/modules
COPY insides /usr/local/src/insides
COPY SiteBroker.py /usr/local/src/

WORKDIR /usr/local/src

CMD ["python", "SiteBroker.py"]
