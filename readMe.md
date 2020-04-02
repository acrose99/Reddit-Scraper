## Reddit Age Predicter

### How does it work
I am using [PRAW](https://praw.readthedocs.io/en/latest/) to parse through subreddits.
Currently, this looks at a subreddit and depending on user input, ends up writing comments from users of that subreddit's posts to a csv file (read the Scraping methods folder for more info). In the future it will be way more flexible. 

###Why did I build this
In particular, I am currently using this for a project that will guess the generation/age of a redditor based off one comment, using machine learning and natural language processing.
However, I've had a lot of fun making this and wanna create a full fleged scraper!

###Authentication
1. [Create a script here](https://www.reddit.com/prefs/apps)
2. Create a file called config.py
3. Sub in these variables
* `client_id=''`
* `client_secret=''`
* `password=''`
* `user_agent=''`
* `username=''`

