FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 8501

CMD ["streamlit", "run", "--server.address", "0.0.0.0", "soccer_stats_app.py"]
