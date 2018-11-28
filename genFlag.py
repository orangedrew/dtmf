import time, wave
timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)

infiles = []
outfile = timestr + ".wav"
wavFiles = [ "1.wav", "2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav"]

keys = [[" "], ["a", "b", "c"], ["d","e","f"], ["g","h","i"], ["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]


message = "metadata"

for i in message:
	print(i) 
	a = 0
	while i not in keys[a]:
		a = a + 1

        print(keys[a])
       
        keyGroup = a 
        print(keyGroup)
        
        nbKeyPres = keys[a].index(i) + 1
        print(nbKeyPres) # amount of presses on keygroup
        for b in range(0,nbKeyPres):
            print(wavFiles[a])
            infiles.append(wavFiles[a])


        print(infiles)



data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
output.writeframes(data[0][1])
output.writeframes(data[1][1])
output.close()



