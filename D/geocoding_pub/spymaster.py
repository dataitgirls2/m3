import urllib.parse
import urllib.request
from json import loads
import pandas as pd

class Agent:
    def __init__(self, client_id: str, client_secret: str):
        self.id = client_id
        self.secret = client_secret
    # 남은 검색 횟수도 조회할 수 있다면 좋을지도??

def get_search_mods():
    """search에 사용 가능한 mode 목록을 출력함
    """
    print('사용 가능한 검색 모드: local, blog, encyc, doc, kin, book, news, movie, cafearticle, shop')
    return None


def get_url(keyword, mode, display=100, start=1, sort='sim'):
    """인자를 받아 네이버 api에 request를 보내기 적합한 형식으로 url 생성
    __________________________________
    keyword: 검색 키워드, 혹은 (geocode 모드일 때) 제대로 된 주소.
    mode: geocode, local, blog, encyc, doc, kin, book, news, movie, cafearticle, shop 있음.
    display: 한 번에 받아올 검색 결과 수. 최대 100. 디폴트 100.
    start: 검색 결과의 몇 번째 항목부터 받아올 것인가. 디폴트 1.
    sort: 검색 결과 목록 정렬 방식. 'sim':유사도순, 'date':날짜순. 디폴트 'sim'
    """
    keyword_encoded = urllib.parse.quote(keyword.encode('utf-8'))
    if mode == 'geocode':
        url_base = "https://openapi.naver.com/v1/map/geocode?query={}"
        url = url_base.format(keyword_encoded)
    else:
        url_base = "https://openapi.naver.com/v1/search/{}.json?query={}&display={}&start={}&sort={}"
        url = url_base.format(mode, keyword_encoded, display, start, sort)
    return url


def get_response(agent, url):
    client_id, client_secret = agent.id, agent.secret
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    return response


def get_search_result(agent, keyword, mode, display=100, start=1, sort='sim'):
    url = get_url(keyword, mode, display, start, sort)
    response = get_response(agent, url)
    rescode = response.getcode()
    if rescode == 200:
        response_raw = response.read().decode('utf-8')
        return response_raw
    else:
        # 나중에 rescode 해석해주는 기능도 넣을까?
        print("Error Code:" + rescode)
        return None


def tidy_search_result(response_raw):
    """검색 결과물을 데이터프레임 형식으로 반환"""
    response_loaded = loads(response_raw)
    total = response_loaded['total']
    print('total number of items are: ', total)
    items = response_loaded['items']
    columns = list(items[0].keys())
    data = []
    for item in items:
        item_temp = []
        for c in range(len(columns)):
            column_temp = columns[c]
            item_temp.append(item[column_temp])
        data.append(item_temp)
    df = pd.DataFrame(data=data, index=None, columns=columns)
    return df


def search(agent, keyword, mode, display=100, start=1, sort='sim'):
    """
    agent, 검색 키워드와 검색 mode 데이터로 네이버 검색 api를 호출,
    결과물을 데이터프레임 형식으로 출력합니다.
    --------------------------------------------------------
    agent: Naver-Client-Id, Secret 데이터를 보유한, Agent 인스턴스
    keyword: 검색 키워드.
    display: 한 번에 받아올 검색 결과 수. 최대 100. 디폴트 100.
    start: 검색 결과의 몇 번째 항목부터 받아올 것인가. 디폴트 1.
    sort: 검색 결과 목록 정렬 방식. 'sim':유사도순, 'date':날짜순. 디폴트 'sim'

    """
    response_raw = get_search_result(agent, keyword, mode, display, start, sort)
    df = tidy_search_result(response_raw)
    return df


def get_coor(agent, address):
    """agent, 제대로 된 형식의 주소를 받아 주소의 경도(lng), 위도(lat)를
    딕셔너리 형태로 반환합니다.
    ------------------------------------------------------
    agent: Naver-Client-Id, Secret 데이터를 보유한, Agent 인스턴스
    address: 지번이나 도로명주소 (국내)
    """
    response_raw = get_search_result(agent, address, mode='geocode')
    response = loads(response_raw)
    coor = response['result']['items'][0]['point']
    lng = coor['x']    # 경도
    lat = coor['y']    # 위도
    return {'lng': lng, 'lat': lat}


# ----------미구현------------------------------

def add_coordinates_columns(agent, data, address_column, status='new'):
    # 제대로된 주소가 있는 데이터프레임을 입력하면 주소로 좌표를 추출해
    # 위도, 경도 컬럼을 추가해주는 모듈을 만들려 했으나 생각해보니 별 필요 없어보여서 보류.
    if status == 'new':
        data['lon'] = None
        data['lat'] = None
    for i in data:
        if True:
            # 해당 열 lon이 비어있지 않을 경우 실시, 이미 데이터가 있으면 pass
            try:
                lon, lat = get_coordinates(agent, data[address_column])
            except:
                pass
        else:
            pass


def get_trend():
    # 지금 당장 필요하지는 않으니 시간 나면 해야겠다
    pass



