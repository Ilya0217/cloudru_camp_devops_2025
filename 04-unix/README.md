# Ответ к заданию /04-unix
# Четвертое тестовое задание для Cloud.ru Camp 2025 - DEVOPS
Поскольку **по условию** контейнер запускается без привилегий (флаг `--privileged`), следующие стандартные методы блокировки сетевого доступа **не будут работать** 
(ошибка **RTNETLINK answers: Operation not permitted**):
- Удаление маршрута по умолчанию (`ip route del default`)
- Блокировка с помощью iptables (`iptables -A OUTPUT -j DROP`)

Альтернативные решения:
1. Изменение конфигурации DNS (`resolv.conf`)
2. Модификация файла `hosts`

В обоих случаях перед внесением изменений создается резервная копия файла для возможности восстановления сетевого доступа.

## Способ 1: Изменение DNS конфигурации

```bash
# Обновляем список пакетов
apt-get update

# Создаем резервную копию
cp /etc/resolv.conf /etc/resolv.conf.bak

# Меняем DNS сервер на локальный
echo "nameserver 127.0.0.1" > /etc/resolv.conf

# Проверяем результат
apt-get update
```

## Способ 2: Изменение файла hosts

```bash
# Обновляем список пакетов
apt-get update

# Создаём резервную копию
cp /etc/hosts /etc/hosts.bak

# Блокируем доступ к Ubuntu-репозиториям
echo "127.0.0.1 archive.ubuntu.com security.ubuntu.com" >> /etc/hosts

# Проверяем результат
apt-get update
```