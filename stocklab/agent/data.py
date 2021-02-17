import requests
import configparser
import xml.etree.ElementTree as ET


class Data:
    CORP_CODE_URL = (
        "http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByNm"
    )
    CORP_INFO_URL = "http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBasicInfo"
    STOCK_DISTRIBUTION_URL = "http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionShareholderStatus"

    def __init__(self):
        config = configparser.RawConfigParser()
        config.read("conf/config.ini")
        self.api_key = config["DATA"]["api_key"]
        if self.api_key is None:
            raise Exception('Need to api key')

    def get_corp_code(self, name=None):
        '''
        한국예탁결제원에서 제공하는 기업 코드를 회사명으로 검색합니다.
        :param name:str 회사명 ex) 삼성전자, 삼성 등..
        :return:dict 회사 코드와 회사명을 반환합니다.
        '''

        query_params = {
            'serviceKey': self.api_key,
            'issucoNm': name,
            'numOfRows': str(5000)
        }
        request_url = self.CORP_CODE_URL+'?'
        for k, v in query_params.items():
            request_url = request_url + k + '=' + v + '&'

        res = requests.get(request_url[:-1])
        root = ET.fromstring(res.text)
        from_tags = root.iter('items')
        result = {}
        for items in from_tags:
            for item in items.iter('item'):
                if name in item.find('issucoNm').text.split():
                    result['issucoCustno'] = item.find('issucoCustno').text
                    result['issucoNm'] = item.find('issucoNm').text
        return result
