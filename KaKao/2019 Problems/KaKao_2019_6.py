import re

# 구글 검색으로 다른 해설의 풀이를 참고한 파이썬 풀이. re모듈 공부에 좋은 문제인듯.

def solution(word, pages):
    meta_p = re.compile('<meta(.+?)/>')
    a_p = re.compile('<a(.+?)>')
    page_infos = []
    for page in pages:
        page_dict = {}
        a_tags = a_p.findall(page)
        outer_url = []
        for a_tag in a_tags:
            first_idx = end_idx = -1
            for idx, char in enumerate(a_tag):
                if char == '"':
                    if first_idx == -1:
                        first_idx = idx
                    elif end_idx == -1:
                        end_idx = idx
            outer_url.append(a_tag[first_idx+1:end_idx])
        meta_tag = meta_p.search(page).group()
        content_prop = meta_tag.split()[2]
        first_idx = end_idx = -1
        for idx, char in enumerate(content_prop):
            if char == '"':
                if first_idx == -1:
                    first_idx = idx
                elif end_idx == -1:
                    end_idx = idx
        url = content_prop[first_idx+1:end_idx]
        page_dict['outer_url_list'] = outer_url
        page_dict['url'] = url
        #아래에 re.sub 이후 +를 붙이는 이유는 우선 해당하는 문자가 하나라도 있어야하고 한번에 묶어서 하나의 .으로 만들기위해.
        page_dict['keyword_point'] = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
        page_dict['link_point'] = 0
        page_infos.append(page_dict)
    for page_info in page_infos:
        for outer_url in page_info['outer_url_list']:
            for outer_url_candidate in page_infos:
                if outer_url == outer_url_candidate['url'] :
                    outer_url_candidate['link_point'] += page_info['keyword_point']\
                                                        /len(page_info['outer_url_list'])
    point_1 = [page_info['link_point']+page_info['keyword_point'] for page_info in page_infos]
    return point_1.index(max(point_1))