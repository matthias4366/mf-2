import re
from make_number_from_national_institute_of_health_str import \
    make_number_from_national_institute_of_health_str

# TODO: Make a test for the function
#  make_number_from_national_institute_of_health_str instead. Then, delete
#  this learning file.

str_ = '!!3451.334GG534*h'
str_manipulated = \
    make_number_from_national_institute_of_health_str(
        str_,
        re,
    )
print('str_manipulated')
print(str_manipulated)

# initializing bad_chars_list
bad_chars = [';', ':', '!', "*"]

# initializing test string
test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string
print("Original String : " + test_string)

# using replace() to
# remove bad_chars
for i in bad_chars:
    test_string = test_string.replace(i, '')

# printing resultant string
print("Resultant list is : " + str(test_string))