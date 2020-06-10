import logging
import time

from .utils.exceptions import IncorrectParameters
__LOGGER__ = logging.getLogger(__name__)

from .runspeedtest import RunSpeedTest
from .twitterpost import TwitterPost


class Speed(object):

    def run(self, interval=3600, post_tweet=True, download_threshold=500, upload_threshold=30):
        while True:
            try:
                test_run = RunSpeedTest().execute()
                if test_run:
                    if test_run['download'] <= download_threshold or test_run['upload'] <= upload_threshold:
                        if post_tweet:
                            TwitterPost().post(
                                "{:.2f}".format(test_run['download']),
                                "{:.2f}".format(test_run['upload']),
                                100 * float(1000 - int(test_run['download']))/float(1000)
                            )
                        print('Download Speed is {:.2f}'.format(test_run['download']))
                        print('Upload Speed is {:.2f}'.format(test_run['upload']))
                        print('Percentage Below What Im paying: {}'.format(100 * float(1000 - int(test_run['download']))/float(1000)))
                else:
                    self.run()
            except:
                time.sleep(interval/2)
                self.run()
            time.sleep(interval)

    @property
    def speedtest(self):
        return RunSpeedTest().execute()
