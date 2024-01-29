import re
findmembers=[]
for member in dir(re):
    if "find" in member:
        findmembers.append(member)
    
print(sorted(findmembers))