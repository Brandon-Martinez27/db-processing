from db_processing.src.db_proc import DbProc
import pytest
import db_processing.env as env

pytest.fixture
def config(self):
    return {
        "dialect": "mysql",
        "driver": "mysqlconnector",
        "host": env.host,
        "port": 3306
    }

pytest.fixture
def creds():
    return {
        "username": env.user,
        "password": env.password
    }

def test_canCreateInstanceOfDbProcClass():
    dbp = DbProc(config, creds)



