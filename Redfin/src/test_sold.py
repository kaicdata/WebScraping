# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:20:59 2017
"""

import os
import pandas as pd
#ROTT_DIR ='C:\Disks\D\WebScraping\WebScraping\Redfin\src'
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(ROOT_DIR)
import argparse
from time import sleep

import redfin

CFG_SCRAPING = pd.read_csv('../config/cfg_scraping_NJ.csv', dtype =str)


def main(args):
        
    if args.test:
        
        CFG_SCRAPING = pd.read_csv('../config/cfg_scraping_test.csv', dtype =str)
               
    # for testing:
    for index, row in CFG_SCRAPING.iterrows():
        zipcode = row['zipcode']
        zipcode = '0'*(5-len(zipcode))+zipcode # add leading zeros if removed
        viewport = row['viewport']
        #zipcode = CFG_SCRAPING['zipcode'][0]
        #viewport = CFG_SCRAPING['viewport'][0]
        
        
        """
        Redfin_HistorialSales SubClass - by zipcode
        """
        redfin_sold = redfin.Redfin_HistoricalSales(zipcode = zipcode)
        redfin_sold.use_proxies = False
        redfin_sold.start_browser()
        sleep(1)
        redfin_sold.get_historicalsales_byzipcode(viewport = viewport )
        redfin_sold.get_property_data()
        redfin_sold.close_brower()


if __name__ == "__main__": 
    
    parser = argparse.ArgumentParser(description="Redfin Scraping")
    parser.add_argument('-t', '--test', help ='TEST MODE', type = bool, default = True)
    args = parser.parse_args()
    
    main(args)