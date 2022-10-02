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

    def read_data(self, config: dict, sql=None):
        """Reads data by passing a query to SQL Alchemy connection engine
        and returns it as a dictionary

        Parameters
        ----------
            config: dict
                configuration for the sql query to populate select query
                (columns, table, schema, ect.)
            query: str
                Custom query in the case query requires more complexity
        """
        if sql is not None:
            query = sql
        else:
            cols = ",".join(
                (
                    [col for col in config["columns"]]
                )
            )
            table = config["table"]
            limit = config["limit"]
            query = f"SELECT {cols} FROM {table} LIMIT {limit}"

        with self.conn.connect() as conn:

            result = conn.execute(
                query
            ).fetchall()

            d, result_list = {}, []
            for row in result:
                for column, value in row.items():
                    d = {**d, **{column: value}}
                result_list.append(d)

        return result_list