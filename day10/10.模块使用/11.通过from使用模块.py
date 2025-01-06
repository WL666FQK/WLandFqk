# Author: 王璐
# Date: 2024/10/16

from test_module import say_hello as module_say_hello
from test_module2 import say_hello
from test_module2 import title
from test_module2 import Dog

module_say_hello()
say_hello()
print(title)
dog=Dog()