# S.O
FROM alpine:3.10
# Python installation
RUN apk add --no-cache python3-dev build-base libffi-dev && apk add --no-cache py3-pip
# Workspace
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
CMD ["python3", "src/app.py"]
# docker run -p 3000:3000 app-info
