FROM ubuntu:22.04
RUN apt update && apt install -y python3 && rm -rf /var/lib/apt/list/*

COPY . . 

# Указываем команду, которая будет выполняться при запуске контейнера
CMD ["python3", "game.py"]