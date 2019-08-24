#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/24 11:15 
# @Author : Ahrist 
# @Site :  
# @File : main.py 
# @Software: PyCharm

import sys
import os

from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", 'crawl', 'books'])