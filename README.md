# speedtweet

This package will check your internet speed against a specified threshold and if it is below then it will tweet at the provided account about your current internet speeds.

## Example Tweet

```
@MediacomSupport I am experiencing issues with my internet. My speed is at 295.96 MB/s Down & 60.26 MB/s Up. This is 70.5% below what I am paying for.
```

## Getting Started

You can install this project from this repository by first cloning the repository.  Before installing, please modify the [speedtweet.yml](speedtweet.yml) configuration file or set environmental variables.  You will need to have Twitter API access and keys as well as know the account in which you want to tweet to.

### Running Locally

Clone the repository and make configuration changes as needed (see below) then run:

```bash
python setup.py install
```

Alternatively you can run this in the provided docker container.  First clone this repository and make configuratin changes as needed (see below) then run:

```
docker build --force-rm -t speedtweet .
docker run speedtweet
```

### Prerequisites

In order to use speedtweet you must have Twitter API Keys and know the account in which you want to tweet notifications to.

You can place these in the provided [speedtweet.yml](speedtweet.yml) configuration file or set environmental variables with this information:

```
twitter_consumer_key: 'KEY'
twitter_consumer_secret: 'SECRET'
twitter_access_token: 'TOKEN'
twitter_access_token_secret: 'TOKEN_SECRET'
speedtweet_at_account: "@SOMEINTERNETPROVIDERS ACCOUNT"
```

If you are using the provided Docker container then you should set these values in the configuration file.  You can set them in the Dockerfile but you must know what you are doing first.

You can set environmental variables locally using your shell:

```bash
export twitter_consumer_key="myvalue"
export twitter_consumer_secret="myvalue"
export twitter_access_token="myvalue"
export twitter_access_token_secret="myvalue"
export speedtweet_at_account="myvalue"
```

Or you can do so using Python:

```python
import os

os.environ['twitter_consumer_key'] = 'myvalue'
os.environ['twitter_consumer_secret'] = 'myvalue'
os.environ['twitter_access_token'] = 'myvalue'
os.environ['twitter_access_token_secret'] = 'myvalue'
os.environ['speedtweet_at_account'] = 'myvalue'
```

### Running

If you are using the Docker container then you can modify the [run.py](run.py) script to change different additional settings.  The `run` method of the SpeedTweet package contains additional configuration options regarding duration and thresholds.

These configuration options are listed below:

* interval = The interval in which to check internet speeds.  Default is 1 hour
* post_tweet = This will attempt to post a tweet.  Default is True.  False to just print out the results (good for testing)
* download_threshold = Your personal download threshold in mb.  Default is 500
* upload_threshold = Your personal upload threshold in mb.  Default is 30

## Built With

* [carcass](https://github.com/MSAdministrator/carcass) - Python packaging template

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* Josh Rickard - *Initial work* - [MSAdministrator](https://github.com/MSAdministrator)

See also the list of [contributors](https://github.com/MSAdministrator/speedtweet/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
