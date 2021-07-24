# SiminchikAPI


Tomado de la fuente de https://github.com/rjzevallos

# Colaboradores

- Solís Carbajal Alejandro Daniel
- Montero Osorio Edwar
- Guillen Mamani Juan Jose
- Mattos Rosales Daniel
- Cahuana Ccallocunto Kevin Edward
- Diaz Rojas, Joao Samel



## Instalación

Ejecutar línea por línea

```bash
sudo apt update

sudo apt install -y python3-pip

git clone https://github.com/dmattosr/SiminchikAPI.git

cd SiminchikAPI

pip3 install -r requirements.txt

```

Nota:

Para usar dentro de Windows 10, seguir las siguientes indicaciones:

Activar la terminal de linux en este [enlace](https://www.neoguias.com/activar-terminal-linux-windows-10), seleccionar `Ubuntu`


## Iniciar SiminchikAPI

```bash
python3 manage.py runserver
```

Luego entrar al enlace http://127.0.0.1:5000


# Pruebas a la API

[link](./PruebasApi.md)


# Servicios agregados


Modelo | Estado
----|-----|-----|-----|-----
Audio Prompt | Verificado
Country | Verificado
State | Verificado
City | Verificado
audio_prompt | Verificado
audio_recorder | Verificado
audio_transcription | Verificado
document | Verificado
Language | Verificado
Dialect | Verificado
text_prompt | Verificado
text_transcription | Verificado


# Docker

Ejecutar

```bash

docker-compose up -s

```


# TODO

- Diccionario de datos
- Modelo de datos
- Pruebas unitarias
- Llaves foraneas y constrains
- Integración con el Speech Recognition App
