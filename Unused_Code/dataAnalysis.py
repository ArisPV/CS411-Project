from collections import Counter
import datetime
import numpy as np

def goForItBaby():
    images = [['https://scontent.cdninstagram.com/vp/cd06264d57cc07d245cdd63234ff923c/5B5E7809/t51.2885-15/s640x640/sh0.08/e35/27877886_1573841139401372_4992273558836084736_n.jpg', '1718399401841452012_26740600', '1519069193', True, False, 118, [], 'Normal', 4, True], ['https://scontent.cdninstagram.com/vp/c5c1eb2ae90353c3250a8c8648e07edb/5B7F1175/t51.2885-15/s640x640/sh0.08/e35/26870642_232339087308579_2356797491896123392_n.jpg', '1703122532305039030_26740600', '1517248048', False, False, 111, ['35mm', 'canon', 'ae1'], 'Normal', 6, False], ['https://scontent.cdninstagram.com/vp/80eb6c125bd45bb97a144a193daee7bc/5B613D67/t51.2885-15/s640x640/sh0.08/e35/25023858_368231916922787_2008963165928292352_n.jpg', '1678157909973962125_26740600', '1514272033', False, False, 119, ['shotoniphone'], 'Normal', 2, False], ['https://scontent.cdninstagram.com/vp/716b979c55227a0f3d19e1f379d70046/5B7CB7E0/t51.2885-15/s640x640/sh0.08/e35/25021855_1657782670945170_8766642517358673920_n.jpg', '1677558271143219976_26740600', '1514200551', False, False, 121, ['shotoniphone'], 'Normal', 7, False], ['https://scontent.cdninstagram.com/vp/1ffe2dd87b77822a5506374a456d7707/5B97DF4B/t51.2885-15/s640x640/sh0.08/e35/19367116_1059478204196564_7686187968712671232_n.jpg', '1542896990747141900_26740600', '1498147675', False, False, 151, ['shotoniphone', 'miamibeach', 'miamibeachgolfclub'], 'Normal', 7, False], ['https://scontent.cdninstagram.com/vp/f5003a80e6e2afc5f280258c0fea2bd3/5B9C88C5/t51.2885-15/s640x640/sh0.08/e35/18947797_1504296816296157_5679727016371290112_n.jpg', '1532838463149486048_26740600', '1496948605', False, False, 129, ['boston'], 'Normal', 6, False], ['https://scontent.cdninstagram.com/vp/8dbb865c47cbf451a8605c7fde532f64/5B9B51AC/t51.2885-15/s640x640/sh0.08/e35/18161992_360616351002710_4362679053149274112_n.jpg', '1508168732249594792_26740600', '1494007744', True, False, 104, [], 'Normal', 1, True], ['https://scontent.cdninstagram.com/vp/d8b872390364de3b6769024ac3be4d30/5B9B2345/t51.2885-15/s640x640/sh0.08/e35/13712290_284781245232180_1413983204_n.jpg', '1321220513230365572_26740600', '1471721780', False, False, 87, ['boston'], 'Normal', 6, False], ['https://scontent.cdninstagram.com/vp/9b332a71839ab887640028306cbe2758/5B9010CC/t51.2885-15/s640x640/sh0.08/e35/13725505_1493273194031947_25634678_n.jpg', '1312435278556487879_26740600', '1470674498', False, False, 91, ['splash', 'photoshoot', 'waterdrop'], 'Normal', 2, False], ['https://scontent.cdninstagram.com/vp/2534dc269c802d7850fc1cc99f25d888/5B841842/t51.2885-15/s640x640/sh0.08/e35/13735961_1093724904043721_1235817558_n.jpg', '1311507918135099904_26740600', '1470563948', False, False, 81, ['photoshoot'], 'Normal', 12, True], ['https://scontent.cdninstagram.com/vp/eecd0ffd05dcd7d9c1fe2a5bf51b0a8f/5B79F9A5/t51.2885-15/s640x640/sh0.08/e35/12547225_1551307785196737_1218404529_n.jpg', '1169974598956573809_26740600', '1453691862', True, False, 123, [], 'Normal', 4, False], ['https://scontent.cdninstagram.com/vp/2e1d3db9437d315b476973a8f0f3ebb6/5B9D194A/t51.2885-15/s640x640/sh0.08/e35/12519292_521748571318226_1308944238_n.jpg', '1158782206517798699_26740600', '1452357625', True, False, 85, [], 'Normal', 0, False], ['https://scontent.cdninstagram.com/vp/4232b8a1606011f8053560c08122200c/5B7903EA/t51.2885-15/s640x640/sh0.08/e35/10560969_151957538508059_1916775288_n.jpg', '1157251978456818763_26740600', '1452175207', True, False, 56, [], 'Normal', 2, False], ['https://scontent.cdninstagram.com/vp/1b25eeb3288188b35039f10a36099672/5B95068C/t51.2885-15/s640x640/sh0.08/e35/10518143_1012906835436649_1948734580_n.jpg', '1151278418210939912_26740600', '1451463104', True, False, 41, [], 'Normal', 5, False], ['https://scontent.cdninstagram.com/vp/9e53bbda0851cb78531ebf68ac582869/5B972E2C/t51.2885-15/e15/11325397_418427228330340_713994641_n.jpg', '1002859353457911641_26740600', '1433770172', False, False, 35, ['macro', 'bluejeans', 'iphone'], 'Normal', 2, False], ['https://scontent.cdninstagram.com/vp/a2b7fcf777a71835924743e92682fb00/5B9BD65B/t51.2885-15/e15/11357805_470007316488728_33191468_n.jpg', '997072005830894911_26740600', '1433080267', True, False, 54, [], 'Normal', 0, False], ['https://scontent.cdninstagram.com/vp/72555958a37c250825024e3d82ea8150/5B65B58D/t51.2885-15/e15/11363996_711584408967790_99845854_n.jpg', '993476965774747322_26740600', '1432651704', False, False, 66, ['snowphotoshoot'], 'Normal', 5, False], ['https://scontent.cdninstagram.com/vp/ed9a922d44d3b01fe17054885db15cd8/5B5D0067/t51.2885-15/e15/1742364_796987230380263_1522945280_n.jpg', '946223564255225329_26740600', '1427018660', False, False, 54, ['photoshoot'], 'Normal', 4, True], ['https://scontent.cdninstagram.com/vp/a79090a2e982fc20844bc282fe5daf2a/5B83C451/t51.2885-15/e15/11056028_627316920745024_1367364574_n.jpg', '938449510316205715_26740600', '1426091921', True, False, 55, [], 'Normal', 6, True], ['https://scontent.cdninstagram.com/vp/d22b98f2f2cfb18112cafdbee87fa3cf/5B5D4957/t51.2885-15/e15/11032869_1540872912844539_1654825267_n.jpg', '931806476673574425_26740600', '1425300009', False, False, 47, ['d7000', 'nikon'], 'Normal', 10, False]]
    sortedByLikes = sorted(images,key=lambda l:l[6], reverse=True)
    best_hastags = []

    times = []
    for i in range(len(images)):

        date = datetime.datetime.fromtimestamp(int(sortedByLikes[i][2]))
        hour = date.hour
        minute = date.minute
        if minute >= 10: finalTime = hour + 1
        else: finalTime = hour
        times += [finalTime]

    #print(times)


    hist = np.histogram(times, bins=list(range(0, 25)))


    for i in range(len(images)):
        best_hastags += sortedByLikes[i][6]
    best_hastag_counts = Counter(best_hastags)

    #return str(list(hist[0]))

    best_hastag_counts = dict(best_hastag_counts)

    timesHistogramValues = hist[0]
    timesHistogramBins   = hist[1]

    bestTimesIndexes = timesHistogramValues.argsort()[-3:][::-1]
    bestTimesString =   str(timesHistogramBins[bestTimesIndexes[0]]) + " - " + str(timesHistogramBins[bestTimesIndexes[0] + 1]) + ", " + \
                        str(timesHistogramBins[bestTimesIndexes[1]]) + " - " + str(timesHistogramBins[bestTimesIndexes[1] + 1]) + " and "+ \
                        str(timesHistogramBins[bestTimesIndexes[2]]) + " - " + str(timesHistogramBins[bestTimesIndexes[2] + 1]) 
    



    li = [(value,key) for key, value in best_hastag_counts.items()]
    li.sort()
    m = 5
    best5hastags = str([k for v, k in li[-m:]])



    return (best5hastags,bestTimesString) #dictionary with key as hastag and val as number of occurance



