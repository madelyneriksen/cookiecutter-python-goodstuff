FROM python:3.6-alpine

WORKDIR /usr/src/{{cookiecutter.package_slug}}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python setup.py install

CMD {{ cookiecutter.package_name }}
