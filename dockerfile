FROM python:3.11.7-slim

WORKDIR /app
COPY . /app
RUN apt-get update -y && apt-get install -y gcc
RUN pip install --no-cache-dir --ignore-installed --no-deps  -r packages.txt

EXPOSE 8501
CMD ['streamlit run app.py']
