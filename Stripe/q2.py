"""
You are given a string expression which consists of several comma separated tokens 
enclosed within opening ('{') and closing ('}') curly braces.
The string expression might or might not have a prefix before opening curly brace('{') and
a suffix after closing curly brace ('}').
You have to return a list of strings as output for each comma separated item as shown below in the examples. 

Example 1: 
Input = "/2022/{jan,feb,march}/report"
Output = "/2022/jan/report"
		 "/2022/feb/report"
		 "/2022/march/report"
		 
Example 2: 
Input = "over{crowd,eager,bold,fond}ness"
Output = "overcrowdness"
		 "overeagerness"
		 "overboldness"
		 "overfondness"
		 
Example 3: 
Input = "read.txt{,.bak}"
Output = "read.txt"
		 "read.txt.bak"
"""

expression = input()
stack = []
curarray = []
cur = ""
for i in expression:
    print(stack,curarray)
    if i=='{':
        curarray.append(cur)
        cur = ""
        stack.append(i)
    elif i=='}':
        stack.append(cur)
        cur = ""
        ls = len(stack)-1
        while stack[ls]!='{':
            if stack[ls]=='#' or stack[ls]=='@':
                stack[ls]='@'
                ls-=1
                continue
            stack[ls] = curarray[-1] + stack[ls]
            ls-=1
        else:
            stack[ls] = "#"
            curarray.pop()
    elif i==',':
        stack.append(cur)
        cur = ""
    else:
        cur+=i
answer = []
subset = []
print(stack,subset)
for i in stack:
    if i=='#':
        if subset==[]:
            continue
        else:
            answer.append(subset)
            subset = []
    if i=='@' or i=='' or i in subset:
        continue
    subset.append(i)
if subset!=[]:
    answer.append(subset)
print(answer)

