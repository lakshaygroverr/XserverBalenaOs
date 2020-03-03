###
# Build stage
##
#FROM balenalib/%%BALENA_MACHINE_NAME%%-node:10-build as build

FROM balenalib/i386-debian-python:3.6-buster-build

USER root
WORKDIR /usr/src/app
	
RUN apt-get update
RUN apt-get install python3-tk

 

COPY . ./


CMD ["python3","new_video.py"]
