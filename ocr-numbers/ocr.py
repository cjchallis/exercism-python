all = ['    _  _     _  _  _  _  _  _ ',
       '  | _| _||_||_ |_   ||_||_|| |',
       '  ||_  _|  | _||_|  ||_| _||_|', 
       '                              ']

dic = {' ':'0', '_':'1', '|':'2'}

num_hash = [''] * 10
for i in range(10):
	for j in range(3*i,3*i+3):
		for k in range(4):
			num_hash[i] += dic[all[k][j]]
	num_hash[i] = int(num_hash[i], 3)
	
num_hash = [num_hash[-1]] + num_hash[:-1]



ROW = 4
COL = 3

def number(ocr):
	return grid(ocr)
	
def grid(ocr):
	if len(ocr) != ROW or any(len(r) % COL for r in ocr):
		raise ValueError('Error in grid size.')
	nums = ''
	for i in range(len(ocr)/COL):
		hash = ''
		for j in range(COL*i, COL*(i+1)):
			for k in range(ROW):
				try:
					hash += dic[ocr[k][j]]
				except KeyError:
					hash += '?'
		try:
			nums += str(num_hash.index(int(hash, 3)))
		except ValueError:
			nums += '?'
		return nums
		
			
