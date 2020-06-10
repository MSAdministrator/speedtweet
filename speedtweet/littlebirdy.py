import yaml
import os


class LittleBirdy(object):

    yaml_config = 'speedtweet.yml'

    def __init__(self):
        self.__get_config()

    def __get_config(self):
        # Check for yaml config first
        if os.path.exists(self.yaml_config):
            with open(os.path.abspath(self.yaml_config), 'r') as f:
                self.config = yaml.load(f, Loader=yaml.BaseLoader)
        elif os.environ.get('twitter_consumer_key'):
            self.config = {
                'twitter_consumer_key': os.environ.get('twitter_consumer_key'),
                'twitter_consumer_secret': os.environ.get('twitter_consumer_secret'),
                'twitter_access_token': os.environ.get('twitter_access_token'),
                'twitter_access_token_secret': os.environ.get('twitter_access_token_secret'),
                'speedtweet_duration': os.environ.get('speedtweet_duration', 3600),
                'speedtweet_at_account': os.environ.get('speedtweet_at_account')
            }
        else:
            raise EnvironmentError('Unable to find either the {} yaml config or environmental variables'.format(self.yaml_config))
