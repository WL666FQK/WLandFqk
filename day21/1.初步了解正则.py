# Author: 王璐
# Date: 2025/1/6
# Time: 17:10

import re

result=re.match('fengqikang','fengqikang loves wanglu')
if result:
    print(result.group())