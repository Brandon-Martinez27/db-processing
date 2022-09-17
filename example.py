from db_processing.src.db_proc import DbProc
from db_processing.src.config_provider import ConfigurationProvider

import yaml

# Obtain the 2 configuration files via ConfigurationProvider Utility
config = ConfigurationProvider().configure("db_processing/config/config.yml")
creds = ConfigurationProvider().configure("db_processing/config/creds.yml")

print(f"CONFIG: {config}")
print(f"USER: {creds['username']}")
print(f"PASS: *****")

# Set up Db Processing Class
db_proc = DbProc(config, creds)

print(db_proc)


