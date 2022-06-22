from artifactory import ArtifactoryPath
import settings

# API Key
path = ArtifactoryPath(f"{settings.URL}/", auth=(settings.USERNAME, settings.PASSWORD))
print(path)

# ''items.find({"type":"file"}).sort({"$desc": ["size"]}).limit(100) '
artifacts = path.aql('items.find', {"type": "file"}, '.sort', {'$desc': ['size']},  '.limit', '100')

# aql_args = [
#     'items.find',{
#
#     }
# ]

print(artifacts)
