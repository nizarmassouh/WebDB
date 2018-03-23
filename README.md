# WebDB
For the creation of image databases from the web.
This software will download images from 3 search engines (google, yahoo and bing).

By running download.py using 2 arguments:
example:  python download.py queries.txt dirnames.txt

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
