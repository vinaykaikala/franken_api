Franken Plot  API
=============

- Instal
    --
``` 
    - cd flanken_api
    - python setup.py  install
    - pip install -r requirements.txt
    - pip install .
``` 
 - Run application
    --
```
    - flanken_api -p 8090
```

- Run DB Migration script:

```
sudo docker exec -it probiouidocker_postgress_1 bash
su postgres
psql
CREATE USER referral_writer WITH ENCRYPTED PASSWORD '<password: this should match with password in flask app settings.py>';
CREATE DATABASE referrals;
CREATE DATABASE curation;
GRANT ALL PRIVILEGES ON DATABASE referrals TO referral_writer;
GRANT ALL PRIVILEGES ON DATABASE curation TO referral_writer;
exit

python flanken_api/migrate.py db init --multidb
python flanken_api/migrate.py db migrate
python flanken_api/migrate.py db upgrade
```
