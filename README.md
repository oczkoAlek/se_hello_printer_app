# Simple Flask App

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:

  ```
  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  $ python3 -m venv .venv

  # aktywowanie hermetycznego środowiska
  $ source .venv/bin/activate
  $ make deps


  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```

  # jako zwykły program
  $ make run


  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ make test
  # lub
  $ PYTHONPATH=. py.test

  ```
  lint
  $ make lint
  #albo
  $ flake8 hello_world test

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja
  $ source .venv/bin/activate
  ```

- Integracja z TravisCI:

  ```
  # miejsce na twoje notatki
  # dodanie pliku .travis.yml i zupenienie pliku Makefile
  ```

# Pomocnicze

## Ubuntu

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Heroku

- Dodanie gunicorn

  ```
  #Aktywacja venv
  $ echo 'gunicorn' >> requirements.txt
  $ pip install -r requirements.txt
  ```
- Testowanie dzialania

  ```
  # w jednym oknie terminala
  $ PYTHONPATH=$PYTHONPATH:$(pwd) gunicorn hello_world:app
  # w drugim oknie terminala
  $ curl 127.0.0.1:8000
  ```



- utworzenie pliku Procfile i dodaj linie

  ```
  # web: gunicorn hello_world:app
  ```

- Zainstaluj Heroku CLI, korzystając z instrukcji na stronie:
https://devcenter.heroku.com/articles/heroku-cli


- Odpalanie heroku-cli w terminalu

  ```
  # w jednym oknie terminala
  $ heroku local
  # w drugim oknie terminala
  $ curl 127.0.0.1:5000
  ```

- dodanie konta do statuscacke.com i dodanie tam aplikacji na Heroku


 ## Status do TravisCI

 [![Build Status](https://travis-ci.org/oczkoAlek/se_hello_printer_app.svg?branch=master)](https://travis-ci.org/oczkoAlek/se_hello_printer_app)




 ## Sprawdzenie statusu na statuscake
 
 ![Build Status](https://app.statuscake.com/button/index.php?Track=5902166&Days=1&Design=7)

## Centos

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
