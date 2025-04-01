import random

print("Do You Want To Encode Or Decode The Message?")
a = int(input("Type 1 For Encode Or 2 For Decode : "))

if (a<3) : 
   pass
else :
    print("Invalid Choice!")

random_chars = 'abcdefghijklmnopqrstuvwxyz'

if (a==1):
    encode = str(input("Enter The Message You Want To Encode : "))
    encode_message = encode[1:] + encode[0]
    random_chars_start = ''.join(random.choices(random_chars , k = 3))
    random_chars_end = ''.join(random.choices(random_chars , k = 3))
    print(random_chars_start + encode_message + random_chars_end)

elif (a==2):
    decode = str(input("Enter The Message You Want To Decode : "))
    if len(decode) < 7 :
            print("Too Short Message")
            if decode == 0 :
                 print("Nothing To Be Found")
    decode_message = decode[3:-3] 
    decode_message = decode_message[-1] + decode_message[:-1]
    print(decode_message)