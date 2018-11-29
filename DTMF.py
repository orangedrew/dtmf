import time
import sox

timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)


cbn = sox.Combiner()

infiles = []
outfile = timestr + ".wav"
wavFiles = [ "1.wav", "2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav"]

keys = [[" "], ["a", "b", "c"], ["d","e","f"], ["g","h","i"], ["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]


message = "ulyssis"

for i in message:
   #     print(i) 
        a = 0
        while i not in keys[a]:
            a = a + 1
        #print(keys[a])
        keyGroup = a 
   #     print(keyGroup)
        nbKeyPres = keys[a].index(i) + 1
   #     print(nbKeyPres) # amount of presses on keygroup
        for b in range(0,nbKeyPres):
   #         print(wavFiles[a])
            infiles.append(wavFiles[a])
        print(infiles)
cbn.build(
    infiles, outfile, 'concatenate'
    )

    
