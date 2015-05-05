Kevin Davis
cst236 spring '15
lab 4 write up


What observations did you make while performing the analysis on the system?
==================================================

Requirements coverage and requirements completeness seemed to mean the same thing.


What are the advantages/disadvantages of performing this analysis
===========================================

This analysis creates a systematic way of establishing some measurable level of confidence
in the system. It can also give data that can be tracked over time in a way that can indicate
development progress. However, development tends to be slow at first, accelerating over time.
For this reason, the data yielded through this analysis may be overly discouraging at first.


What are the advantages of data mutation? Did you use any of these tools?
================================================

With data mutation, situations that do not exist can be modeled for the purpose of testing. I did not
implement these tools.

What did you use Mock for in this lab?
========================

I attempted to use Mock to follow the following example:

def function_under_test():
    rx_data = socket.recv(255)
    data = parse_data(rx_data)
    return data

from mock import Mock

def test_rx_msg_process(self):
    socket.recv = Mock(return_value=0x123553)
    self.assertEqual(function_under_test(), value)
	
	
with this:

def get_other_users():
    try:
        host = '192.168.64.3'
        port = '1337'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"
		
	from mock import Mock

@requirements(['#0024', '#0025', '#0026', '#0027'])
    def test_get_other_users(self):
        s.recv = Mock(return_value='hello$other$users$list')             this threw an error until I changed s.recv to data
        self.assertEqual(get_other_users(), 'IT\'S A TRAAAPPPP')			but it still didnt seem to like the $ delimited string I gave it.

How long did this lab take to complete?
=========================

I spent about 5 hours on this lab.