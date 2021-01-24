FROM continuumio/miniconda3:4.8.2
RUN apt-get update -y && apt-get install -y build-essential && apt-get install -y make \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $HOME/src

COPY requirements.txt $HOME/src
RUN pip install -r requirements.txt