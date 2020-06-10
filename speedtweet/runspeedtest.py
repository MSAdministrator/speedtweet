import json
import subprocess


class RunSpeedTest(object):

    def execute(self):
        return_data = json.loads(subprocess.check_output(['speedtest-cli', '--json']))
        return {
            'download': return_data['download'] / 1048576,
            'upload': return_data['upload'] / 1048576
        }