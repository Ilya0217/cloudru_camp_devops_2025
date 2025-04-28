# Ответ к заданию /03-kubernetes
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/00/Kubernetes_%28container_engine%29.png" 
       width="200" title="Kubernetes">
</p>

# Третье тестовое задание для Cloud.ru Camp 2025 - DEVOPS

## Коды манифестов находятся в следующих файлах:
- /base/deployment.yaml
- /base/ingress.yaml
- /base/namespace.yaml
- /base/secret.yaml
- /base/service.yaml

## Коды Helm-шаблонов
- /helm/templates/deployment.yaml
- /helm/templates/ingress.yaml
- /helm/templates/namespace.yaml
- /helm/templates/secret.yaml
- /helm/templates/service.yaml

## Запуск осуществляется командами
- **helm upgrade --install echo-app ./helm --namespace echo-app --create-namespace** - Установка Helm-приложений
- **kubectl port-forward svc/echo-app-service -n echo-app 8080:80** - Запуск веб-приложения