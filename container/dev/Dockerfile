FROM python:3.6.5-slim

WORKDIR /application

ADD ./application/requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ADD ./container/dev/resources /resources/
RUN chmod +x /resources/test.sh
RUN chmod +x /resources/runservices.sh

ONBUILD ADD application /application/
EXPOSE 80
ENTRYPOINT /resources/runservices.sh
