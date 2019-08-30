FROM python:3.6.5-slim


ADD resources /resources/
RUN python --version
RUN chmod +x /resources/test.sh
RUN chmod +x /resources/runservices.sh

WORKDIR /resources/
RUN pip install -r ./requirements.txt

ONBUILD ADD application /application/

WORKDIR /application

EXPOSE 80
ENTRYPOINT /resources/runservices.sh
