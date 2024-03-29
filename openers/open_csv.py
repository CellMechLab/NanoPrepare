
import openers._skeleton as skeleton

NAME = 'CSV'
EXT = '.csv'

class opener(skeleton.prepare_opener):
    def parse(self):
        f = open(self.filename)
        f.close()