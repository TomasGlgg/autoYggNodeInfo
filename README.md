# autoYggNodeInfo

## Описание
Автоматическое подстановка вывода команды в значение NodeInfo.

## Использование
В файле settings.json дожлны содержаться настройки для подстановки в формате json:
```json
{
  "<name>": "<command>"
}
```
### Запуск
```
sudo python3 update.py <путь до входного конфига> <путь до выходного конфига>
```
**Важно! Входной конфиг должен быть в формате json!**

## Пример
### Входные значения конфигов:
```settings.conf```:
```json
{
  "update": "date +%T%Z"
}
```
```/etc/yggdrasil.conf```:
```json
{
    "Listen": [
        "tcp://x.x.x.x:y"
    ],
    "NodeInfo": {
        "contanct": {
            "bitmessage": "BM-2cWVVbnxwNDYYuJJcwqD7yk6GSGWqsw1n3",
            "vk": "vk.com/tmsconsole"
        },
        "name": "TomasGlComp"
        },
    "Peers": [
        "tcp://x.x.x.x:y"
    ]
}
```
____
```
$ sudo python3 update.py /etc/yggdrasil.conf /etc/yggdrasil.conf
```
```
Opening input config...
Input config loaded, updating config...
Config updated, saving...
Config saved, reloading yggdrasil...
Done.
```

### Выходные значения конфигов:
```/etc/yggdrasil.conf```:
```json
{
    "Listen": [
        "tcp://x.x.x.x:y"
    ],
    "NodeInfo": {
        "contanct": {
            "bitmessage": "BM-2cWVVbnxwNDYYuJJcwqD7yk6GSGWqsw1n3",
            "vk": "vk.com/tmsconsole"
        },
        "name": "TomasGlComp",
        "update": "19:55:04MSK"  <---
    },
    "Peers": [
        "tcp://x.x.x.x:y"
    ]
}
```
