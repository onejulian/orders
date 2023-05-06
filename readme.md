# Orders

Proyecto escrito en python usando django que permite crear, editar y listar artículos y pedidos

## Guía para configurar el proyecto en fase de desarrollo

1. Clonar este repositorio
2. Pegar en la raíz del proyecto el archivo .env proporcionado vía email
3. Instalar [python](https://www.python.org/downloads/)
4. Instalar virtualenv
```bash
python -m pip install virtualenv
```
5. Iniciar el entorno de paquetes
```bash
python -m virtualenv env
```
6. Si utilizas Visual Studio Code, puede que aparezca el siguiente cuadro en la parte inferior derecha, allí selecciona Yes
![](https://raw.githubusercontent.com/onejulian/storage-fun/main/image.png)
7. Activar el entorno
- Mac - Linux
```bash
 source env/bin/activate
```
- Windows
```bash
 source env/Scripts/activate
```
8. Instalar todos los paquetes necesarios
```bash
 pip install -r requirements.txt
```

> Para levantar el servidor en local

```bash
python src/manage.py runserver
```

> Para desactivar el entorno de paquetes

```bash
 deactivate
```