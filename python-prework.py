def hello_name(username):

    print("Hello, " + username.title() + "!")
    
hello_name('george')


        
def odd_numbers(n):
    return [x for x in range(0, n+1) if x%2 != 0]
print(odd_numbers(100))  

def max_num_in_list( a_list ):
    max = a_list[ 0 ]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

def is_leap_year(a_year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0): 
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):

      leap = True
  else:
      leap = False
  return leap

def is_consecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))
      

lst = [2, 3, 1, 4, 5]
print(is_consecutive(lst))



