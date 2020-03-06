from codal.Groups import updateGroups
from gold.Gold import updateGoldData
import json
import time

print(json.dumps(updateGoldData(), indent = 4))

time.sleep(10)

