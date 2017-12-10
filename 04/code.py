
def isPassPhraseValid1(passphrase):
	w = passphrase.split()
	return len(w) == len(set(w))

def isAnagram(w1, w2):
	if len(w1)!=len(w2):
		return False
	for l in w1:
		if l not in w2:
			return False
	for l in w2:
		if l not in w1:
			return False		
	return True		


def isPassPhraseValid2(passphrase):
	w = []
	for p in passphrase.split():
		for i in w:
			if isAnagram(i, p):
				return False
		w.append(p)
	return True

valid1 = 0
valid2 = 0
with open('input') as f:
	for l in f.readlines():
		if isPassPhraseValid1(l):
			valid1 += 1
		if isPassPhraseValid2(l):
			valid2 += 1	
		

print valid1
print valid2

	