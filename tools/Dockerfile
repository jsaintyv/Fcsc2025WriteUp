FROM ubuntu:24.04

VOLUME /data

RUN apt update && apt install -y zip unzip binwalk python3 python3-pip xz-utils bsdmainutils make gcc z3 tcpdump tshark vim netcat-openbsd xz-utils 
RUN pip3 install pycryptodome sympy gmpy2 --break-system-packages

CMD sleep infinity
