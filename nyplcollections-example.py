#!/usr/bin/env python

import pprint
from nyplcollections import NYPLsearch

# Create search object
# Could also pass in a format of 'xml' if you want to use the raw_results
# and require xml. Otherwise the search will return json in raw_results
searchObj = NYPLsearch('[YOUR_KEY]')

# Find captures based on uuid
# Don't need to set this equal to anything, could also access results from
# searchObj.results
temp = searchObj.captures('2600a3f0-c5ec-012f-424e-58d385a7bc34')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(temp)

