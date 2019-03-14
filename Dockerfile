FROM python:3-alpine

EXPOSE 5000 

RUN pip install flask tailer

RUN mkdir /data 

ADD server.py /

ARG VCS_REF

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/nicoinn/mockup_REST"

ENTRYPOINT ["python","/server.py"]
