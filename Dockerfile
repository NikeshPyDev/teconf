FROM python:3.5.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /teconf_project
WORKDIR /teconf_project
ADD . /teconf_project/
RUN python3 -m venv /venv_doc
RUN /venv_doc/bin/pip install -U pip
RUN /venv_doc/bin/pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
