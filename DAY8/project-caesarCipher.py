# def encode(word,shift):
#     new_word = ""
#     for char in word:
#         new_index = letters.index(char)+shift
#         if(new_index>25):
#             new_index = new_index-26
#         new_word+=letters[new_index]
#     return new_word

# def decode(word,shift):
#     original=""
#     for char in word:
#         new_index = letters.index(char)-shift
#         # Since in python we are having negative indexing 
#         # if(new_index<0):
#         #     new_index = 26+new_index
#         original+=letters[new_index]
#     return original   

def caesar(operation, word, shift):
    new_word = ""
    if (operation == "encode"):
        for char in word:
            new_index = letters.index(char) + shift
            if (new_index > 25):
                new_index = new_index - 26
            new_word += letters[new_index]
    elif (operation == "decode"):
        for char in word:
            new_index = letters.index(char) - shift
            # Since in python we are having negative indexing 
            # if(new_index<0):
            #     new_index = 26+new_index
            new_word += letters[new_index]
    print(new_word)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
operation = input("Enter the operation to be performed either encode or decode : ")
word = input("Enter the message to be encoded : ").lower()
shift = int(input("Enter the shift value : "))
caesar(operation, word, shift)
