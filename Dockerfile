FROM python:3.9

COPY . /dockerSample
WORKDIR /dockerSample
ENTRYPOINT ["python", "main.py"]