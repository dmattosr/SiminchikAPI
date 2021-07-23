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


## GET

/location/country/1

# state

## POST

{
  "country_id": 1,
  "name": "LIMA",
  "state_code": "01"
}


## GET
/location/state/1


# city

## POST

{
  "state_id": 1,
  "name": "LIMA CERCADO",
  "latitude": "-12.0453",
  "longitude": "-77.0311"
}


## GET

/location/city/1

# document

## POST

{
  "name": "DNI",
  "description": "DOCUMENTO NACIONAL DE IDENTIDAD"
}


## GET

/document/1



# language

## POST

{
  "name": "ESPAÑOL",
  "iso3": "esp"
}


## GET

/language/1


# dialect

## POST

{
  "language_id": 1,
  "name": "CASTELLANO"
}

## GET


/dialect/1






user






https://github.com/Siminchik/NER_Quechua 
