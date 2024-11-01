def is_palindrome(s): 
 # remove the unless character 
 cleaned_str =""
 for char in s:
  if char.isalpha(): # only alphabate 

    cleaned_str += char.lower()


 # chack the word is palindrome or not

    left,right =0 ,len(cleaned_str)-1 
    while left<right:
      if cleaned_str[left] != cleaned_str[right]:
        return False
      
      left += 1
      right -= 1

    return True
    

my_inpurt = input("Enter a word")

if is_palindrome(my_inpurt):
  print("its is palindrome")

else :
  print("not palindrome")




    