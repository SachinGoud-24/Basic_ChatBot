FROM python:3.11.7-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r packages.txt
EXPOSE 8501
CMD ['streamlit run app.py']
