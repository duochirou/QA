from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "omg"])
#execute(["scrapy", "crawl", "test"])
#execute(["scrapy", "crawl", "quotes"])
#scrapy crawl quotes -o quotes.json
# scrapy crawl quotes -o quotes.jl
