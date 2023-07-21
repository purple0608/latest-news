FROM ubuntu

RUN apt-get update && apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip install flask requests requests-html bs4 pymongo asyncio

COPY . /opt/source-code

WORKDIR /opt/source-code

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
