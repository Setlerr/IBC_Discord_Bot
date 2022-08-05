FROM python:3.9
COPY . /app
WORKDIR /app
RUN python3 -m pip install -U nextcord
CMD ["python", "./main.py"]
