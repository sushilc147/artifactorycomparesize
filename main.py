from artifactory import ArtifactoryPath
import settings
import csv
import json

# API Key
pa_path = ArtifactoryPath(settings.PA_URL, auth=(settings.USERNAME, settings.PASSWORD))
va_path = ArtifactoryPath(settings.VA_URL, auth=(settings.USERNAME, settings.PASSWORD))
print(pa_path)
print(va_path)

# ''items.find({"type":"file"}).sort({"$desc": ["size"]}).limit(100) '
aql_args = [
    'items.find',
    {"type": "file"},
    '.sort',
    {'$desc': ['size']},
    '.limit',
    '100'
]

pa_artifacts = pa_path.aql(*aql_args)
print(pa_artifacts)

va_artifacts = va_path.aql(*aql_args)
print(va_artifacts)

"""
The output is assumed to be in the format below
To test on actual device uncomment codes above
"""
# pa_artifacts = """
# {
#     "storageSummary": {
#         "repositoriesSummaryList": [
#             {
#                 "repoKey": "DATA HERE",
#                 "repoType": "DATA HERE",
#                 "foldersCount": 10,
#                 "filesCount": 2,
#                 "usedSpace": "10 GB",
#                 "itemsCount": 2,
#                 "packageType": "Npm",
#                 "percentage": "0%"
#             },
#             {
#                 "repoKey": "DATA 2 HERE",
#                 "repoType": "DATA 2 HERE",
#                 "foldersCount": 20,
#                 "filesCount": 200,
#                 "usedSpace": "10 GB",
#                 "itemsCount": 220,
#                 "packageType": "Npm",
#                 "percentage": "10%"
#             }
#         ]
#     }
# }
# """
pa_artifacts = json.loads(pa_artifacts)
va_artifacts = json.loads(va_artifacts)
field_names = (
    'repoKey', 'repoType', 'foldersCount', 'filesCount', 'usedSpace', 'itemsCount', 'packageType', 'percentage'
)

with open('pa_output.csv', 'w') as file:
    writer = csv.DictWriter(file, field_names)
    writer.writeheader()
    writer.writerows(pa_artifacts["storageSummary"]["repositoriesSummaryList"])


with open('va_output.csv', 'w') as file:
    writer = csv.DictWriter(file, field_names)
    writer.writeheader()
    writer.writerows(va_artifacts["storageSummary"]["repositoriesSummaryList"])
