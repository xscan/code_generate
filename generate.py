# -*- coding: utf-8 -*-
from string import Template
import time
import datetime
import json
import os
import argparse
import sys

def readConfig(ConfigPath):
    f= open(ConfigPath,'r')

    tpl = f.readlines()

    f.close()

    stpl =''.join(tpl)

    return json.loads(stpl)


def readTpl(TplPath):

    f= open(TplPath,'r')

    tpl = f.readlines()

    f.close()

    stpl =''.join(tpl)

    result=False

    if stpl.strip()=='':
        result = False
    else:
        result = stpl
    
    return result
pass

def compileTpl(data,Tpl,mode=True):

    stpl = Template(Tpl)
    
    if mode:
        compileTpl = stpl.substitute(data)
    else:
        compileTpl = stpl.safe_substitute(data)


    if compileTpl.strip():
        return compileTpl
    else:
        return False
pass

def build(config):
    # config = readConfig(settingpath)

    for index,generate in enumerate(config['list']):

        tpl = readTpl(config['tpl'])
       
        generate['classname'] = generate['name'].capitalize()

        ctpl = compileTpl(generate,tpl)

        outputfilename = os.path.join(config['output'],generate['name']+'.py')

        with open(outputfilename,'w') as f:

            print "%d : generate file %s success!" %(index+1,outputfilename)
            
            f.writelines(ctpl.encode('utf-8'))
    



parser = argparse.ArgumentParser(description='genetate setting')
parser.add_argument('--input',"-i", nargs='?', type=argparse.FileType('r'),
                default=sys.stdin)
args = parser.parse_args()
if args.input:
    try:
        config = json.loads(args.input.read())
        # print config
        build(config)
        pass
    except:
        print 'config error!'
        pass
    
# if args.input:
#     config = json.loads(args.input.read())
#     print config
#     build(config)



