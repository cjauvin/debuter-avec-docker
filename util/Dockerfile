FROM python

RUN pip install cowsay

COPY say_hello.py /inside_container/

WORKDIR /inside_container

ENTRYPOINT ["python", "say_hello.py"]
