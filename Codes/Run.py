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

#TODO Extract Valid Group
#TODO Extract Hala Companies
#TODO Extract list of key value in SoratHayeMali
#TODO Extract List Of All Valid information in 'list of key value in SoratHayeMali'
#TODO Extract data And deserialize htmls 'list of key value in SoratHayeMali'
#TODO gozaresh mahiane save page
#TODO Extract gozaresh mahiane
#TODO Namayesh Nemodary with ui
#TODO EXTract Group and sod-dehi saliane
#TODO catch To Zip

#TODO استخراج حجم معملات هر سهم
#TODO استخراج قیمت هر سهم در روز
#TODO استخراج روزهای بدون معامله
#TODO اسخراج رتبه در معاملات صنعت
#TODO مقایسه حجم معاملات با دیگر شرکتهای هم صنعت
#TODO مقایسه روزهای معامله در صنعت
#TODO استخراج حقیق و حقوقی و پول هوشمند

#TODO خرید و فروش خودکار
#TODO مفید تریدر در ساعت خاص تست شود برای بازار طلای زر
#TODO اتصال پیامکبه خرید و فروش


