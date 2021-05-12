## A python implementation of the IROS 2017 paper: [Learning Deep Visual Object Models From Noisy Web Data: How to Make it Work](https://www.researchgate.net/publication/314115657_Learning_Deep_Visual_Object_Models_From_Noisy_Web_Data_How_to_Make_it_Work)


Create image databases from the Web.
This software will expand a list of visual queries and download images from 3 search engines (google, yahoo and bing).

### Requirements

* Python 3.8 or above
* [Selenium](https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/#_python_) 3.141 or above
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/#Download) 4.9.3 or above
* Firefox
* [Firefox webdriver](https://github.com/mozilla/geckodriver/releases)
* [User-Agent addon for Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/)

#### Setting up Firefox Webdriver
Extract the contents of the downloaded file.
For file with `.zip` extension use `unzip <filename>` or for file with `.tar.gz` extension use `tar -xvf <filename>`

Finally, add the extracted file to `$PATH`. Refer [how to add executables to PATH](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#adding-executables-to-your-path)

#### Install User Agent Addon

If you encounter any error or pop ups which asks for cookies that doesn't appear when the search is launched by the user. Ensure the `User-Agent` is recent with respect to your browser version.

Refer common "How to debug the script"

This addon is required only for debugging purpose change user agent
### Create Expanded Query list
run the bash file `expand.sh` with 1 argument (the list of queries as a line separated list) from terminal

For e.g.
```bash
sh expand.sh queries.txt
```

The expanded query will be saved to the file `expandedqueries.txt`

### Download Web Images

User can download the images by running download.py using 3 arguments:
example:

```bash
python download.py --queries queries.txt --directories dirnames.txt --run_headless
```

* `--queries` A file containing the search queries
* `--directories`: A file containing the directory name where the downloaded images are stored
* `--run_headless`: Argument that doesn't display the browser when script runs. Don't pass this argument when you don't need to visualize the script in action. This is useful for debugging purposes and check if scripts navigates to the correct page.

where queries.txt is a text file with a list of queries and dirnames.txt is the equivalent directory name of each query line by line.


		queries.txt:	query1
				query2
				...
		dirnames.txt:	dir1
         		 	dir2
				...

Note: It's also possible to provide single entry in the dirnames.txt file, so that all the images are saved in a single folder.

In case of query expansion the queries provided on the same line separated with a comma can be downloaded into the same directory name.

	queries.txt: query1.1, query1.2, query1.3...     dirnames.txt: dir1
        	     query2.1, query2.2, query2.3...                   dir2
  		     ...                                               ...


### How to debug:

All the search engines constantly try to introduce changes to their webpages in order to restrict webscraping, therefore scripts in this repository requires maintenance when they break.

We provide very basic method for debugging the scripts.

* We try to catch and log the exceptions in the console during HTML parsing or image retrevial. Looking at the stack trace would help identify the root cause.
* Visualizing the selenium action on the browser could help quickly identify any browser rendering issue. Remove `--run_headless` flag argument when invoking `download.py`.
* We use [css selectors](https://www.w3schools.com/cssref/css_selectors.asp) in order get unqiuely identify selector tags in the webpage. Seach engines could update these tags which might cause the script to fail.
* Ensure you are using the latest version of Firefox browser and update the `User-Agent` accordingly. Depending upon browser version and User-Agent the page might render differently which could cause the script to fail.
* If you observe slower network speed. Try increasing the script sleep time.

The script is expected to run slower with varying sleep times. This is mimic human behaviour and not to flood server with constant requests. 
`Warning:` Repated requests with almost no wait time could lead to blacklisting of the user's IP.

### How to use css selector:
* How to check tags are uniquely identified.
	* Open Firefox, Navigate to "www.google.com"
	* Press `F12` to open the developer tools
	* Press `Ctrl + Shift + c` to pick elements from the page
	* Hover the mouse over `Input Search` text box in google search page.
	* In the inspector tab, you should see the `<input class="gLFyf gsfi"..etc..>` selected
	* Now click `Console` tab. Type `$$("input.gLFyf.gsfi")` and hit enter. Spaces in the class name should be replace with `.`
	* You should see the output html tag displayed
* Using the above tag in selenium is very easy
	```python
	input_text_box = driver.find_element_by_css_selector("input.gLFyf.gsfi")
	```
