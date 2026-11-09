print("Roll No.: 0863CS241039")
print("Name: Anushka Porwal")

def check_palindrome(string):
    dict={}
    odd=0
    for i in text    :#aabb
        if i not in dict:
            dict[i]=1 #[i:1] # a:2 #a:2,b:1
        else:
            dict[i]+=1

    for a in dict.values():
        if a % 2 == 1:
            odd += 1

    return odd <= 1

text=input("Enter a string: ")
if check_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")