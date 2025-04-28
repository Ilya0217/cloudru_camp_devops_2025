# Ответ к заданию /01-application
# Первое тестовое задание для Cloud.ru Camp 2025 - DEVOPS

## Пуш образа в регистри

- "docker login" : аутентификация в docker hub
- "docker build -t ilya0923/echo-server-python" : для сбора образа
- "docker push ilya0923/echo-server-python" : пушим образ в репозиторий

## Запуск контейнера

- "docker run -d -p "8000:8000" -e AUTHOR="Ilya Sulimenko" ilya0923/echo-server-python