FROM ubuntu:22.04
RUN apt update && apt install -y python3 && rm -rf /var/lib/apt/list/*

COPY . . 

CMD ["python3", "game.py"]
