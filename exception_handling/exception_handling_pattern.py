def show_exceptions():
    """
    Show exception handling patterns
    :return:
    """
    file =None
    try:
        # File is being opened
        file = open('input-file', 'open mode')
    except FileNotFoundError as fe:
        # When File is Not Found
        print("Caught the File Not Found error.")
        raise fe
    except EOFError as ex:
        # When End of file has been reached and
        # Still there is an effort to read more
         print("Caught the EOF error.")
         raise ex
    except IOError as ie:
        # Issue in File handling
         print("Caught the I/O error.")
         raise ie
    finally:
        print('I am here now')
        # File object exists and it has to be closed for resource clean up
        if(file!=None):
            file.close()


# Exception Handling Extra:
def show_exception_extra():
    """
    Some Extra things in Exception Handling
    :return:
    """
    try:
        num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
        result = num1 / num2
        print("Result is", result)
    except ZeroDivisionError:
        # When the denominator is zero(0)
        print("Division by zero is error !!")
    except SyntaxError:
        # Comma is missing in the input
        print("Comma is missing. Enter numbers separated by comma like this 1, 2")
    except:
        print("Wrong input")
    else:
        print("No exceptions")
    finally:
        print("This will execute no matter what")

# Best Practice for manually raising exceptions
def show_manual_exception_handling():
    """
    Manually raise an exception and handle it accordingly
    :return:
    """
    try:
        raise ValueError('Testing exceptions: The input is in incorrect order', 'one', 'two', 'four')
    except ValueError as err:
        print(err.args)


# show_exceptions()
# show_exception_extra()
show_manual_exception_handling()
