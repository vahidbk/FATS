from codal.Groups import updateGroups
from codal.CodalLinks import updateCodalLetterLinks
from codal.CodalSavePages import updateCodalSavePages
from gold.Gold import updateGoldData
from codal.processCodalData import processCodalDataToGenerateTags
import json
from codal.showTagData import showTagData

#import mofidBroker.easyTraderScraper
#import smsService.Service


#start = input("Please Enter Start Symbol counter:")
#end = input("Please Enter End Symbol counter:")
start = 786
end = 786
#start=end=601
#print(json.dumps(updateGoldData(), indent = 4))
#updateGroups()
#updateCodalLetterLinks(start, end)
updateCodalSavePages(start, end)
#processCodalDataToGenerateTags(start, end)
#showTagData(start, end)


