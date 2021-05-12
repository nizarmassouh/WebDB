## A python implementation of the IROS 2017 paper: [Learning Deep Visual Object Models From Noisy Web Data: How to Make it Work](https://www.researchgate.net/publication/314115657_Learning_Deep_Visual_Object_Models_From_Noisy_Web_Data_How_to_Make_it_Work)


For the creation of image databases from the web.
This software will expand a list of visual queries and download images from 3 search engines (google, yahoo and bing).

### Requirements

* Python 3.6 or above
* Selenium
* BeautifulSoup
* Chromium browser
* [Chromium webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Note: The chromium webdriver should match the chrome browser installed in the users system.
### Create Expanded Query list
run the bash file `expand.sh` with 1 argument (the list of queries as a line separated list) from terminal

For e.g.
```bash
sh expand.sh queries.txt
```

The expanded query will be saved to the file `expandedqueries.txt`

### Download Web Images

User can download the images by running download.py using 2 arguments:
example:  

```bash
python download.py --queries queries.txt --directories dirnames.txt
```

where queries.txt is a text file with a list of queries and dirnames.txt is the equivalent directory name of each query line by line.


		queries.txt:	query1
				query2
				...
		dirnames.txt:	dir1
         		 	dir2
				...

In case of query expansion the queries provided on the same line separated with a comma can be downloaded into the same directory name.

	queries.txt: query1.1, query1.2, query1.3...     dirnames.txt: dir1
        	     query2.1, query2.2, query2.3...                   dir2
  		     ...                                               ...
