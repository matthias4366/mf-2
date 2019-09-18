# A python program to create user-defined exception

# # class MyError is derived from super class Exception
# class MyError(Exception):
#
# 	# Constructor or Initializer
# 	def __init__(self, value):
# 		self.value = value
#
# 	# # __str__ is to print() the value
# 	# def __str__(self):
# 	# 	return(repr(self.value))
#
# try:
# 	raise(MyError(3*2))
#
# # Value of Exception is stored in error
# except MyError as error:
# 	print('A New Exception occured: ',error.value)

#===============================================================================
from measuredfood.utils.error.custom_error import \
    NoValueForTargetedNutrientError

try:
    raise(NoValueForTargetedNutrientError(['protein', 'carbs']))

except NoValueForTargetedNutrientError as e:
    print('There were no values for the nutrients:', e.nutrient_value_missing)
