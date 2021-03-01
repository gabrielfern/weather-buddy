FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=5000

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    apt-get install -y npm

WORKDIR weather-buddy

COPY . .

RUN pip3 install -r requirements.txt
RUN npm install
RUN npm run build

CMD ["gunicorn", "-w", "1", "app:app"]
