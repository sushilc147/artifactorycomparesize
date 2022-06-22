from artifactory import ArtifactoryPath
import settings

# API Key
path = ArtifactoryPath(f"{settings.URL}/", auth=(settings.USERNAME, settings.PASSWORD))

print(path)

for p in path:
    print(p)
