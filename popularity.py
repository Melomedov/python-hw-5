from array import array

from collections import Counter
from operator import itemgetter




def popularity(text):
    lower_text = text.lower()
    
    arr= Counter(lower_text.split())
    sorted_arr = sorted(arr.items(), key=lambda item: (-item[1], item[0]))
    return list(map(itemgetter(0), sorted_arr))

    # # arr.sort()
    # sorted_tuple = sorted(arr.items(), key=lambda x: x[1], reverse=True)
    # sorted_tuple = dict(sorted_tuple)
    # my_list=[]
    # for key in sorted_tuple:
    #      for two_key in sorted_tuple:
    #         if sorted_tuple[key]==sorted_tuple[two_key]:
    #             print(sorted_tuple[key])



print(popularity('apple kiwi pineapple kiwi apple kiwi')) #-> ['kiwi', 'apple', 'pineapple']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) #-> ['apple', 'kiwi', 'pine']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) #-> ['apple', 'kiwi', 'pine']
print(popularity('aab aaa aac aab aac aaa x')) #-> ['aaa', 'aac', 'aac', 'x']
print(popularity('sdfgksjfhklsf'))