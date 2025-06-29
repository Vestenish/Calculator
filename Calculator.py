while True:
    try:
      user_input = input("Please enter an operation: ")
      result = eval(user_input)  # The result of the user's operation
      print(result)              # Print the result
      if isinstance(result, (float, int)):
       print("Operation successful.")
       break
      else:
        print("Operation failed.")
    except (ValueError, TypeError, ZeroDivisionError, SyntaxError, NameError):
        print("Please enter a valid mathematical operation.")
