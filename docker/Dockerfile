# We choose ubuntu 22.04 because of the long-term support. The base image size is 188MB
FROM ubuntu:22.04

RUN ln -snf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime                &&\
    echo Europe/Warsaw > /etc/timezone                                      &&\
    apt-get update                                                          &&\
    apt-get install -y python3 \
    python3-pip \
    python3-setuptools                                                      &&\
    apt-get clean                                                           &&\
    rm -rf /var/lib/apt/lists/*                                             &&\
    update-alternatives --install /usr/bin/python python /usr/bin/python3 1

RUN pip3 install --upgrade pip                   &&\
    pip3 install --no-cache-dir pytest             \
										  sphinx             \
										  sphinx_rtd_theme &&\
    mkdir /workdir

ADD . /workdir/
