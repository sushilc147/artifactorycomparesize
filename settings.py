from email.policy import default
from decouple import config

USERNAME = config("ARTIFACTORY_USERNAME", cast=str)
PASSWORD = config("ARTIFACTORY_PASSWORD", cast=str)

URL = config("ARTIFACTORY_URL", default="https://artifactory.hrzon.as.bankof.com/artifactory/apisearch/aql", cast=str)
