from pywinauto import application

import time

app = application.Application()
	
	#Test 1 @requirements(['#0003', '#0004', '#0006', '#0008'])

app.start_('sharpTona')
app.sharpTona.TypeKeys("What {SPACE} is {SPACE} the {SPACE} answer {SPACE} to {SPACE} everything?")
time.sleep(0.25)	
app.sharpTona.Ask.Click()
time.sleep(0.25)
result = app.sharpTona['Answer:Edit '].Texts()[0]
time.sleep(0.25)
if result != '42':
	print 'Test 1 failed'
else:
	print 'Test 1 passed'
app.sharpTona.TypeKeys("%{F4}")

	#Test 2 @requirements(['#0005])
app = application.Application()
app.start_('sharpTona')
cor = app.sharpTona.Correct.IsEnabled()
tch = app.sharpTona.Teach.IsEnabled()
if cor or tch:
	print 'Test 2 failed'
else:
	print 'Test 2 passed'
app.sharpTona.TypeKeys("%{F4}")

	#Test 3 @requirements(['#0007'])
app.start_('sharpTona')
time.sleep(0.5)
app.sharpTona.Ask.Click()
good = 'Was that a question?'
result = app.sharpTona['Answer:Edit '].Texts()[0]
if result != good:
	print 'Test 3 failed'
else:
	print 'Test 3 passed'
app.sharpTona.TypeKeys("%{F4}")

	#Test 4 @requirements(['#0008'])
app.start_('sharpTona')
app.sharpTona.TypeKeys("What {SPACE} is {SPACE} the {SPACE} answer {SPACE} to {SPACE} everything?")
time.sleep(0.25)	
app.sharpTona.Ask.Click()
time.sleep(0.25)
result = app.sharpTona['Question:Edit '].IsEnabled()
time.sleep(0.25)
if result != True:
	print 'Test 4 failed'
else:
	print 'Test 4 passed'
app.sharpTona.TypeKeys("%{F4}")


	#Test 5 @requirements(['#0009'])
app.start_('sharpTona')
app.sharpTona.TypeKeys("What {SPACE} is {SPACE} the {SPACE} answer {SPACE} to {SPACE} everything?")
time.sleep(0.25)	
app.sharpTona.Ask.Click()
time.sleep(0.25)
app.sharpTona['Answer:Edit '].TypeKeys('3')
time.sleep(0.25)
app.sharpTona.Correct.Click()
ans = app.sharpTona['Answer:Edit '].IsEnabled()
cor = app.sharpTona.Correct.IsEnabled()
tch = app.sharpTona.Teach.IsEnabled()
if ans or cor or tch:
	print 'Test 5 failed'
else:
	print 'Test 5 passed'
app.sharpTona.TypeKeys("%{F4}")

	#Test 6/7 @requirements(['#0010', '#0011'])
app.start_('sharpTona')
app.sharpTona.TypeKeys("Where {SPACE} am {SPACE} I?")
time.sleep(0.25)	
app.sharpTona.Ask.Click()
time.sleep(0.25)
good = 'I don\'t know please teach me.'
result = app.sharpTona['Answer:Edit '].Texts()[0]
time.sleep(0.25)
tch = app.sharpTona.Teach.IsEnabled()
if (result == good) and tch:
	print 'Test 6 passed'
else:
	print 'Test 6 failed'
app.sharpTona['Answer:Edit '].TypeKeys("At home")
app.sharpTona.Teach.Click()
tc = app.sharpTona.Teach.IsEnabled()
an = app.sharpTona['Answer:Edit '].IsEnabled()
cr = app.sharpTona.Correct.IsEnabled()
if tc or an or cr:
	print 'Test 7 failed'
else:
	print 'Test 7 passed'
app.sharpTona.TypeKeys("%{F4}")