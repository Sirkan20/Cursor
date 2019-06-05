print('Lets check factorials')
number = int(input('Put your number here: '))
fib_number = 1
fib_number2 = 1
for i in  range(1, number+1):
	fib_number = fib_number*i
print('You put number {}, factorial is {}'.format(number, fib_number))

lens = len(str(fib_number))
print('Lens of digit is {} digits'.format(lens))

#lens_zip = zip(range(1, lens + 1),str(fib_number))
#print(dict(lens_zip))

