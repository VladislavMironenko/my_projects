# 3,5 - 37,5
# 4 - 38
# 4,5 - 38,5
# 5 - 39
# 5,5 - 39,5
# 6UK: 7US / 40EU
# 6,5UK: 7,5US / 40,5EU
# 7UK: 8US / 41EU
# 7,5UK: 8,5US / 41,5EU
# 8UK: 9US / 42EU
# 8,5UK: 9,5US / 42,5EU
# 9UK: 10US / 43EU
# 9,5UK: 10,5US / 43,5EU
# 10UK: 11US / 44EU / 30 см
# 10,5UK: 11,5US / 44,5EU
# 11UK: 12US / 45EU
# 11,5UK: 12,5US / 45,5EU
# 12UK: 13US / 46EU
# 13UK: 14US / 47EU
# 14UK: 15US / 48EU
# 15UK: 16US / 49EU
# 16UK: 17US / 50EU
# 17UK: 18US / 51EU
# 18UK: 19US / 52EU
import json
# adidas = []
# megasport = []
adidas = {
    '38' : '4',
    '39' : '5',
    '40': '6',
    '41': '7',
    '42': '8',
    '43': '9',
    '44': '10',
    '45': '11',
    '46': '12',
    '47': '13',
    '48': '14',
    '49': '15',
}

megasport = {
    '35': '22',
    '36': '22.5',
    '36,5': '23',
    '37': '23.5',
    '37,5': '24',
    '38': '24.5',
    '38,5': '25',
    '39': '25.5',
    '40': '26',
    '40,5': '26.5',
    '41': '27',
    '42': '27.5',
    '42,5': '28',
    '43': '28.5',
    '44': '29',
    '44,5': '29.5',
    '45': '30',
    '45,5': '30.5',
    '46': '31',
    '47': '32'
}

puma = {
    '35,5':'35.5',
    '36':'36',
    '37':'37',
    '37,5':'37.5',
    '38':'38',
    '38,5':'38.5',
    '39':'39',
    '40':'40',
    '40,5':'40.5',
    '41':'41',
    '42':'42',
    '42,5':'42.5',
    '43':'43',
    '44':'44',
    '44,5':'44.5',
    '45':'45',
    '46':'46',
    '47':'47'
}
adidas_shorts_tshirts = {
    'XS':'xs',
    'S':'s',
    'M':'m',
    'L':'l',
    'XL':'xl',
    'XXL': 'xxl'
}

puma_shorts_tshirts = {
    'XS':'xs',
    'S':'s',
    'M':'m',
    'L':'l',
    'XL':'xl',
    'XXL': 'xxl'
}
dict = {
   'adidas_sneakers' : adidas,
    'megasport_sneakers' : megasport,
    'puma_sneakers' : puma,
    'adidas_shorts_tshirts': adidas_shorts_tshirts,
    'puma_shorts_tshirts': puma_shorts_tshirts
}
# with open('size.json' , 'w') as f:
#     json.dump(adidas , f , indent=4 , ensure_ascii=False)
with open('size.json' , 'w') as f:
    json.dump(dict , f ,  indent=4 , ensure_ascii=False)
lst = []
# with open('size.json' , 'r') as f:
#     b = json.load(f)
#     a = b['puma_sneakers']
#     print(a)
#     for k,v in a.items():
#         lst.append(str(k))
# print(lst)
