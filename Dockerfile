FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

RUN pytest tests

ENTRYPOINT [ "gunicorn" ]

CMD ["app:app", "-b", "0.0.0.0:80"]
