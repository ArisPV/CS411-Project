# Import literally everything.
from json_username_token import get_token_and_username
from instagram_json_call import call_instagram_api
import instagram_json_parse
from db import is_user_in_database, get_list_of_img_ids_for, insert_data_for_user, get_use_data, doDBTests
from download_image import download_image
from google_cloud_interface import analyze_file
import json
from instagram_json_parse import read_insta_json


def api_main(access_token_json):
    """ Calls all of like everything.
    """
    print("in api_main()")
    username, access_token = get_token_and_username(access_token_json)
    
    insta_json_data = call_instagram_api(access_token)
    print("got json from instagram")

    img_data_already_in_mongo = [] #existing image ids in database

 #   if not is_user_in_database(username):
    img_data_already_in_mongo = get_list_of_img_ids_for(username)
    print("got existing images from mongo = ", img_data_already_in_mongo)
    
    newImages = read_insta_json(insta_json_data, img_data_already_in_mongo)
    print("got new images from instagram parse")

    doDBTests()
    

    for i in range(len(newImages)):
        print("analyzed image", i+1 , "out of", len(newImages))
        image_url = newImages[i][0]
        image_id = newImages[i][1]

        download_image(image_url, image_id)

        best_Labels_with_scores_dict = analyze_file('app/static/img/' + image_id + '.jpg')
        google_image_output_keys_list = list(best_Labels_with_scores_dict.keys())

        newImages[i].append(google_image_output_keys_list)

    #newImages = [['https://scontent.cdninstagram.com/vp/3126da303828882fbb8185e69c36a0cd/5B860509/t51.2885-15/s640x640/sh0.08/e35/27877886_1573841139401372_4992273558836084736_n.jpg', '1718399401841452012_26740600', '1519069193', True, False, 119, [], 'Normal', 4, True, ['reflection', 'water', 'sky']], ['https://scontent.cdninstagram.com/vp/c5c1eb2ae90353c3250a8c8648e07edb/5B7F1175/t51.2885-15/s640x640/sh0.08/e35/26870642_232339087308579_2356797491896123392_n.jpg', '1703122532305039030_26740600', '1517248048', False, False, 111, ['35mm', 'ae1', 'canon'], 'Normal', 6, False, ['black and white', 'monochrome photography']], ['https://scontent.cdninstagram.com/vp/80eb6c125bd45bb97a144a193daee7bc/5B613D67/t51.2885-15/s640x640/sh0.08/e35/25023858_368231916922787_2008963165928292352_n.jpg', '1678157909973962125_26740600', '1514272033', False, False, 119, ['shotoniphone'], 'Normal', 2, False, ['sky', 'reflection', 'nature', 'water']], ['https://scontent.cdninstagram.com/vp/716b979c55227a0f3d19e1f379d70046/5B7CB7E0/t51.2885-15/s640x640/sh0.08/e35/25021855_1657782670945170_8766642517358673920_n.jpg', '1677558271143219976_26740600', '1514200551', False, False, 121, ['shotoniphone'], 'Normal', 7, False, ['reflection', 'winter', 'waterway', 'water', 'snow', 'body of water']], ['https://scontent.cdninstagram.com/vp/1ffe2dd87b77822a5506374a456d7707/5B97DF4B/t51.2885-15/s640x640/sh0.08/e35/19367116_1059478204196564_7686187968712671232_n.jpg', '1542896990747141900_26740600', '1498147675', False, False, 151, ['shotoniphone', 'miamibeach', 'miamibeachgolfclub'], 'Normal', 7, False, ['tree', 'green', 'nature', 'plant', 'woody plant', 'vegetation']], ['https://scontent.cdninstagram.com/vp/f5003a80e6e2afc5f280258c0fea2bd3/5B9C88C5/t51.2885-15/s640x640/sh0.08/e35/18947797_1504296816296157_5679727016371290112_n.jpg', '1532838463149486048_26740600', '1496948605', False, False, 129, ['boston'], 'Normal', 6, False, ['reflection', 'waterway', 'water', 'sky', 'city', 'river', 'body of water', 'landmark']], ['https://scontent.cdninstagram.com/vp/8dbb865c47cbf451a8605c7fde532f64/5B9B51AC/t51.2885-15/s640x640/sh0.08/e35/18161992_360616351002710_4362679053149274112_n.jpg', '1508168732249594792_26740600', '1494007744', True, False, 104, [], 'Normal', 1, True, ['eye', 'eyebrow']], ['https://scontent.cdninstagram.com/vp/d8b872390364de3b6769024ac3be4d30/5B9B2345/t51.2885-15/s640x640/sh0.08/e35/13712290_284781245232180_1413983204_n.jpg', '1321220513230365572_26740600', '1471721780', False, False, 87, ['boston'], 'Normal', 6, False, ['water', 'white', 'black', 'nature', 'photograph', 'black and white', 'tree', 'monochrome photography']], ['https://scontent.cdninstagram.com/vp/9b332a71839ab887640028306cbe2758/5B9010CC/t51.2885-15/s640x640/sh0.08/e35/13725505_1493273194031947_25634678_n.jpg', '1312435278556487879_26740600', '1470674498', False, False, 91, ['splash', 'photoshoot', 'waterdrop'], 'Normal', 2, False, ['water', 'blue', 'cobalt blue']], ['https://scontent.cdninstagram.com/vp/2534dc269c802d7850fc1cc99f25d888/5B841842/t51.2885-15/s640x640/sh0.08/e35/13735961_1093724904043721_1235817558_n.jpg', '1311507918135099904_26740600', '1470563948', False, False, 81, ['photoshoot'], 'Normal', 12, True, ['blue', 'fashion model']], ['https://scontent.cdninstagram.com/vp/eecd0ffd05dcd7d9c1fe2a5bf51b0a8f/5B79F9A5/t51.2885-15/s640x640/sh0.08/e35/12547225_1551307785196737_1218404529_n.jpg', '1169974598956573809_26740600', '1453691862', True, False, 123, [], 'Normal', 4, False, ['winter', 'snow', 'tree', 'urban area', 'woody plant', 'plant']], ['https://scontent.cdninstagram.com/vp/2e1d3db9437d315b476973a8f0f3ebb6/5B9D194A/t51.2885-15/s640x640/sh0.08/e35/12519292_521748571318226_1308944238_n.jpg', '1158782206517798699_26740600', '1452357625', True, False, 85, [], 'Normal', 0, False, ['sky', 'reflection']], ['https://scontent.cdninstagram.com/vp/4232b8a1606011f8053560c08122200c/5B7903EA/t51.2885-15/s640x640/sh0.08/e35/10560969_151957538508059_1916775288_n.jpg', '1157251978456818763_26740600', '1452175207', True, False, 56, [], 'Normal', 2, False, ['eyebrow', 'blue', 'face', 'eye']], ['https://scontent.cdninstagram.com/vp/1b25eeb3288188b35039f10a36099672/5B95068C/t51.2885-15/s640x640/sh0.08/e35/10518143_1012906835436649_1948734580_n.jpg', '1151278418210939912_26740600', '1451463104', True, False, 41, [], 'Normal', 5, False, ['electronics']], ['https://scontent.cdninstagram.com/vp/9e53bbda0851cb78531ebf68ac582869/5B972E2C/t51.2885-15/e15/11325397_418427228330340_713994641_n.jpg', '1002859353457911641_26740600', '1433770172', False, False, 35, ['macro', 'iphone', 'bluejeans'], 'Normal', 2, False, ['blue']], ['https://scontent.cdninstagram.com/vp/a2b7fcf777a71835924743e92682fb00/5B9BD65B/t51.2885-15/e15/11357805_470007316488728_33191468_n.jpg', '997072005830894911_26740600', '1433080267', True, False, 54, [], 'Normal', 0, False, ['sky', 'sunset', 'sun', 'reflection', 'sunrise']], ['https://scontent.cdninstagram.com/vp/2e26de791f76f59d0e357126c7c25648/5B8D428D/t51.2885-15/e15/11363996_711584408967790_99845854_n.jpg', '993476965774747322_26740600', '1432651704', False, False, 66, ['snowphotoshoot'], 'Normal', 5, False, ['snow', 'motor vehicle']], ['https://scontent.cdninstagram.com/vp/a76fc851d9c703ffdef07c62558be223/5B848D67/t51.2885-15/e15/1742364_796987230380263_1522945280_n.jpg', '946223564255225329_26740600', '1427018660', False, False, 54, ['photoshoot'], 'Normal', 4, True, ['black', 'beauty']], ['https://scontent.cdninstagram.com/vp/a79090a2e982fc20844bc282fe5daf2a/5B83C451/t51.2885-15/e15/11056028_627316920745024_1367364574_n.jpg', '938449510316205715_26740600', '1426091921', True, False, 55, [], 'Normal', 6, True, ['yellow', 'orange']], ['https://scontent.cdninstagram.com/vp/297bd6f58d8f0d4c28114b1f9a7f7f10/5B84D657/t51.2885-15/e15/11032869_1540872912844539_1654825267_n.jpg', '931806476673574425_26740600', '1425300009', False, False, 47, ['d7000', 'nikon'], 'Normal', 10, False, ['flame']]]

    #print(newImages)
    for image in newImages:

        insert_data_for_user(username, image)








    # Get the information from the database using the output_db function.
    # The return values from this would only be the newly updated images that
    # didn't already exist on the database beforehand.
    


    #update_db(username, imgeList)
    #print(imgeList)

    return get_use_data(username)