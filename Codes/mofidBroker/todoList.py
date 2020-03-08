
#RoadMap 13981125: خرید در ابتدای صبح در ابتدای صف
#RoadMap 13981126: استخراج سهام های پایدار با کمک بالاتر از بازار
#RoadMap 13981215: استخراج اطلاعات بنیادی

#TODO 13981215 پرکردن فیلد های خرید و فروش خودکار
#TODO 13981215 ذخیره اطلاعات مربوط به خرید و فروش های روز براس وضعیت گرارش ایزی تریدر
#TODO 13951215 یافتن نفر جلوتر در صف خرید و فروش
#TODO 13981215 خودکار سازی فرآیند خرید با قیمت مشخص در زمان مشخص
#TODO 13981215 تولید فایل اجرایی
#TODO create Ui for easy Trader and buy and sell
#TODO 13981209 اتصال پیامک به بازار ارز و طلا
#TODO مفید تریدر در ساعت خاص تست شود برای بازار طلای زر
#TODO اتصال پیامک به خرید و فروش

#TODO Extract letter type for data extraction from codal
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



#todo EasyTrader download https://pypi.org/project/selenium-wire/
# Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
#todo EasyTrader localStorageOfChrome:Stocks
#     https://stackoverflow.com/questions/46361494/how-to-get-the-localstorage-with-python-and-selenium-webdriver
#     ...
      # driver.execute_script("window.localStorage;")
#todo EasyTrader getRemain
#     Request URL: https://d11.emofid.com/easy/api/Money/GetRemain
#     Request Method: GET
#     Status Code: 200 OK
#        {"realBalance":5523736.0,"blockedBalance":0.0,"accountBalance":5523736.0}
#todo EasyTrader getTseIndex
#     Request URL: https://d11.emofid.com/easy/api/MarketData/GetTseIndex
#     Request Method: GET
#     Status Code: 200 OK
#         [{"dayOfEvent":"2020-01-28T18:32:00","indexChanges":308.560547,"lastIndexValue":17588.26,"symbolISIN":"IRX6XS300006","percentVariation":1.7856791,"symbolTitle":"شاخص 30 شركت بزرگ"},{"dayOfEvent":"2020-01-28T18:32:00","indexChanges":249.680664,"lastIndexValue":15960.15,"symbolISIN":"IRX6XSLC0006","percentVariation":1.58925867,"symbolTitle":"شاخص50شركت فعالتر"},{"dayOfEvent":"2020-01-28T18:32:01","indexChanges":5272.84375,"lastIndexValue":382257.9,"symbolISIN":"IRX6XSNT0006","percentVariation":1.39868939,"symbolTitle":"شاخص صنعت"},{"dayOfEvent":"2020-01-28T18:32:00","indexChanges":6471.28125,"lastIndexValue":427139.4,"symbolISIN":"IRX6XTPI0006","percentVariation":1.53833628,"symbolTitle":"شاخص كل"},{"dayOfEvent":"2020-01-28T18:32:00","indexChanges":1151.89063,"lastIndexValue":93369.82,"symbolISIN":"IRXYXTPI0026","percentVariation":1.24909544,"symbolTitle":"شاخص قيمت (هم وزن)"},{"dayOfEvent":"2020-01-28T19:42:18","indexChanges":81.36035,"lastIndexValue":5404.45,"symbolISIN":"IRXZXOCI0006","percentVariation":1.52843559,"symbolTitle":"شاخص كل فرابورس"}]
#todo EasyTrader symbolInfo
#     Request URL: https://d11.emofid.com/easy/api/MarketData/GetSymbolDetailsData/IRO1BDAN0001/SymbolInfo
#     Request Method: GET
#     Status Code: 200 OK        
#        {"symbolISIN":"IRO1BDAN0001","totalNumberOfTrades":5919,"totalTradeValue":239582752984.0,"firstTradedPrice":8499.0,"tradeDate":"1398/11/08 12:30:00","marketUnit":"سهام بورس","basisVolume":600000.0,"eps":416.8127,"pe":19.1885,"e30":0.0482,"lastTradedPrice":7998,"tradeDateTime":"2020-01-28T12:30:00","cancelNav":null,"cancelNavDate":"","fYear":"1399/01/02","floatPercent":0.3,"volume90Avg":14011464.1,"maxPercentChange":5,"gpe":19.124,"closingPrice":8146,"highPrice":8499.0,"lowPrice":7900.0}
#todo EasyTrader header
#     Request URL: https://d11.emofid.com/easy/api/MarketData/GetSymbolDetailsData/IRO1BDAN0001/header
#     Request Method: GET
#     Status Code: 200 OK        
#         {"symbolISIN":"IRO1BDAN0001","firstSymbolState":1,"secondSymbolState":0,"lastTradedPrice":7998,"closingPrice":8146,"priceVar":-1.77,"closingPriceVar":0.05,"totalNumberOfSharesTraded":29411251,"symbolFa":"دانا1","companyName":"بیمه دانا","priceChange":-144}
#todo EasyTrader marketDepth
#     Request URL: https://d11.emofid.com/easy/api/MarketData/GetSymbolDetailsData/IRO1BDAN0001/marketDepth
#     Request Method: GET
#     Status Code: 200 OK
#         {"lastTradedPrice":7998,"symbolISIN":"IRO1BDAN0001","closingPrice":8146,"highAllowedprice":8549,"lowAllowedPrice":7735,"priceVar":-1.77,"closingPriceVar":0.05,"highPrice":8499.0,"lowPrice":7900.0,"referencePrice":8142.0,"totalTradeValue":239582752984.0,"queues":[{"bestBuyPrice":7990,"bestSellPrice":8030,"bestSellQuantity":3500,"bestBuyQuantity":183807,"noBestBuy":4,"noBestSell":1},{"bestBuyPrice":7989,"bestSellPrice":8039,"bestSellQuantity":360,"bestBuyQuantity":3501,"noBestBuy":2,"noBestSell":1},{"bestBuyPrice":7980,"bestSellPrice":8040,"bestSellQuantity":6136,"bestBuyQuantity":150,"noBestBuy":1,"noBestSell":1},{"bestBuyPrice":7971,"bestSellPrice":8049,"bestSellQuantity":10000,"bestBuyQuantity":1372,"noBestBuy":2,"noBestSell":1},{"bestBuyPrice":7970,"bestSellPrice":8050,"bestSellQuantity":13700,"bestBuyQuantity":5176,"noBestBuy":4,"noBestSell":2}]}
#todo EasyTrader returnChart
#     Request URL: https://d11.emofid.com/easy/api/MarketData/GetSymbolDetailsData/IRO1BDAN0001/returnChart
#     Request Method: GET
#     Status Code: 200 OK
#         {"e30":0.0482,"e90":0.4241,"e360":2.8158,"maturityDay":"0001-01-01T00:00:00","daysToMaturity":0,"returnToMaturity":null,"lastPrice":null}
#todo EasyTrader IndInstTrade
#     Request URL: https://d11.emofid.com/easy/api/MarketData/GetSymbolDetailsData/IRO1BDAN0001/IndInstTrade
#     Request Method: GET
#     Status Code: 200 OK
#         {"symbolISIN":"IRO1BDAN0001","indBuyVolume":25041103.0,"indBuyNumber":1915.0,"indSellVolume":28585807.0,"indSellNumber":1694.0,"insBuyVolume":4370148.0,"insBuyNumber":9.0,"insSellVolume":825444.0,"insSellNumber":5.0,"date":"2020-01-29T00:00:00"}
#todo EasyTrader portfoilo
#     Request URL: https://d11.emofid.com/easy/api/portfolio
#     Request Method: GET
#     Status Code: 200 OK
#         {"items":[{"quantity":300,"isin":"iro1kvir0001","totalQuantityBuy":0,"totalQuantitySell":0,"newBuy":0,"newSell":0,"lastTradedPrice":null,"priceVar":null,"firstSymbolState":null,"symbol":"کویر1","marketUnit":"Exchange","id":"2d821bef-c543-44fb-afa4-6dbe59ea8131","creationDateTime":"2020-01-29T19:00:53.956678+03:30"},{"quantity":11255,"isin":"iro1sshr0001","totalQuantityBuy":0,"totalQuantitySell":0,"newBuy":0,"newSell":0,"lastTradedPrice":null,"priceVar":null,"firstSymbolState":null,"symbol":"سشرق1","marketUnit":"Exchange","id":"a800a5ca-eb89-4dab-9784-3d092295f3e4","creationDateTime":"2020-01-29T19:00:53.9566868+03:30"}],"itemsHash":null,"id":"95089764-5c82-4948-86ce-fbac9b9c84c8","creationDateTime":"2020-01-29T19:00:53.9566919+03:30"}
#todo EasyTrader GetAuth        
#     Request URL: https://d11.emofid.com/easy/api/auth/GetAuth
#     Request Method: GET
#     Status Code: 200 OK
#         {"userName":"mfdonline2632563","lsToken":"&A1PkF2QEJnLUjcd1jyKOfvtOkaZpVMNCX9ULz+Q203b37V+zmj7bnqAXt2pKF3dtgWTIpD6gcWWvi/VOk6Rswg=="} 

#todo EasyTrader Request URL: 
#     https://d11.emofid.com/easy/api/CandleChart/GetTodayTrend/IRO1SORB0001        
#         {"chartDataItem":[],"id":"2e72fb26-20d8-4696-a9a0-5b1d58289d75","creationDateTime":"2020-01-29T20:00:35.2928725+03:30"}
#     https://d11.emofid.com/easy/api/SymbolChart/GetWeeklyTrend/IRO1SORB0001    
#         {"chartDataItem":[{"d":"1398/11/02","v":32770},{"d":"1398/11/05","v":32930},{"d":"1398/11/06","v":31738},{"d":"1398/11/07","v":31101},{"d":"1398/11/08","v":32410}],"id":"33a7007a-b9b6-437b-bb6a-e8ee513e5bd9","creationDateTime":"2020-01-29T18:43:36.6234663+03:30"}
#     https://d11.emofid.com/easy/api/SymbolChart/GetMonthTrend/IRO1SORB0001
#         {"chartDataItem":[{"d":"1398/11/02","v":32770},{"d":"1398/11/05","v":32930},{"d":"1398/11/06","v":31738},{"d":"1398/11/07","v":31101},{"d":"1398/11/08","v":32410}],"id":"33a7007a-b9b6-437b-bb6a-e8ee513e5bd9","creationDateTime":"2020-01-29T18:43:36.6234663+03:30"}
#     https://d11.emofid.com/easy/api/SymbolChart/Get3MonthsTrend/IRO1SORB0001
#         {"chartDataItem":[{"d":"1398/08/08","v":26063},{"d":"1398/08/11","v":26440},{"d":"1398/08/12","v":25802},{"d":"1398/08/13","v":24998},{"d":"1398/08/14","v":24543},{"d":"1398/08/18","v":25069},{"d":"1398/08/19","v":24281},{"d":"1398/08/20","v":24454},{"d":"1398/08/21","v":24387},{"d":"1398/08/22","v":24344},{"d":"1398/08/25","v":23978},{"d":"1398/08/26","v":22784},{"d":"1398/08/27","v":23480},{"d":"1398/08/28","v":24095},{"d":"1398/08/29","v":23943},{"d":"1398/08/29","v":23943},{"d":"1398/09/02","v":23669},{"d":"1398/09/03","v":23806},{"d":"1398/09/04","v":24093},{"d":"1398/09/05","v":25297},{"d":"1398/09/06","v":26488},{"d":"1398/09/09","v":26784},{"d":"1398/09/10","v":26476},{"d":"1398/09/11","v":26053},{"d":"1398/09/12","v":26820},{"d":"1398/09/13","v":27178},{"d":"1398/09/16","v":28492},{"d":"1398/09/17","v":29184},{"d":"1398/09/18","v":28253},{"d":"1398/09/19","v":27683},{"d":"1398/09/20","v":26845},{"d":"1398/09/23","v":27952},{"d":"1398/09/24","v":28265},{"d":"1398/09/25","v":27384},{"d":"1398/09/26","v":26853},{"d":"1398/09/27","v":26281},{"d":"1398/09/30","v":26950},{"d":"1398/10/01","v":27007},{"d":"1398/10/02","v":27017},{"d":"1398/10/03","v":26287},{"d":"1398/10/04","v":26270},{"d":"1398/10/07","v":27395},{"d":"1398/10/08","v":28634},{"d":"1398/10/09","v":29082},{"d":"1398/10/10","v":28388},{"d":"1398/10/11","v":29633},{"d":"1398/10/14","v":28881},{"d":"1398/10/15","v":27437},{"d":"1398/10/17","v":26124},{"d":"1398/10/18","v":25602},{"d":"1398/10/21","v":26114},{"d":"1398/10/22","v":26697},{"d":"1398/10/23","v":27707},{"d":"1398/10/24","v":29041},{"d":"1398/10/25","v":30129},{"d":"1398/10/28","v":31635},{"d":"1398/10/29","v":31845},{"d":"1398/10/30","v":32018},{"d":"1398/11/01","v":31589},{"d":"1398/11/02","v":32770},{"d":"1398/11/05","v":32930},{"d":"1398/11/06","v":31738},{"d":"1398/11/07","v":31101},{"d":"1398/11/08","v":32410}],"id":"9db47062-c088-4035-818b-ebc2eb4f836c","creationDateTime":"2020-01-29T18:45:00.976554+03:30"}
#     https://d11.emofid.com/easy/api/SymbolChart/GetYearTrend/IRO1SORB0001
#         {"chartDataItem":[{"d":"1397/11/09","v":5231},{"d":"1397/11/10","v":5216},{"d":"1397/11/13","v":5445},{"d":"1397/11/14","v":5691},{"d":"1397/11/15","v":5659},{"d":"1397/11/16","v":5888},{"d":"1397/11/17","v":5791},{"d":"1397/11/21","v":5629},{"d":"1397/11/23","v":5564},{"d":"1397/11/24","v":5650},{"d":"1397/11/27","v":5789},{"d":"1397/11/28","v":5603},{"d":"1397/11/29","v":5637},{"d":"1397/11/30","v":5612},{"d":"1397/12/01","v":5678},{"d":"1397/12/04","v":5719},{"d":"1397/12/05","v":5548},{"d":"1397/12/06","v":5822},{"d":"1397/12/07","v":6003},{"d":"1397/12/08","v":5923},{"d":"1397/12/11","v":5809},{"d":"1397/12/12","v":5680},{"d":"1397/12/13","v":5720},{"d":"1397/12/14","v":5534},{"d":"1397/12/15","v":5584},{"d":"1397/12/18","v":5656},{"d":"1397/12/19","v":5884},{"d":"1397/12/20","v":5968},{"d":"1397/12/21","v":5855},{"d":"1397/12/22","v":6047},{"d":"1397/12/25","v":6189},{"d":"1397/12/26","v":6369},{"d":"1397/12/27","v":6677},{"d":"1397/12/28","v":6582},{"d":"1398/01/05","v":6663},{"d":"1398/01/06","v":6775},{"d":"1398/01/07","v":6939},{"d":"1398/01/10","v":7278},{"d":"1398/01/11","v":7290},{"d":"1398/01/17","v":7230},{"d":"1398/01/18","v":7430},{"d":"1398/01/19","v":7710},{"d":"1398/01/20","v":8076},{"d":"1398/01/21","v":8462},{"d":"1398/01/24","v":8292},{"d":"1398/01/25","v":8315},{"d":"1398/01/26","v":8708},{"d":"1398/01/27","v":8488},{"d":"1398/01/28","v":8437},{"d":"1398/01/31","v":8796},{"d":"1398/02/02","v":8915},{"d":"1398/02/03","v":8962},{"d":"1398/02/04","v":8582},{"d":"1398/02/07","v":8253},{"d":"1398/02/08","v":8650},{"d":"1398/02/09","v":9074},{"d":"1398/02/10","v":9470},{"d":"1398/02/11","v":9860},{"d":"1398/02/14","v":10206},{"d":"1398/02/15","v":9757},{"d":"1398/02/16","v":9273},{"d":"1398/02/17","v":8828},{"d":"1398/02/18","v":9087},{"d":"1398/02/21","v":8961},{"d":"1398/02/22","v":8664},{"d":"1398/02/23","v":9097},{"d":"1398/02/24","v":9551},{"d":"1398/02/25","v":10028},{"d":"1398/02/28","v":10529},{"d":"1398/02/29","v":11051},{"d":"1398/02/30","v":10525},{"d":"1398/03/05","v":12109},{"d":"1398/03/07","v":12648},{"d":"1398/03/08","v":13280},{"d":"1398/03/11","v":13718},{"d":"1398/03/12","v":13912},{"d":"1398/03/13","v":13559},{"d":"1398/03/18","v":14161},{"d":"1398/03/19","v":14411},{"d":"1398/03/20","v":14241},{"d":"1398/03/21","v":14922},{"d":"1398/03/22","v":15664},{"d":"1398/03/25","v":16307},{"d":"1398/03/26","v":17112},{"d":"1398/03/27","v":16913},{"d":"1398/03/28","v":16824},{"d":"1398/03/29","v":16491},{"d":"1398/04/01","v":15667},{"d":"1398/04/02","v":15602},{"d":"1398/04/03","v":16363},{"d":"1398/04/04","v":16976},{"d":"1398/04/05","v":17811},{"d":"1398/04/09","v":18188},{"d":"1398/04/10","v":17448},{"d":"1398/04/11","v":16803},{"d":"1398/04/12","v":16469},{"d":"1398/04/15","v":15701},{"d":"1398/04/16","v":15875},{"d":"1398/04/17","v":15751},{"d":"1398/04/18","v":16416},{"d":"1398/04/19","v":16940},{"d":"1398/04/22","v":17525},{"d":"1398/04/23","v":18338},{"d":"1398/04/24","v":18203},{"d":"1398/04/25","v":17319},{"d":"1398/04/26","v":17412},{"d":"1398/04/29","v":17521},{"d":"1398/04/30","v":17305},{"d":"1398/04/31","v":17630},{"d":"1398/05/01","v":17712},{"d":"1398/05/02","v":17759},{"d":"1398/05/05","v":17073},{"d":"1398/05/06","v":16272},{"d":"1398/05/07","v":16478},{"d":"1398/05/08","v":16527},{"d":"1398/05/09","v":16481},{"d":"1398/05/12","v":17012},{"d":"1398/05/13","v":17862},{"d":"1398/05/14","v":18755},{"d":"1398/05/15","v":19692},{"d":"1398/05/16","v":20470},{"d":"1398/05/19","v":20978},{"d":"1398/05/20","v":20090},{"d":"1398/05/22","v":21035},{"d":"1398/05/23","v":21902},{"d":"1398/05/26","v":22958},{"d":"1398/05/27","v":23992},{"d":"1398/05/28","v":24992},{"d":"1398/06/02","v":26472},{"d":"1398/06/03","v":25791},{"d":"1398/06/04","v":27079},{"d":"1398/06/05","v":28261},{"d":"1398/06/06","v":26988},{"d":"1398/06/09","v":26543},{"d":"1398/06/10","v":25271},{"d":"1398/06/11","v":24604},{"d":"1398/06/12","v":25490},{"d":"1398/06/13","v":25962},{"d":"1398/06/16","v":26602},{"d":"1398/06/17","v":27325},{"d":"1398/06/20","v":26197},{"d":"1398/06/23","v":25118},{"d":"1398/06/24","v":24912},{"d":"1398/06/25","v":25181},{"d":"1398/06/26","v":24163},{"d":"1398/06/27","v":25179},{"d":"1398/06/30","v":26419},{"d":"1398/06/31","v":27345},{"d":"1398/07/01","v":27607},{"d":"1398/07/02","v":26431},{"d":"1398/07/03","v":25858},{"d":"1398/07/06","v":26555},{"d":"1398/07/07","v":26158},{"d":"1398/07/08","v":26955},{"d":"1398/07/09","v":25977},{"d":"1398/07/10","v":25118},{"d":"1398/07/13","v":25166},{"d":"1398/07/14","v":25752},{"d":"1398/07/15","v":26994},{"d":"1398/07/16","v":26151},{"d":"1398/07/17","v":25672},{"d":"1398/07/20","v":26853},{"d":"1398/07/22","v":26418},{"d":"1398/07/23","v":25995},{"d":"1398/07/24","v":24762},{"d":"1398/07/28","v":23943},{"d":"1398/07/29","v":22889},{"d":"1398/07/30","v":23947},{"d":"1398/08/01","v":22852},{"d":"1398/08/04","v":23827},{"d":"1398/08/06","v":24969},{"d":"1398/08/08","v":26063},{"d":"1398/08/11","v":26440},{"d":"1398/08/12","v":25802},{"d":"1398/08/13","v":24998},{"d":"1398/08/14","v":24543},{"d":"1398/08/18","v":25069},{"d":"1398/08/19","v":24281},{"d":"1398/08/20","v":24454},{"d":"1398/08/21","v":24387},{"d":"1398/08/22","v":24344},{"d":"1398/08/25","v":23978},{"d":"1398/08/26","v":22784},{"d":"1398/08/27","v":23480},{"d":"1398/08/28","v":24095},{"d":"1398/08/29","v":23943},{"d":"1398/08/29","v":23943},{"d":"1398/09/02","v":23669},{"d":"1398/09/03","v":23806},{"d":"1398/09/04","v":24093},{"d":"1398/09/05","v":25297},{"d":"1398/09/06","v":26488},{"d":"1398/09/09","v":26784},{"d":"1398/09/10","v":26476},{"d":"1398/09/11","v":26053},{"d":"1398/09/12","v":26820},{"d":"1398/09/13","v":27178},{"d":"1398/09/16","v":28492},{"d":"1398/09/17","v":29184},{"d":"1398/09/18","v":28253},{"d":"1398/09/19","v":27683},{"d":"1398/09/20","v":26845},{"d":"1398/09/23","v":27952},{"d":"1398/09/24","v":28265},{"d":"1398/09/25","v":27384},{"d":"1398/09/26","v":26853},{"d":"1398/09/27","v":26281},{"d":"1398/09/30","v":26950},{"d":"1398/10/01","v":27007},{"d":"1398/10/02","v":27017},{"d":"1398/10/03","v":26287},{"d":"1398/10/04","v":26270},{"d":"1398/10/07","v":27395},{"d":"1398/10/08","v":28634},{"d":"1398/10/09","v":29082},{"d":"1398/10/10","v":28388},{"d":"1398/10/11","v":29633},{"d":"1398/10/14","v":28881},{"d":"1398/10/15","v":27437},{"d":"1398/10/17","v":26124},{"d":"1398/10/18","v":25602},{"d":"1398/10/21","v":26114},{"d":"1398/10/22","v":26697},{"d":"1398/10/23","v":27707},{"d":"1398/10/24","v":29041},{"d":"1398/10/25","v":30129},{"d":"1398/10/28","v":31635},{"d":"1398/10/29","v":31845},{"d":"1398/10/30","v":32018},{"d":"1398/11/01","v":31589},{"d":"1398/11/02","v":32770},{"d":"1398/11/05","v":32930},{"d":"1398/11/06","v":31738},{"d":"1398/11/07","v":31101},{"d":"1398/11/08","v":32410}],"id":"7376ed62-d2c3-4bde-b58a-07245701ce93","creationDateTime":"2020-01-29T18:42:50.962114+03:30"}

#todo EasyTrader buy
#     https://d11.emofid.com/easy/api/OmsOrder
#         1. isin: "IRO1SORB0001"
#         2. financeId: 1
#         3. quantity: 5000
#         4. price: 32656
#         5. side: 1
#         6. validityType: 74
#         7. validityDateJalali: "1398/11/9"
#         8. easySource: 1
#         9. referenceKey: "538bf269-9772-4939-a610-8a0a14dc94a6"

#     response:
#         1. isSuccessfull: true
#         2. message: ""
#         3. omsOrderId: 0
#         4. orderEntryDate: "2020-01-29T20:23:44.4274191+03:30"
#         5. orderEntryDateJalali: "1398/11/09 20:23"
#         6. omsErrorDescription: null


#todo EasyTrader sell
#     https://d11.emofid.com/easy/api/OmsOrder
#         1. isin: "IRO1SORB0001"
#         2. financeId: 1
#         3. quantity: 10000
#         4. price: 32656
#         5. side: 0
#         6. validityType: 74
#         7. validityDateJalali: "1398/11/9"
#         8. easySource: 1
#         9. referenceKey: "79a7d917-cfca-497d-a5fd-5aaddd7ce070"

#     response:
#         1. isSuccessfull: true
#         2. message: ""
#         3. omsOrderId: 0
#         4. orderEntryDate: "2020-01-29T22:35:14.6562724+03:30"
#         5. orderEntryDateJalali: "1398/11/09 22:35"
#         6. omsErrorDescription: null
