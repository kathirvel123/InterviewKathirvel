#merge intervel


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l=[]
        j=0
        for i in intervals:
            if l==[]:
                l.append(i)
            else:
                if l[j][1]<i[0]:
                    l.append(i)
                    j+=1
                elif l[j][1]<=i[1]:
                    l[j]=[l[j][0],i[1]]
        return l