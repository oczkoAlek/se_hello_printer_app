import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
import xml.etree.cElementTree as ET
import json


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
        expected = {'imie': 'Ola1', 'msg': 'Hello World!'}
        actual = json.loads(rv.data)
        self.assertEqual(expected['imie'], actual['imie'])
        self.assertEqual(expected['msg'], actual['msg'])

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        greetings = ET.Element("greetings")
        lx_name = ET.SubElement(greetings, "name")
        lx_name.text = 'Ola1'
        lx_msg = ET.SubElement(greetings, "msg")
        lx_msg.text = 'Hello World!'
        s = ET.tostring(greetings)

        self.assertEqual(s, rv.data)
