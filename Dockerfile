FROM python:3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install git openssh-client iproute2 procps lsb-release \
    && pip --disable-pip-version-check --no-cache-dir install pylint \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=dialog
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

ENV PORT=8050
EXPOSE ${PORT}
ENV GUNICORN_BIND="0.0.0.0:"${PORT} 
CMD ["gunicorn", "--config", "gunicorn.conf", "app:app"]