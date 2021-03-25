###solution to exercise 98 from ben stephenson's "the python workbook".

def hex2int(hex_):

  digits = {  '0':  0,
              '1':  1,
              '2':  2,
              '3':  3,
              '4':  4,
              '5':  5,
              '6':  6,
              '7':  7,
              '8':  8,
              '9':  9,
              'A':  10,
              'B':  11,
              'C':  12,
              'D':  13,
              'E':  14,
              'F':  15  }

  result = 0
  hex_ = hex_[::-1].upper()
  for n in range(len(hex_)):
    result += digits[hex_[n]] * 16 ** n

  return result

def int2hex(int_):

  digits = {  0:  '0',
              1:  '1',
              2:  '2',
              3:  '3',
              4:  '4',
              5:  '5',
              6:  '6',
              7:  '7',
              8:  '8',
              9:  '9',
              10: 'A',
              11: 'B',
              12: 'C',
              13: 'D',
              14: 'E',
              15: 'F' }

  if int_ in digits.keys():
    return digits[int_]
  else:
    raise ValueError('Integer is not convertible to a hex digit!')
