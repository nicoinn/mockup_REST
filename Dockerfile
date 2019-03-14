FROM python:3-alpine

EXPOSE 5000 

RUN pip install flask tailer

RUN mkdir /data 

ADD server.py /

ENTRYPOINT ["python","/server.py"]
