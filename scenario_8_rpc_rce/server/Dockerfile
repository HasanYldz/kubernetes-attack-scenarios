FROM python:3


# Ensure bash is installed
RUN apt-get update && \
    apt-get install -y bash netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install uvicorn
RUN pip install typing_extensions
RUN pip install ./rpc.py-0.6.0

CMD ["python3", "./rpc.py-0.6.0/examples/async_server.py"]

