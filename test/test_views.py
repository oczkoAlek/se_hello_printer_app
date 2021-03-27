import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        # TODO: compare actual and expected as JSONs
        self.assertEqual(b'{ "imie":"Ola", "mgs":Hello World!"}', rv.data)

#    def test_msg_with_output_xml(self):
#        rv = self.app.get('/?output=xml')

        # TOOO: compare expected and actual as XMLs
#        self.assertEqual(
        #    b"""<greetings>
        #    \t<name>Ola</name>\n\t<msg>Hello World!</msg>\n</greetings>""",
        #    rv.data)
