# Exception Handling
# Error handling

# An error is handled by using try except

# try:
# In try block, we write the code that may arise an error
# if error came in try block, except block will be executed
# If error didnot came, try block will be executed

# except:
# code to be executed if error arise in try block


# General error handling
# try:
#     list1 = [1,2,3,4,6,7,8,9]
#     print(list1[1])
#     num1 = int(input("ENter a number: "))
#     num2 = int(input("ENter a number: "))
#     print(num1/num2)
# except:
#     print("List doesnot have the provided index")
# Try block never comes alone, except should come with try block


# Specific error handling
# try:
#     list1 = [1,2,3,4,6,7,8,9]
#     print(list1[1])
#     num1 = int(input("ENter a number: "))
#     num2 = int(input("ENter a number: "))
#     print(num1/num2)
    
# except IndexError:
#     print("List doesnot have the provided index")
    
# except ValueError:
#     print("Cannot convert to int data type")
    
# except:
#     print("An error occured")


# Specific error handling with custom value
# try:
#     list1 = [1,2,3,4,6,7,8,9]
#     print(list1[1])
#     num1 = int(input("ENter a number: "))
#     num2 = int(input("ENter a number: "))
#     print(num1/num2)
#     file = open("aaa.txt","r")
#     file.close()

# except Exception as e:
#     print(f"An error occured: {e}")


# Nested Try except
try:
    try:
        try:
            pass
        except:
            pass
    except:
        try:
            pass
        except:
            pass
except:
    try:
        try:
            pass
        except:
            pass
    except:
        try:
            pass
        except:
            pass
        
        
# Finally block
# finally block is always executed 
# Whether error arise or not

try:
    list1 = [1,2,3,4,6,7,8,9]
    print(list1[1])
    num1 = int(input("ENter a number: "))
    num2 = int(input("ENter a number: "))
    print(num1/num2)

except Exception as e:
    print(f"An error occured: {e}")
    
finally:
    print("This is executed anyways.")
    
# TAsk:
# Update the programs till we did by using try except
# Handle the error for all the programs dome till now
