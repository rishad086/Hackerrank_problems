def print_formatted(number):
  i=1
  while i<=number:
      print(i,end=" ")
      o=oct(i).split("o")

      h=hex(i).split("x")

      b=bin(i).split("b")

      print(o[1], end=" ")
      print(h[1], end=" ")
      print(b[1], end=" ")
      print(" ")
      i+=1


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)