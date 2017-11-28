import winsound

myname = 'fred'
guess = ''
while guess != myname:
	guess = input ('What is my name?')
	print('that is not my name, try again.')
else:
	print('Correct!')
	winsound.PlaySound("DeviceConnect", winsound.SND_ALIAS)
