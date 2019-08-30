FROM continuumio/miniconda3
#Maintainer : Kaikala vinay
#Date : 26-07-2019
#Gene Query 
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
RUN apt-get update -y
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion python-pip python-dev build-essential

COPY ./docker/base.yml /base.yml
RUN conda env update -f /base.yml

ENTRYPOINT ["fra_api"]
CMD ["-p 5000"]
