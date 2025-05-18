# Documento Entrega 

La solución para crear la aplicación del Backend End se desarrollo con los principios SOLID, Clean Arqhitecture, Clean Code, Design Patterns y se utilizaron los lenguajes de programación y tecnologías correspondientes en el apartadoo de **Technology**:

# Technology

  - Python
  - FastAPI

# Install Depedendecies

  - python -m venv .venv
  - pip install "fastapi[standard]"
  - pip install google-cloud-firestore
  - uvicorn app.main:app

# Paths Executable

  - GET http://locahost:8080/use-firebase/tasks
  - POST http://locahost:8080/use-firebase/tasks
  - UDPATE http://locahost:8080/use-firebase/tasks/:id
  - DELETE http://locahost:8080/use-firebase/tasks/:id