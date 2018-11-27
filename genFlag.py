##import wave
##
##infiles = ["sound_1.wav", "sound_2.wav"]
##outfile = "sounds.wav"
##
##data= []
##for infile in infiles:
##    w = wave.open(infile, 'rb')
##    data.append( [w.getparams(), w.readframes(w.getnframes())] )
##    w.close()
##
##output = wave.open(outfile, 'wb')
##output.setparams(data[0][0])
##output.writeframes(data[0][1])
##output.writeframes(data[1][1])
##output.close()

keys = [[" "], ["a", "b", "c"], ["d","e","f"], ["g","h","i"], ["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]



message = "metadata"

for i in message:
	print(i) 
	a = 0
	while i not in keys[a]:
		a = a + 1
	print(keys[a])
	print(keys[a].index(i) + 1)

