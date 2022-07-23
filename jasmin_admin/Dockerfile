FROM --platform=linux/amd64 python:3-buster

MAINTAINER Sam Ng <sam@createworld.tech>

ENV TZ=Asia/Hong_Kong
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt install -y telnet

#RUN mkdir -p /etc/jasmin/resource

ENV APP_NAME jasmin_admin

WORKDIR /usr/${APP_NAME}

COPY ${APP_NAME}/app app
COPY ${APP_NAME}/requirements.txt .
COPY cwt_datamodel app/cwt_datamodel
COPY jasmin_web_panel/main app/main
COPY django app/django
COPY rest_framework app/rest_framework

#RUN mkdir -p app/jasmin/jasmin
#COPY jasmin/jasmin/config app/jasmin/jasmin/config

RUN pip install -r requirements.txt

ENV ROOT_PATH /
ENV CONFIG_PATH /etc/${APP_NAME}

COPY ${APP_NAME}/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python3", "app/daily_quota.py"]