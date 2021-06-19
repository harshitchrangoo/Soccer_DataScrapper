# Soccer_DataScrapper

This is a repository that would enable the user to extract data from the football statistic platform www.understat.com
This platform has data of the top 5 european football leagues and gives us data from season 2014. 
Here, we extract this data and combine it. 

Later we would look to clean this data as I have observed that the player names get butchered upon scraping as some letters don't fall into the english alphabets.
We would look to create a dictionary and replace the letters as we encounter them so that the names could be written in English and closely relate to the native language.
Eg: *Sergio AgÃ¼ero* would become *Sergio Aguero* instead of _Sergio Agüero_.

-----------------------

Upon digging, we can see that the code is working fine but the csv does not support utf8 by default.
Follow the steps below to get the data as required:

1.  Open a new *Excel* file > *Data* tab > *Get external data* > *From Text*
2.  Navigate to the file and select it. Proceed by clicking on import.
3.  Choose the file type that best describes your data - Delimited or Fixed Width.
4.  Choose 65001: Unicode (UTF-8) from the drop-down list that appears next to File origin.
5.  Click on the Next button.
6.  Place a checkmark next to the delimiter that was used in the file you wish to import into Microsoft Excel. The Data preview window will show you how your data will appear based on the delimiter that you chose.
7.  Click on the Next button.
8.  Choose the appropriate data format for each column of data that you want to import. You also have the option to not import one or more columns of data if you want.
9.  Click on finish to complete data import.

