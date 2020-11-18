# XML TO EXCEL FILE
import xml.etree.ElementTree as ET
from openpyxl import Workbook
import os
import json
import csv


def readFile(filename):
    '''
		Checks if file exists, parses the file and extracts the needed data
		returns a 2 dimensional list without "header"
	'''
    if not os.path.exists(filename): return
    tree = ET.parse(filename)
    root = tree.getroot()
    # you may need to adjust the keys based on your file structure
    dict_keys = ["id", "first_name", "last_name", "email", "gender", "ip_address"]  # all keys to be extracted from xml
    mdlist = []
    for child in root:
        temp = []
        for key in dict_keys:
            temp.append(child.find(key).text)
        mdlist.append(temp)
    return mdlist
