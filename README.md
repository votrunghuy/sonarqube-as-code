############
Installation
############

``python-sonarqube-api`` is compatible with Python 2.7 and 3.4+.

Use :command:`pip` to install the latest stable version of ``python-sonarqube-api``:

   $ sudo pip install --upgrade python-sonarqube-api
   
############
Usage
############

ADD config to file quality-gates.yaml 

list-quality-gates:
  - qlg1:
      - metric:
          - underscore: 80
          - lowercase: 50
  - qlg2:
      - metric:
          - underscore: 80
          - lowercase: 50
  - qlg3:
      - metric:
          - underscore: 80
          - lowercase: 50
  - Sonar way:
      - metric:
          - underscore: 80
          - lowercase: 50