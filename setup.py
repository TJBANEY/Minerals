import json

from Minerals.serializers import MineralSerializer

json_data = open('minerals.json').read()

data = json.loads(json_data)

for item in data:
    print(item)
    ms = MineralSerializer(data=item)
    if ms.is_valid():
        ms.save()
