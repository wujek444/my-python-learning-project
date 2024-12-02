spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

#types
print("----------types-test----------------")
print("type(\"string of characters\"): " + str(type("string of characters")))
print("type(1.0):" + str(type(1.0)))
print("type(None): " + str(type(None)))
print("type(10000): " + str(type(10000)))

#arithmetic operations
print("----------arithmetic-operations----------------")
print("5 // 2 = " + str(5 // 2)) #floor division
print("5 / 2 = " + str(5 / 2)) #division
print("5 ** 2 = " + str(5 ** 2)) #power

#built-in number functions
print("----------built-in-number-functions----------------")
print("min(0.312312221, 0.211111111, 0.000000002121212)=" + str(min(0.312312221, 0.211111111, 0.000000002121212)))
print("max(0.312312221, 0.211111111, 0.000000002121212)=" + str(max(0.312312221, 0.211111111, 0.000000002121212)))
print("abs(-21345)=" + str(abs(-21345)))

#type conversions
print("----------type-conversions----------------")
print("int(\"2345\"): " + str(int("2345")))
print("float(2345): " + str(float(2345)))
print("implicit conversion test: 2 + 0.56 = " + str(2 + 0.56))
#print("test" + 2) #will result in error

##calling print() with additional parameters
print("----------calling-print----------------")
help(print)
print("Test1", "Test2", sep='; ')