from email.policy import default
from decouple import config

USERNAME = config("ARTIFACTORY_USERNAME", cast=str)
PASSWORD = config("ARTIFACTORY_PASSWORD", cast=str)

PA_URL = config("ARTIFACTORY_URL_PA", default="https://artifactory.hrzon.as.bankof.com/artifactory", cast=str)
VA_URL = config("ARTIFACTORY_URL_VA", default="https://artifactory.hrzon.as.bankof.com/artifactory", cast=str)
