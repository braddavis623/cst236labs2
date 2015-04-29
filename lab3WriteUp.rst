Kevin Davis
cst236 spring '15
lab3 write up

Five useful plugin examples
===========================

I'm not sure, I have mostly been trying to learn how everything else in the 
class fits together.

Plans for plugin creation
=========================

At this point I will likely be scaling the project back to requirements I 
write tests for and then implement code for.

The hardest part of the lab
===========================

Implementing a plugin. It was an exciting idea, but I wasn't sure how to 
go about naming it, (spent a while trying to figure out what 'configSection'
was and how to use it) or what data or methods I'd have access to. What I imagined
was a simpl open a file, figure out how to use 'requirements' to get data
to write to the file. It seems that file IO would be straightforward in python
once I figured out how it was done. I also made the mistake of creating a lab3
directory in my labs file on my machine, and now git/github are a mess.


Rqquirements implementation
===========================

The code did not implement the requirements fully. The tests revealed several bugs that 
are outlined in the bug report.

Requirements completeness
=========================

The requirements were incoplete as they did not specify some useful portions 
of the code. One example of this is that there is no requirement that would  
lead to testing the ability of the code to rais the exception: "not a string"
found on line 34 of main.py


Bug report
==========

+--------------------------------------------------------------------------------------------+
| | **Issue Number:** 1                                                                      |
+--------------------------------------------------------------------------------------------+
| | **Brief:**                                                                               |
| | no previous question, improper response                                                  |
+--------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                  |
| | before asking the system a question, attempt to provide it an answer                     |
+--------------------------------------------------------------------------------------------+
| | **Comments:**                                                                            |
| | the system will respond as though you are trying to update an answer it already has stor |
| | ed                                                                                       |
+--------------------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------------------------------------------------------+
| | **Issue Number:** 2                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------+
| | **Brief:**                                                                                                                  |
| | Who invented python, improper response                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                                                     |
| | ask the system who invented python                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------+
| | **Comments:**                                                                                                               |
| | the system will respond with:                                                                                               |
| | Guido Rossum(Benevolent Dictator For Life)                                                                                  |
| | not:                                                                                                                        |
| | Guido Rossum(BFDL)                                                                                                          |
| | as specified in requirements                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------+
| | **Issue Number:** 3                                                         |
+-------------------------------------------------------------------------------+
| | **Brief:**                                                                  |
| | converting feet to miles, improper response                                 |
+-------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                     |
| | ask the system about a distance of 5280 feet                                |
+-------------------------------------------------------------------------------+
| | **Comments:**                                                               |
| | the system will respond:                                                    |
| | 1.0                                                                         |
| | not:                                                                        |
| | 1.0 miles, as specified by the requirements                                 |
+-------------------------------------------------------------------------------+


Requirements tracing
====================

Requirements tracing is a way to ensure that test writing and code writing are bound
to the requirements. It keeps programmers from writing code that may be nice, but 
isn't required, and it allows test writers to know when they have tested the code with
some measure of completeness. It also establishes a conflict resolving systed, wherby
testers and coders can refer to the requirements when resolving a dispute.

Time on this lab
================

I have spent about 8~9 hours on this lab. Had I allowed ~12 hours, I think I 
could have done better.

repo url (its a mess, so I'll also send you a .zip until I can get git sorted)

