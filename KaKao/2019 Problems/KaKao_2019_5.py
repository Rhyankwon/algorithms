#2019 카카오 블라인드 채용 5번 문제(길 찾기 게임)

import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    pre = []
    post = []
    dict_node = {}
    if not nodeinfo:
        return []
    for i in range(len(nodeinfo)):
        dict_node[tuple(nodeinfo[i])] = i+1
    def bst(nodes):
        if not nodes:
            return
        sorted_y_axis = sorted(nodes, key = lambda x : -x[1])
        sorted_x_axis = sorted(nodes, key = lambda x : x[0])
        idx = sorted_x_axis.index(sorted_y_axis[0])
        pre.append(dict_node[tuple(sorted_y_axis[0])])
        bst(sorted_x_axis[:idx])
        bst(sorted_x_axis[idx+1:])
        post.append(dict_node[tuple(sorted_y_axis[0])])
    bst(nodeinfo)
    return [pre, post]