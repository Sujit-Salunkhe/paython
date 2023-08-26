# print(k)
# sujit="KingKhanK"
# print(sujit.index("K",0))
# s="BANANA"

            
# substring(s)
        

# def extract_substrings(s):
#     k = []
#     vowels = ["a", "e", "i", "o", "u"]
#     t = 0
#     for char in s:
#         if char.lower() in vowels:
#             k.append(s[t:])
#             t = s.index(char, t) + 1

#     valid_substrings = []
#     for i in range(len(k)):
#         if len(k[i]) == 1:
#             continue
#         if any(char in vowels for char in k[i]):
#             valid_substrings.append(k[i])

#     return valid_substrings

# s = "BANANA"
# result = extract_substrings(s)
# print(result)
# def extract_substrings(s):
#     k = []
#     vowels = ["a", "e", "i", "o", "u"]
#     t = 0
#     for char in s:
#         if char.lower() in vowels:
#             k.append(s[t:])
#             t = s.index(char, t) + 1

#     valid_substrings = []
#     for i in range(len(k)):
#         if any(char in vowels for char in k[i]):
# #             valid_substrings.append(k[i])

# #     return valid_substrings

# # def is_valid_substring(substring):
# #     return substring.count("A") + substring.count("E") + substring.count("I") + substring.count("O") + substring.count("U") >= 2

# # s = "BANANA"
# # result = extract_substrings(s)

# # valid_result = [substring for substring in result if is_valid_substring(substring)]
# # print(valid_result)
# def extract_substrings(s):
#     k = []
#     vowels = ["a", "e", "i", "o", "u"]
#     t = 0
#     for char in s:
#         if char.lower() in vowels:
#             k.append(s[t:])
#             t = s.index(char, t) + 1
#     return k

# def is_valid_substring(substring):
#     vowels_count = sum(substring.count(vowel) for vowel in "AEIOUaeiou")
#     return vowels_count >= 1 and len(substring) > 1
    # any_vowels=any(char in vowels for char in k[i])
    # for i in range(len(k)):
    #     if len(k[i]) == 1:
    #         return ()
    #     if (any_vowels):
    #         substring(k[i])
    #     else:
    #         return ()
    # print(k)

# s = "BANANA"
# substrings = extract_substrings(s)

# valid_substrings = [substring for substring in substrings if is_valid_substring(substring)]
# print(valid_substrings)
s="BANANA"






