FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip setuptools wheel

COPY pyproject.toml ./pyproject.toml
COPY backend ./backend
COPY run.py ./run.py

RUN pip install -e .

EXPOSE 6000

CMD ["python", "run.py"]
