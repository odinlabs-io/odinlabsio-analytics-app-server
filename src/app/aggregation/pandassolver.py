#  MIT License
#
#  Copyright (c) 2020 OdinLabs IO
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import re
from typing import Union, Any, List

import numpy as np

from app.aggregation.dag import Solver


class DateSolver(Solver):
    def __init__(self):
        self._relative_date = re.compile(r'\s*(?P<origin>(today|yesterday))\s*((?P<offset>[-+])\s*(?P<count>\d+))?$')
        self._date = re.compile(r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$')

    def _to_time(self, value):
        matched = self._relative_date.match(value)
        if matched:
            origin = matched.group('origin')
            origin_time = np.datetime64('today')
            if origin == 'yesterday':
                origin_time = origin_time - 1
            count = matched.group('count')
            if count:
                offset = matched.group('offset')
                if offset == '+':
                    origin_time = origin_time + int(count)
                else:
                    origin_time = origin_time - int(count)
            return origin_time
        matched = self._date.match(value)
        if matched:
            return np.datetime64(value)

        raise Exception('Failed to parse date value from {}'.format(value))

    def solve_for_variable(self, value: Union[Any, List[Any]]) -> Union[Any, List[Any]]:
        if isinstance(value, List):
            return [self._to_time(time_value) for time_value in value]
        else:
            return self._to_time(value)
