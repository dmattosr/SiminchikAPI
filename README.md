# SiminchikAPI


# SiminchikAPI en Windows 10

Activar la terminal de linux en este [enlace](https://www.neoguias.com/activar-terminal-linux-windows-10), seleccionar `Ubuntu`

## Instalación

Ejecutar línea por línea

```bash
sudo apt update

sudo apt install -y python3-pip

git clone https://github.com/dmattosr/SiminchikAPI.git

cd SiminchikAPI

pip3 install -r requirements.txt

```

## Iniciar SiminchikAPI

```bash
python3 manage.py runserver
```

Luego entrar al enlace http://127.0.0.1:5000


# Pruebas a la API

[link](./PruebasApi.md)


# Cambios


Modelo | Service | Dto | Controller
Audio Prompt | Si | Si | Si
Country | Si | Si | Si
State | Si | Si | Si
City | Si | Si | Si
audio_prompt | Si | Si | Si
audio_recorder | Si | Si | Si
audio_transcription | No | No | No
document | No | No | No
language | No | No | No
text_prompt | No | No | No



# Docker

Ejecutar

```bash

docker-compose up -s

```
