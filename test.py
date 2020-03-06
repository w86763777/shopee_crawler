import requests

url = "https://shopee.tw/api/v2/search_items"
params = {
    "keyword": "藍寶石 rx580",
    "by": "price",
    "limit": "50",
    "newest": "0",
    "price_max": "500",
    "price_min": "300",
    "order": "asc",
    "page_type": "search",
    "version": "2",
}
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.181 Safari/537.36',
    # 'cookie': 'REC_T_ID=484a65c0-e90e-11e9-bd36-b49691377b10; _ga=GA1.2.457121'
    #           '808.1570458317; _fbp=fb.1.1570458316930.1376755124; __BWfp=c157'
    #           '0458336828xfb9d323a3; cto_lwid=668a6d86-e3c6-452c-b326-73535438'
    #           '0499; G_ENABLED_IDPS=google; SPC_F=cIDB7yJUAY78T8w0pwh0VturHGtu'
    #           'zCuj; _gcl_au=1.1.1044091401.1580193698; csrftoken=1fWo3HZSm4a9'
    #           'Lhyekw3IW8wQvhEcpzqi; _fbc=fb.1.1582443259071.IwAR2Y5UT9XGYmvl2'
    #           'wtHm1g55qdhMizS8LPdmX8PPwh_KAOVbRzikaaikcfeE; _gid=GA1.2.437375'
    #           '453.1582443260; _med=refer; welcomePkgShown=true; CTOKEN=QYsmjl'
    #           '3eEeqpRsy7%2Fl4CUg%3D%3D; SPC_IA=-1; SPC_SI=smo6s4ocg4mq1j19d0q'
    #           '4qn8fvgwl4iab; SPC_U=-; SPC_EC=-; AMP_TOKEN=%24NOT_FOUND; SPC_C'
    #           'T_584d9ec3="1583499641.i+r6GxNWnQZ+9Dz6F0r+Blaf3t0MZm97yihIgt+X'
    #           'uGM="; SPC_CT_d764fc0c="1583499650.ZOTKo4xSnfI3KHJbGgtX5n098tt1'
    #           'uGR+w/FkzXhCSx8="; SPC_CT_215dd61c="1583499653.bwHh8lc69CmGNjiu'
    #           'a4ZbnqTGhxmnxuCvLYRnaYhc4Mw="; SPC_CT_5a320433="1583499658.7/+w'
    #           'LK8Ablf6GwdO7Wgphw34V2/3kCE0f/HRDYgc3tA="; SPC_CT_208f1b5b="158'
    #           '3499662.u78MU8U5e56i9Nd5Cv0Co3YfcDrqnkBLG815Um44+cs="; SPC_CT_c'
    #           '0a1802b="1583499669.jRvE1bj567LMMw+TevpUgRYNS19D41ijGPquvB/1Klc'
    #           '\'="; SPC_CT_9297d619="1583499677.tGzkTldfzirc51yBoGyPuNSGbUmk9'
    #           'vOinvMpl/ILWUM="; SPC_CT_e825cee4="1583499684.64oE515e7y6zz5Vh0'
    #           'xPVuSn85dj5THUkGnAlhnRpNyI="; SPC_CT_f7ec8846="1583499690.wzdCV'
    #           'otazf03GcghrMiJuUhld9TIYAfkQOQyjoZpm+A="; REC_MD_20=1583499771;'
    #           ' SPC_CT_c3f879a3="1583499763.ZBpjOQkcPhoUmLef+dDD/P71OCjO8pFHcR'
    #           'BFTz++eJE="; SPC_R_T_ID="w6HU0NTBsjmvTq83Md7yRAW+JEDXK2R3Daqxga'
    #           'xarqgl6EjPW4MdVCRk9TFP+JlXKvrWtiwzECBkqadhFTRjkTQBwEkggpgmXp1ul'
    #           '9AnrHQ="; SPC_T_IV="7q8C95H8IF8sauT+10djJQ=="; SPC_R_T_IV="7q8C'
    #           '95H8IF8sauT+10djJQ=="; SPC_T_ID="w6HU0NTBsjmvTq83Md7yRAW+JEDXK2'
    #           'R3Daqxgaxarqgl6EjPW4MdVCRk9TFP+JlXKvrWtiwzECBkqadhFTRjkTQBwEkgg'
    #           'pgmXp1ul9AnrHQ="',
    # "x-api-source": "pc",
    # "cache-control": "no-cache",
    # "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    #                    ",zh-CN;q=0.6,ja;q=0.5",
    "if-none-match-": "55b03-932dd7bcde62654ef397c73b79016c8b",
}

print(requests.get(
    url, params=params, headers=headers).json()['items'][2]['name'])
