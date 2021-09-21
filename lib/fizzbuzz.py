def fizzbuzz(i):
  if i % 3 == 0:
    return 'Fizz'
  else:
    return i

def main():
  for i in range(1, 101):
    print(fizzbuzz(i))

if __name__ == '__main__':
  main()