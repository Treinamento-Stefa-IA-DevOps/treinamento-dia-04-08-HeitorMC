#Imagem
FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install pandas fastapi sklearn uvicorn[standard]

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]