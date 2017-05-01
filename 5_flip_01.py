"""You are given an integer array with N elements: d[0], d[1], ... d[N - 1]. 
You can perform AT MOST one move on the array: choose any two integers [L, R], and flip all the elements between (and including) the L-th and R-th bits. L and R represent the left-most and right-most index of the bits marking the boundaries of the segment which you have decided to flip.

What is the maximum number of '1'-bits (indicated by S) which you can obtain in the final bit-string? """

mylist = [1, 0, 0, 1, 0, 0 ,1 ,0 ]
#mylist = [1, 0, 1 ]
mylist = [1, 1, 1, 1, 1, 1 ,1 ,1 ]
mylist = [0, 0, 0, 0, 0, 0 ,0 ,0 ]
#mylist = [0, 0, 0, 1, 0, 0 ,0 ,0 ]


def flip_max_one(arr):
   count_zero = 0
   count_one = 0

   for i in range (0, len(arr)):
      if arr[i] == 0:
        count_zero = count_zero + 1
      else:
        count_one = count_one + 1

   if count_zero > count_one :
     return count_zero
   else:
     return count_one

def find_max_one(arr):
   count_one = 0
   
   for i in range (0, len(arr)):
      if arr[i] == 1:
        count_one = count_one + 1

   return count_one        

def get_max_len(arr):
   left = 0;
   right = 0;
   maxone = 0
   for i in range (0, len(arr)+1):
      #print "i=",i
      for j in range (0, i+1):
         temp = find_max_one(arr[0:j]) + flip_max_one(arr[j:i]) + find_max_one(arr[i:])
         #print "  i=%s, j=%s [0:j]=%s [i:j]=%s [i:]=%s" % ( i, j, find_max_one(arr[0:j]), flip_max_one(arr[j:i]), find_max_one(arr[i:]))
       
         if temp > maxone:
            maxone = temp
            left = j
            right = i 
            print "    ***temp", maxone, left, right

   return [maxone, left, right]

print mylist
print flip_max_one(mylist)
print find_max_one(mylist)
print get_max_len(mylist)   
