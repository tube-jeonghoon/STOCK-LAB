import requests
import configparser
import xml.etree.ElementTree as ET


class Data():
    CORP_CODE_URL = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByNm'
    CORP_INFO_URL = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBasicInfo'
    STOCK_DISTRIBUTION_URL = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getStkDistributionShareholderStatus'

