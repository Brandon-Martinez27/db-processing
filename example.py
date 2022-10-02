from db_processing.src.db_proc import DbProc
from db_processing.src.config_provider import ConfigurationProvider


# Obtain the 2 configuration files via ConfigurationProvider Utility
config = ConfigurationProvider().configure("db_processing/config/config.yml")
creds = ConfigurationProvider().configure("db_processing/config/creds.yml")

print(f"CONFIG: {config}")
print(f"USER: {creds['username']}")
print(f"PASS: *****")

# Set up Db Processing Class
db_proc = DbProc(config, creds)

print(f"CONN OBJECT: {db_proc} \n")

# Read Data Method
sql_config = ConfigurationProvider().configure("db_processing/config/sql.yml")

read = db_proc.read_data(sql_config)
read2 = db_proc.read_data(None, "SELECT * FROM employees LIMIT 10")

print(f"READ EX1: {read} \n")
print(f"READ EX2: {read2} \n")


