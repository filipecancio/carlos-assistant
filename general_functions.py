import os
import json

def getDirectory(rel_dir):
    script_dir = os.path.dirname(__file__)
    complete_dir = script_dir + rel_dir
    return complete_dir

def getJson(rel_dir):
    complete_dir = getDirectory(rel_dir)
    with open(complete_dir, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data