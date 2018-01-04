#####################################################################################
#
#
# This file contains a number of Utility functions
#
#
#####################################################################################
require(ggmap)
library(ggmap)


ZipToConfig <- function(ZIPCODE_FILE = './data/zipcode_NJ.csv', OUTPUT = '../config/cfg_scraping_NJ.csv'){
  
  
  zipcode_data = read.delim(ZIPCODE_FILE, sep = ',',header=T, colClasses = c("character"), skipNul = F)
  
  for (i in 1: dim(zipcode_data)[1]){zipcode_data[i, 'zip'] = paste0(rep('0',(5-nchar(zipcode_data$zip[i]))), zipcode_data[i,'zip'], collapse = '')}
  
  geocode_data <- geocode(c(zipcode_data[,'zip']), output = 'more',source = 'google')
  zipcode_data = cbind(zipcode_data, geocode_data)
  zipcode_data['viewport']= paste(zipcode_data$north, zipcode_data$south, zipcode_data$east, zipcode_data$west, sep=':')
  zipcode_data = zipcode_data[!is.na(zipcode_data$south),]
  zipcode_data = zipcode_data[c('zip','state','primary_city','viewport')]
  colnames(zipcode_data) =c('zipcode','state','description','viewport')
  
  write.csv(zipcode_data, OUTPUT, row.names = F)  
  
  
}











