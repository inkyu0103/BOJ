# 14405

import re

diction = input().strip()
p = re.sub('pi|ka|chu','',diction)
if p:
    print("NO")
else:
    print("YES")