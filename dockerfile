# FROM python:3

# ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /code

# # Install dependencies
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # Copy project
# COPY . .

FROM python:3

# # RUN apt-get update \
# #     && apt-get upgrade -y \
# #     && apt-get install -y \
# #     build-essential \
# #     libssl-dev \
# #     libffi-dev \
# #     python3-dev \
# #     build-essential \
# #     libjpeg-dev \
# #     zlib1g-dev \
# #     gcc \
# #     libc-dev \
# #     bash \
# #     git \
# #     && pip3 install --upgrade pip


# ENV LIBRARY_PATH=/lib:/usr/lib

# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# # Set work directory
# WORKDIR /code

# # Install dependencies
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# COPY ./entrypoint.sh /
# ENTRYPOINT [ "sh", "/entrypoint.sh" ]
# Copy project
# COPY . .
# WORKDIR /app

# COPY . /app

# RUN pip3 --no-cache-dir install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# COPY ./scripts /scripts
# COPY ./script.sh /script.sh
# COPY ./root /var/spool/cron/crontabs/root


# RUN ls -l /app


WORKDIR /code
EXPOSE 8000


# USER root 
# RUN apk upgrade --available
# RUN apk add --no-cache tini openrc busybox-initscripts
RUN pip install -r /requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh","/entrypoint.sh" ]