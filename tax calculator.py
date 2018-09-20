taxbr = [9000, 25000, 41500, 61500]
tax = [0.07, 0.14, 0.25, 0.33]


def taxincome(income, taxbrackets, tax):
	ti = 0
	for i in range(len(taxbr)-1):
		print('iteration: %i \t income: %i \t tax: %i%%' %(i, taxbrackets[i], 100*tax[i]))
		print('------------------------------------------')
		if income > taxbrackets[i] and income > taxbrackets[i+1]:
			print('brackets: %i & %i #1' %(taxbrackets[i], taxbrackets[i+1]))
			ti += tax[i] * (taxbrackets[i+1] - taxbrackets[i])
			print('taxable income %.2f' %ti)
			if income > taxbrackets[i+1] and i ==len(taxbr)-2:
				print('\nbracket: >%i #3' %taxbrackets[i+1])
				ti += tax[i+1]*(income-taxbrackets[i+1])
				print('taxable income %.2f' %ti)
		elif income > taxbrackets[i] and income <= taxbrackets[i+1]:
			print('brackets: %i & %i #2' %(taxbrackets[i], taxbrackets[i+1]))
			ti += tax[i]*(income-taxbrackets[i])
			print('taxable income %.2f' %ti)
		print('------------------------------------------\n')

taxincome(80000,taxbr,tax)