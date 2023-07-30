from collections import defaultdict
class Solution2:
    def groupAnagrams(self, strs):
        arr = {}
        end = 0
        while end < (len(strs)):
            arr_temp =[]
            string = "".join(sorted(strs[end]))
            if string not in arr :
                arr_temp.append(strs[end])
                arr[string] =  arr_temp
            else:
                arr_temp.append(strs[end])
                arr[string] +=  arr_temp
            end += 1 
        arr= list( arr.values())
        return arr


class Solution :
    def groupAnagrams(self,strs):
        map = defaultdict(list)

        for  str in strs:
            str_sorted = ''.join(sorted(str))
            map[str_sorted].append(str)
        return list(map.values())