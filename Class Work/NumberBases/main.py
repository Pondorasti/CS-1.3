def decimal_to_binary(number):
  binary = ""
  while number:
    binary += str(number % 2)
    number //= 2

  return binary[::-1]

def binary_to_decimal(number):
  pow = 0
  decimal = 0
  
  while number:
    decimal += number % 10 * 2 ** pow
    pow += 1
    number //= 10

  return decimal

def encodeNumber(number: int, base: int) -> str:
  def normalize(number: int) -> str:
    if number < 10:
      return str(number)

    ascii_start = 65 # A
    offset = number % 10
    return chr(ascii_start + offset)

  new_number = ""
  while number:
    new_digit = normalize(number % base)
    new_number += new_digit
    number //= base
  
  return new_number[::-1]

def decodeNumber(number: str, base: int) -> int:
  def normalize(digit: str) -> int:
    if digit.isdigit():
      return int(digit)

    ascii_start = 65 # A
    return 10 + ord(digit) - ascii_start

  pow = 0
  new_number = 0

  while number:
    digit = normalize(number[-1])
    new_number += digit * base ** pow
    pow += 1
    number = number[:-1]

  return new_number
    



print(decimal_to_binary(10))
print(decimal_to_binary(16))
print(decimal_to_binary(23))

print()

print(binary_to_decimal(1010))
print(binary_to_decimal(10000))
print(binary_to_decimal(10111))

print()

print(encodeNumber(10, 2))
print(encodeNumber(23, 3))
print(encodeNumber(223, 16))
print(encodeNumber(1009, 16))

print()

print(decodeNumber("1010", 2))
print(decodeNumber("212", 3))
print(decodeNumber("DF", 16))
print(decodeNumber("3F1", 16))
