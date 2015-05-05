"""
test for main.py
"""
import getpass
from unittest import TestCase
from pyTona.main import Interface
from tests.ReqTracer import *

myInterface = Interface()
myInterface2 = Interface()


class TestInterface(TestCase):

    @requirements(['#0001', '#0002', '#0008', '#0009', '#0012'])
    def test_teach_no_previous_question(self):
        result = myInterface.teach('Your desk.')
        self.assertEqual(result, 'Please ask a question first')

    @requirements(['#0001', '#0002', '#0014', '#0016'])
    def test_correct_no_previous_question(self):
        result = myInterface2.correct('How are you>')
        self.assertEqual(result, 'Please ask a question first')

    @requirements(['#0001', '#0002', '#0010', '#0013'])
    def test_teach_who_invented_python(self):
        result = myInterface.teach('Who invented python>')
        self.assertEqual(result, 'I don\'t know about that. I was taught differently')

    @requirements(['#0001', '#0002', '#0008', '#0009'])
    def test_ask_unknown_question(self):
        result = myInterface.ask('Where am I>')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    @requirements(['#0001', '#0002', '#0019'])
    def test_ask_who_invented_python(self):
        result = myInterface.ask('Who invented python>')
        self.assertEqual(result, 'Guido Rossum(BFDL)')

    @requirements(['#0001', '#0002', '#0017'])
    def test_ask_distance(self):
        result = myInterface.ask('What is 5280 feet in miles>')
        self.assertEqual(result, '1.0 miles')

    @requirements(['#0001', '#0002', '#0021'])
    def test_ask_for_shutdown(self):
        result = myInterface.ask('Why don\'t you shut down>')
        self.assertEqual(result, "I'm afraid I can't do that {0}".format(getpass.getuser()))

    @requirements(['#0001', '#0002', '#0005', '#0020'])
    def test_ask_why_not_understood(self):
        result = myInterface.ask('Why don\'t you understand me>')
        self.assertEqual(result, 'Because you do not speak 1s and 0s')

    @requirements(['#0001', '#0002', '#0003'])
    def test_ask_not_a_question(self):
        result = myInterface.ask('Should I join the Dark Side>')
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0001', '#0002', '#0004'])
    def test_ask_not_a_question2(self):
        result = myInterface.ask('What if I join the Dark Side?')
        self.assertEqual(result, 'Was that a question?')

