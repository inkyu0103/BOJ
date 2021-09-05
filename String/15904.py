#15094
import re
user = input().strip()
tmp=re.sub('[^UCP]',"",user)
print(tmp)
tmp=re.sub('[U]+','U',tmp)
tmp=re.sub('[C]+','C',tmp)
tmp=re.sub('[P]+','P',tmp)
tmp=re.sub('[C]+','C',tmp)
print(tmp)
if "UCPC" in tmp:
    print("I love UCPC")
else:
    print("I hate UCPC")

