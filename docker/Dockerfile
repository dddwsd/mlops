# base image를 ubuntu 18.04로 설정
FROM ubuntu:18.04

# apt-get update 명령어 실행
RUN apt-get update

# TEST env var의 값을 hello로 설정
ENV TEST hello

# DOCKER CONTAINER가 시작될 때, 환경변수 TEST의 값을 출력.
CMD echo $TEST