# Ответ к заданию /03-kubernetes

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