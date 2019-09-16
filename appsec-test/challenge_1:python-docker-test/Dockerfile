# FROM alpine:3.7
# Using the latest image resolves CVE-2019-8457
FROM alpine:latest

# The application in its current state doesn't use any of this, so these are uneeded additions to the attack surface. as we have to keep
# them, lets add setfacl to allow us to harden the system a little.
RUN apk add --no-cache libressl-dev musl-dev libffi-dev gcc g++ make libpcap-dev bash git acl

RUN apk add --no-cache python3

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /etc/hello_world
WORKDIR /etc/hello_world

COPY hello_world.py /etc/hello_world
CMD ["python3","-u","./hello_world.py"]
CMD ["/bin/bash"]
