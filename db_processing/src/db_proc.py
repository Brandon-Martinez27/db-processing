""" Database Processing main script """
import sqlalchemy as sa
from urllib.parse import quote_plus as urlquote

class DbProc:
    """The DbProc Class is used for read and write operations against a database"""

    def __init__(self, config: dict, creds: dict):
        """
        Creates SQL Alchemy connection engine object.

        Parameters
        ----------
            config: dict
                configuration for database connection string
            creds: dict
                username and password
        """

        self.conn = sa.create_engine(
            "{dialect}+{driver}://{username}:%s@{host}:{port}/{database}".format(
                dialect = config["dialect"],
                driver = config["driver"],
                host = config["host"],
                port = config["port"],
                database = config["database"],
                username=creds["username"],
                password = creds["password"]
            )
            % urlquote(creds["password"])
        )

        print(self.conn)
