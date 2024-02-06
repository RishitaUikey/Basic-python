'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' '''

def swap_string(str1,str2):
    
    str1_first_2=str1[:2]
    str2_first_2=str2[:2]

    new_str1 = str2_first_2 + str1[2:]
    new_str2 = str1_first_2 + str2[2:]

    result = new_str1 + ' ' + new_str2

    return result
sample_str1='abc'
sample_str2='xyz'
result = swap_string(sample_str1,sample_str2)

print("Expected Result : ",result)
