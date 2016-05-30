#!/bin/env python
# Copyright 2016, EMC, Inc.
#md5sum="352503544435281bafe3ffa943ce40d0"

import urllib2
import json
import imp
import traceback
import sys

def download_cisco_script():
    # Add switch vendor string as the last URI element as a hint to the
    # HTTP API server
    print "Downloading script <%=switchProfileUri%>/cisco"
    script = urllib2.urlopen('<%=switchProfileUri%>/cisco').read()
    print "Opening script rackhd_cisco_script.py"
    with open('rackhd_cisco_script.py', 'w') as rackhd_cisco_script:
        rackhd_cisco_script.write(script)

try:
    download_cisco_script()
    print "Executing script rackhd_cisco_script.py"
    execfile('./rackhd_cisco_script.py')
except SystemExit as e:
    sys.exit(e)
except:
    data = json.dumps({"error": traceback.format_exc()})
    req = urllib2.Request('<%=switchProfileErrorUri%>', data, {"Content-Type": "application/json"})
    urllib2.urlopen(req)
    # Don't swallow exceptions otherwise the Cisco switch will think the POAP was a success
    # and proceed to boot rather than retrying
    raise error
