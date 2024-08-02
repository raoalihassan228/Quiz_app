from starlette.config import Config
from datetime import timedelta
try:
    config = Config(".env")

except FileNotFoundError as e:
    print(e)

db_url = config("DB_URL")
test_db_url = config("TEST_DB_URL")

access_expiry_time = timedelta(minutes=int(config.get("ACCESS_EXPIRY_TIME")))
refresh_expiry_time = timedelta(days=int(config.get("REFRESH_EXPIRY_TIME")))
sec_key = config.get("SECRET_KEY")
algorithm = config.get("ALGORITHM")