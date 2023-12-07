[![Build Status](https://travis-ci.org/donnemartin/haxor-news.svg?branch=master)](https://travis-ci.org/donnemartin/haxor-news) [![Dependency Status](https://gemnasium.com/donnemartin/haxor-news.svg)](https://gemnasium.com/donnemartin/haxor-news)
[![PyPI version](https://badge.fury.io/py/haxor-news.svg)](http://badge.fury.io/py/haxor-news) [![PyPI](https://img.shields.io/pypi/pyversions/haxor-news.svg)](https://pypi.python.org/pypi/haxor-news/) [![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)

==========
To view the latest `README`, `docs`, and `code` visit the GitHub repo:

To submit bugs or feature requests, visit the issue tracker:

Changelog

------------------

### Bug Fixes

* [#94](https://github.com/donnemartin/haxor-news/pull/94) - Update to `prompt-toolkit` 1.0.0, which includes a number of performance improvements (especially noticeable on Windows) and bug fixes.

### Bug Fixes


0.4.0 (2016-05-30)


* [#52](https://github.com/donnemartin/haxor-news/issues/52) - Add `exit` and `quit` commands, which can be used instead of `ctrl-d`.

* [#36](https://github.com/donnemartin/haxor-news/issues/36) - Fix crash caused by Unicode comments on Windows.
* Fix some comments and docstrings.
### Updates

* [#48](https://github.com/donnemartin/haxor-news/issues/48), [#50](https://github.com/donnemartin/haxor-news/issues/50) - Update latest monthly hiring post ids.
* Update `README`:
    * Update intro
    * Update comments discussion and examples
    * Add note about OS X 10.11 pip installation issue

------------------

- Initial release.# TWINT - Twitter Intelligence Tool
![3](https://i.imgur.com/hVeCrqL.png)

[![PyPI](https://img.shields.io/pypi/v/twint.svg)](https://pypi.org/project/twint/) [![Build Status](https://travis-ci.org/twintproject/twint.svg?branch=master)](https://travis-ci.org/twintproject/twint) [![Python 3.6|3.7|3.8](https://img.shields.io/badge/Python-3.6%2F3.7%2F3.8-blue.svg)](https://www.python.org/download/releases/3.0/) [![GitHub license](https://img.shields.io/github/license/haccer/tweep.svg)](https://github.com/haccer/tweep/blob/master/LICENSE) [![Downloads](https://pepy.tech/badge/twint)](https://pepy.tech/project/twint) [![Downloads](https://pepy.tech/badge/twint/week)](https://pepy.tech/project/twint/week) [![Patreon](https://img.shields.io/endpoint.svg?url=https:%2F%2Fshieldsio-patreon.herokuapp.com%2Ftwintproject)](https://www.patreon.com/twintproject) ![](https://img.shields.io/twitter/follow/noneprivacy.svg?label=Follow&style=social) 



- Can fetch almost __all__ Tweets (Twitter API limits to last 3200 Tweets only);
- **No rate limitations**.

Twitter limits scrolls while browsing the user timeline. This means that with `.Profile` or with `.Favorites` you will be able to get ~3200 tweets.
## Requirements
- aiodns;
- beautifulsoup4;
- cchardet;
- elasticsearch;
- pysocks;
- schedule;
- fake-useragent;
- py-googletransx.

## Installing

**Git:**

**Pip:**
```
or


**Pipenv**:
```bash
pipenv install git+https://github.com/twintproject/twint.git#egg=twint

### March 2, 2021 Update
**Added**: Dockerfile

A few simple examples to help you understand the basics:
- `twint -u username -s pineapple` - Scrape all Tweets from the *user*'s timeline containing _pineapple_.
- `twint -u username --since "2015-12-20 20:30:15"` - Collect Tweets that were tweeted since 2015-12-20 20:30:15.
- `twint -u username -o file.csv --csv` - Scrape Tweets and save as a csv file.
- `twint -g="48.880048,2.385939,1km" -o file.csv --csv` - Scrape Tweets from a radius of 1km around a place in Paris and export them to a csv file.
- `twint -u username -es localhost:9200` - Output Tweets to Elasticsearch
- `twint -u username -o file.json --json` - Scrape Tweets and save as a json file.
- `twint -u username --followers` - Scrape a Twitter user's followers.
- `twint -u username --following` - Scrape who a Twitter user follows.
- `twint -u username --retweets` - Use a quick method to gather the last 900 Tweets (that includes retweets) from a user's profile.
- `twint -u username --resume resume_file.txt` - Resume a search starting from the last saved scroll-id.
More detail about the commands and options are located in the [wiki](https://github.com/twintproject/twint/wiki/Commands)
## Module Example

```python
import twint
c = twint.Config()
c.Username = "realDonaldTrump"

twint.run.Search(c)
```
> Output
`955511208597184512 2018-01-22 18:43:19 GMT <now> pineapples are the best fruit`

```python
import twint
c.Username = "noneprivacy"
c.Custom["tweet"] = ["id"]
c.Store_csv = True
c.Output = "none"

```

- Write to file;
- CSV;
- JSON;
- Elasticsearch.
## Elasticsearch Setup


We are developing a Twint Desktop App.

![4](https://i.imgur.com/DzcfIgL.png)

Twitter can shadow-ban accounts, which means that their tweets will not be available via search. To solve this, pass `--profile-full` if you are using Twint via CLI or, if are using Twint as module, add `config.Profile_full = True`. Please note that this process will be quite slow.
## More Examples
#### Followers/Following
> To get only follower usernames/following usernames
`twint -u username --followers`
`twint -u username --following`

> To get user info of followers/following users
`twint -u username --followers --user-full`
`twint -u username --following --user-full`


> To get only user info of user

`twint --userlist inputlist --user-full`
#### tweet translation (experimental)
> To get 100 english tweets and translate them to italian

`twint -u noneprivacy --csv --output none.csv --lang en --translate --translate-dest it --limit 100`

or

import twint
c.Username = "noneprivacy"
c.Limit = 100
c.Translate = True
twint.run.Search(c)
```

Notes:

- [Basic tutorial made by Null Byte](https://null-byte.wonderhowto.com/how-to/mine-twitter-for-targeted-information-with-twint-0193853/)
- [Analyzing Tweets with NLP in minutes with Spark, Optimus and Twint](https://towardsdatascience.com/analyzing-tweets-with-nlp-in-minutes-with-spark-optimus-and-twint-a0c96084995f)
- [Loading tweets into Kafka and Neo4j](https://markhneedham.com/blog/2019/05/29/loading-tweets-twint-kafka-neo4j/)
