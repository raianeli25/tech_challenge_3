FROM yourstreamlitapp:latest

WORKDIR /usr/src/app

# dont write pyc files
# dont buffer to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r ../app/requirements.txt \
    && rm -rf /root/.cache/pip

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]