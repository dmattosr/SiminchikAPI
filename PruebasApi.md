Pruebas al API
==============


Pruebas a la `API` desde la consola o línea de comandos(bash).

# user
## Creación de usuarios

Método: `Post`
Ruta: `/user/`

Ejemplo 1

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "first_name": "JUAN",
    "last_name": "PEREZ MARTINEZ",
    "type_doc_id": 0,
    "num_doc": "99123456",
    "country_id": 0,
    "state_id": 0,
    "city_id": 0,
    "dialect_id": 0
    }' \
  http://localhost:5000/user/
```

Ejemplo 2
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "first_name": "JAVIER",
    "last_name": "REYES PARDO",
    "type_doc_id": 0,
    "num_doc": "99123457",
    "country_id": 0,
    "state_id": 0,
    "city_id": 0,
    "dialect_id": 0
    }' \
  http://localhost:5000/user/
```


## Lectura de usuarios

Método: `GET`
Ruta: `/user/{user_ud}`

Ejemplo 1

```bash
curl --header "Content-Type: application/json" \
  --request GET \
  http://localhost:5000/user/1
```

`Nota:` cambiar el `1` por el id.(numero identificador) del usuario.


# Audio Prompt

# Creación Audio Prompt

Método: `POST`
Ruta: `/audio_prompt/`

Ejemplo

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
      "text_prompt_id": 1,
      "user_id": 1,
      "name": "ESTE ES UN MENSAJE DE PRUEBA"
    }' \
  http://localhost:5000/audio_prompt/
```

# Lectura Audio Prompt

Método: `GET`
Ruta: `/audio_prompt/1`

Ejemplo

```bash
curl --header "Content-Type: application/json" \
  --request GET \
  http://localhost:5000/audio_prompt/1
```

respuesta

`Nota:` cambiar el `1` por el id.(numero identificador) del usuario.


# auth


# account





PRUEBAS
=========





# country

POST

```json
{
  "name": "PERU",
  "iso3": "PER",
  "iso2": "PE",
  "phone_code": "51",
  "currency": "SOL",
  "native": "string",
  "region": "string",
  "subregion": "string",
  "timezone": "America/Lima"
}
```


## GET

```


/location/country/1
```

# state

## POST

```json
{
  "country_id": 1,
  "name": "LIMA",
  "state_code": "01"
}
```

## GET

```

/location/state/1

```
# city

## POST

```json
{
  "state_id": 1,
  "name": "LIMA CERCADO",
  "latitude": "-12.0453",
  "longitude": "-77.0311"
}
```


## GET


```

/location/city/1

```

# document


```json
## POST

{
  "name": "DNI",
  "description": "DOCUMENTO NACIONAL DE IDENTIDAD"
}
```


## GET

```

/document/1


```


# language

```json
## POST

{
  "name": "ESPAÑOL",
  "iso3": "esp"
}
```


## GET

```

/language/1


```

# dialect

## POST

```json
{
  "language_id": 1,
  "name": "CASTELLANO"
}
```

## GET


```

/dialect/1

```


# user


## POST

```json
{
  "first_name": "PEDRO",
  "last_name": "CASTILLO",
  "type_doc_id": 1,
  "num_doc": "44123123",
  "country_id": 1,
  "state_id": 1,
  "city_id": 1,
  "dialect_id": 1
}
```


## GET

```

/user/1

```

# audio_prompt

## POST


```json
{
  "user_id": 1,
  "name": "NO SE PIERDAN EL KEIKINO"
}
```


## GET

```

/audio_prompt/1

```

# audio_recorder


## POST

```json
{
  "user_id": 1,
  "audio_prompt_id": 1,
  "dialect_id": 1,
  "name": "No se pierdan el KeiKino",
  "quality": 50
}
```

## GET

```

/audio_recorder/1

```

# audio_transcription


## POST


```json
{
  "user_id": 1,
  "dialect_id": 1,
  "name": "Bajen al KeiKino hay lugar para todos",
  "quality": 50
}
```

## GET

```

/audio_transcription/1

```

# text_prompt

## POST

```json
{
  "dialect_id": 1,
  "text": "El Keikino hasta las 6 de la mañana",
  "source": "El Keikino hasta las 6 de la mañana"
}
```



## GET

```

/text_prompt/1

```

# text_transcription


## POST

```json

{
  "audio_transcription_id": 1,
  "source_dialect_id": 1,
  "dest_dialect_id": 1,
  "text_transcription": "Habrá mucha comida y de regalo tapers en el Keikno",
  "quality": 30
}
```


## GET

```

/text_transcription/1

```
