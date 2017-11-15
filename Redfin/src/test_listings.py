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
    Redfin_ActiveLising SubClass - by zipcode
    """    
    redfin_listing = redfin.Redfin_ActiveListing(zipcode = zipcode)
    redfin_listing.use_proxies = False
    redfin_listing.start_browser()
    sleep(1)
    redfin_listing.get_listing_byzipcode(viewport = viewport)
    redfin_listing.get_property_data()

    redfin_listing.close_brower()


if __name__ == "__main__": 
    
    parser = argparse.ArgumentParser(description="Redfin Scraping")
    parser.add_argument('-t', '--test', help ='TEST MODE', type = bool, default = True)
    args = parser.parse_args()
    
    main(args)