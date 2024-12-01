FROM mirror.gcr.io/croncorp/python-ffmpeg:3.10.14-slim-bullseye


SHELL ["/bin/bash", "-c"]


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /zhkh_service
WORKDIR /zhkh_service/

RUN mkdir /zhkh_service/static && mkdir /zhkh_service/media

COPY . .
RUN pip install -r requirements.txt

#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000 --reload"]

#CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "zhkh_service.wsgi:application", "--reload"]