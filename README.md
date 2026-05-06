Ecommerce API

API REST para un ecommerce construida con FastAPI y PostgreSQL.

## Tecnologías

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (autenticación)
- Pydantic

## Instalación

1. Clona el repositorio
git clone https://github.com/JorgePuertasHerrera/ecommerce-api.git
cd ecommerce-api

2. Crea el entorno virtual
python3.11 -m venv venv311
source venv311/bin/activate

3. Instala dependencias
pip install -r requirements.txt

4. Crea el archivo .env
DATABASE_URL=postgresql://usuario:password@localhost:5432/ecommerce_db
SECRET_KEY=tu-clave-secreta

5. Arranca el servidor
python3.11 -m uvicorn app.main:app --reload

## Endpoints

- POST /users/register — Registro de usuario
- POST /users/login — Login y obtención de token JWT
- GET /products — Listar productos
- POST /products — Crear producto (requiere token)
- PUT /products/{id} — Editar producto (requiere token)
- DELETE /products/{id} — Eliminar producto (requiere token)

## Documentación

Disponible en http://localhost:8000/docs
