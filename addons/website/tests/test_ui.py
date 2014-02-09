import os
import glob

import openerp

fname, _ = os.path.splitext(__file__)

class TestUiAdmin(openerp.tests.HttpCase):
    def test(self):
        for i in glob.glob('%s_admin_*.js' % fname):
            self.phantomjs(i) 

class TestUiPublic(openerp.tests.HttpCase):
    def test(self):
        for i in glob.glob('%s_public_*.js' % fname):
            self.phantomjs(i) 

