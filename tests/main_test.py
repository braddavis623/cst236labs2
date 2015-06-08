"""
test for main.py
"""
import getpass
import threading
import os
from unittest import TestCase
from pyTona.main import Interface
from tests.ReqTracer import *
from pyTona.answer_funcs import *
from mock import Mock, patch, MagicMock

myInterface = Interface()
myInterface2 = Interface()


class TestInterface(TestCase):

    @requirements(['#0001', '#0002', '#0008', '#0009', '#0012'])
    def test_teach_no_previous_question(self):
        result = myInterface.teach('Your desk.')
        self.assertNotEqual(result, 'Please ask a question first')

    @requirements(['#0001', '#0002', '#0014', '#0016'])
    def test_correct_no_previous_question(self):
        result = myInterface2.correct('How are you?')
        self.assertEqual(result, 'Please ask a question first')

    @requirements(['#0024', '#0025', '#0026', '#0027'])
    def test_get_other_users(self):
        data = Mock(return_value='hello$other$users$list')
        self.assertEqual(get_other_users(), 'IT\'S A TRAAAPPPP')

    @requirements(['#0024', '#0025', '#0026', '#0027'])
    def test_get_other_users(self):
        data = Mock(return_value='hello$other$users$list')
        self.assertEqual(get_other_users(), 'IT\'S A TRAAAPPPP')

    @requirements(['#0002', '#0010', '#0013'])
    def test_teach_who_invented_python(self):
        result = myInterface.teach('Who invented python?')
        self.assertEqual(result, 'I don\'t know about that. I was taught differently')

    @requirements(['#0002', '#0008', '#0009', '#0022'])
    def test_ask_where_am_I_known(self):
        result = myInterface.ask('Where am I?')
        self.assertEqual(result, 'lab5')

    @requirements(['#0001', '#0002', '#0019'])
    def test_ask_who_invented_python(self):
        result = myInterface.ask('Who invented python?')
        self.assertEqual(result, 'Guido Rossum(BDFL)')

    @requirements(['#0002', '#0017'])
    def test_ask_distance(self):
        result = myInterface.ask('What is 5280 feet in miles?')
        self.assertEqual(result, '1.0 miles')

    @requirements(['#0001', '#0002', '#0021'])
    def test_ask_for_shutdown(self):
        result = myInterface.ask('Why don\'t you shut down?')
        self.assertEqual(result, "I'm afraid I can't do that {0}".format(getpass.getuser()))

    @requirements(['#0002', '#0005', '#0020'])
    def test_ask_why_not_understood(self):
        result = myInterface.ask('Why don\'t you understand me?')
        self.assertEqual(result, 'Because you do not speak 1s and 0s')

    @requirements(['#0002', '#0003'])
    def test_ask_not_a_question(self):
        result = myInterface.ask('Should I join the Dark Side?')
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0001', '#0002', '#0004'])
    def test_ask_not_a_question2(self):
        result = myInterface.ask('What if I join the Dark Side?')
        self.assertNotEqual(result, 'Was that a question?')

    @requirements(['#0030'])
    def test_million_questions(self):
        question = "Question {0}"
        answer = "Asnwer {0}"

        for i in range(0, 1000000, 1):
            myInterface.last_question = question.format(i)
            myInterface.correct(answer.format(i))
        self.assertGreaterEqual(len(myInterface.question_answers), 1000000)

    @requirements(['#0031'])
    def test_time_5ms(self):
        myInterface.ask("When are we?")
        time1 = time.clock()
        myInterface.teach("The present.")
        time2 = time.clock()
        self.assertLessEqual((time2 - time1) * 1000, 5)

    @requirements(['#0034'])
    def test_do_1000_fib_in1min(self):
            start = time.clock()
            for i in range(0,1000):
                myInterface.ask("What is the {0} digit of the fibonacci sequence?".format(i))
            end = time.clock()

            self.assertLessEqual((end - start), 60000)

    @requirements(['#0035'])
    def test_HD_access(self):
        myInterface.ask("Can you find some stuff?")
        self.assertEqual(os.stat('stuff.txt').st_size,15L)