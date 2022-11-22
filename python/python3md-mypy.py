#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


from typing import Optional
from typing import Union
from typing import List, Dict

###

boolvar: bool = True
intvar: int = 123
floatvar: float = 1.23
strvar: str = 'foo'

strvar = 'bar'
boolvar = 'hoge'

###

# # listvar: list = [1, 2, 3]
# # dictvar: dict = {1: 'foo', 2: 'bar'}
# listvar: List[int] = [1, 2, 3]
# dictvar: Dict[int, str] = {1: 'foo', 2: 'bar'}

# intstrvar: Union[int, str] = 123
# intstrvar = 'foo'
# intstrvar = 1.23

###

dictvar: Dict[int, str] = {1: 'foo'}
strnonevar: Optional[str] = dictvar.get(2)
print(strnonevar)
