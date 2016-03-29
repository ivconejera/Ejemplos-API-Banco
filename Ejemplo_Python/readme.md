# API Banco - Cliente Python

Firmado de documentos XML, PDF utilizando un cliente Python y el API de firma electrónica.

### Requisitos
- Python 2.7
- [JWT][reference_jwt]

### Configuración

Las configuraciones necesarias para ejecutar el ejemplo se encuentran en el archivo config.py Solo se debería modificar la siguiente sección:

```python
class variables_generales:

    # Config APP     
    SECRET = "abcd"
    APP_CODE = "system"
    # URLS ENDPOINT -- Cambiar por la URL correspondiente al Entry Point con el servicio de firma
    URL = "http://proxy-banco.modernizacion.gob.cl/v1/files/tickets"
```
### Ejecución 

Ejecutar el ejemplo con
```sh
python firmador.py
```

[reference_jwt]: <https://jwt.io/>
