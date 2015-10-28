import os
for filename in os.listdir('R:/Digitization/Audio/Vendor Digitization/Reel-to-Reel Project/' + 'Batch 1/20130218' + '/' + '8738' + '/' + '8738-SR-1-1-1'):
	if filename.endswith('.jpg'):
		print filename
