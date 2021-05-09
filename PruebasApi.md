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



# auth


# account