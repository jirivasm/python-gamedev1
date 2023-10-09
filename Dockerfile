FROM python:latest
WorkDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["pyrhon", "main.py"]