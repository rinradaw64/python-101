# Python-101 Return to fizzbuzz
#  1. mod 3 == 0 -> Fizz
#  2. mod 5 == 0 -> Buzz
#  3. mod 3,5  == 0 -> fizzbuzz
#  4. mod 3,5 != 0 -> number

def fizzbuzz(number : int) -> str :
    strFizzBuzz = ''
    if(number % 3 == 0): strFizzBuzz = strFizzBuzz+'Fizz'
    if(number % 5 == 0): strFizzBuzz = strFizzBuzz+'Buzz'
    if(number % 5 != 0 and number % 3 != 0): strFizzBuzz = str(number)
    return strFizzBuzz


if __name__ == "__main__":
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))
    print(fizzbuzz(4))