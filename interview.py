# word="AAABBCCCCDDDEE"

# def calculate_occurrences(word):
#     freq={}
#     for i in word:
#         if i not in freq:
#             freq[i]=1
#         else:
#             freq[i]+=1

#     new_str=""
#     for keys in freq:
#         new_str+=keys
#         new_str+=str(freq[keys])
    
#     return new_str

# occurrences=calculate_occurrences(word)

# print(occurrences)




def longest_palindrome(s):
    palindromic_substring=""
    max_length=0
    left=0
    for right in range(1,len(s)):
        curr_substring=s[left:right+1]
        if curr_substring[::-1]==curr_substring:
            palindromic_substring=curr_substring
            max_length=max(len(palindromic_substring),max_length)
        else:
            left+=1

    print(palindromic_substring)

word="BBAEAARRS"



def is_palindrome(s):
    return s==s[::-1]

def longest_palindrome(s):
    ans=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub=s[i:j+1]

            if is_palindrome(sub) and len(sub)>len(ans):
                ans=sub
    return ans

func_call=longest_palindrome(word)
print(func_call)






        

    



