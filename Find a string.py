def count_substring(string, sub_string):
  c=0
  for i in range(len(string)-len(sub_string)+1):
    if(i+len(sub_string))<=len(string):
      #print(string[i:i+len(sub_string)])
      if string[i:i+len(sub_string)]==sub_string:
        c=c+1
  return c










if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)