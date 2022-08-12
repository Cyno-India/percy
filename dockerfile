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

# RUN apt-get update \
#     && apt-get upgrade -y \
#     && apt-get install -y \
#     build-essential \
#     libssl-dev \
#     libffi-dev \
#     python3-dev \
#     build-essential \
#     libjpeg-dev \
#     zlib1g-dev \
#     gcc \
#     libc-dev \
#     bash \
#     git \
#     && pip3 install --upgrade pip


ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
# COPY . .
# WORKDIR /app

# COPY . /app

# RUN pip3 --no-cache-dir install -r requirements.txt