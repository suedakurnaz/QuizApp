quiz_data = [
   {
        "topic": "Python Introduction",
        "question": "Which of the following is not a common use case for Python?",
        "choices": ["Web development", "Mobile game development", "Data science", "Artificial intelligence"],
        "answer": "Mobile game development"
    },
    {
        "topic": "Python Introduction",
        "question": "Which of the following is one of the main reasons why Python is widely used?",
        "choices": ["It is a low-level language", "It has complex syntax", "It is easy to read and write", "It only works on Windows"],
        "answer": "It is easy to read and write"
    },
    {
        "topic": "Python Get Started",
        "question": "Which command is correct for running a file named hello.py in the terminal?",
        "choices": ["python run hello.py", "execute hello.py", "python hello.py", "launch hello.py"],
        "answer": "python hello.py"
    },
    {
        "topic": "Python Get Started",
        "question": "After installing Python, which of the following is the best way to check if Python is successfully installed on your system?",
        "choices": ["Open a web browser and search for Python version", " Type python --version or python3 --version in the terminal", "Double-click any .py file", "Open Excel and search for Python tools"],
        "answer": "Type python --version or python3 --version in the terminal"
    },

    {
        "topic": "Python Syntax",
        "question": "How does Python determine the end of a command line?",
        "choices": ["Semicolon (;)", "Comma (,)", "New line (Enter)", "Curly braces {}"],
        "answer": "New line (Enter)"
    },

    {
        "topic": "Python Syntax",
        "question": "Why does the following code produce an error?\nif x > 5 \nprint('Greater')",
        "choices": ["if should be replaced with when", "Missing colon : after the condition", "print is misspelled", "Variable x must be a string"],
        "answer": "Missing colon : after the condition"
    },

    {
        "topic": "Python Comments",
        "question": "What is the main purpose of using comments in Python code?",
        "choices": ["To make the code run faster", "To explain the code for human readers", "To debug syntax errors", "To save memory"],
        "answer": "To explain the code for human readers"
    },

    {
        "topic": "Python Comments",
        "question": "Which of the following is a correct way to write a multi-line comment in Python?",
        "choices": ["// This is a comment", "<!-- This is a comment -->", "''' This is a multi-line comment '''", "# This is a multi-line comment"],
        "answer": "''' This is a multi-line comment '''"
    },

    {
        "topic": "Python Variables",
        "question": "Which of the following is the correct way to create a variable that stores the number 10?",
        "choices": ["int x = 10", "var x = 10", "x = 10", "x := 10"],
        "answer": "x = 10"
    },
    {
        "topic": "Python Variables",
        "question": "Which of the following variable names is invalid in Python?",
        "choices": ["first_name", "_count", "2ndValue", "total_sum"],
        "answer": "2ndValue"
    },

    {
        "topic": "Python Data Types",
        "question": "Which of the following is not a built-in data type in Python?",
        "choices": ["int", "list", "real", "str"],
        "answer": "real"
    },
    {
        "topic": "Python Data Types",
        "question": "What will be the output of the following code?\nx = 3.14\nprint(type(x))",
        "choices": ["<class 'float'>", "t<class 'int'>", "<class 'str'>", "<class 'double'>"],
        "answer": "<class 'float'>"
    },

    {
        "topic": "Python Numbers",
        "question": "What is the type of the following value in Python?\nx = 7",
        "choices": ["float", "int", "complex", "double"],
        "answer": "int"
    },
    {
        "topic": "Python Numbers",
        "question": "Which of the following is a valid complex number in Python?",
        "choices": ["5 + 2i", "5 + 2j", "5 + j2", "complex(5i, 2)"],
        "answer": "5 + 2j"
    },
  
    {
        "topic": "Python Casting",
        "question": "What will be the result of the following code?\nx = int(3.9) \nprint(x)",
        "choices": ["3.9", "4", "3", "Error"],
        "answer": "3"
    },
    {
        "topic": "Python Casting",
        "question": "Which of the following strings can be safely cast to an integer using int() in Python?",
        "choices": ["'42'", "'3.14'", "'forty'", "'007.0'"],
        "answer": "'42'"
    },

  
    {
        "topic": "Python Strings",
        "question": "What will the following code print?\ntext = 'Python' \nprint(text[1])",
        "choices": ["p", "y", "t", "o"],
        "answer": "y"
    },
    {
        "topic": "Python Strings",
        "question": "What does the upper() method do in Python?",
        "choices": ["Converts the string to lowercase", "Returns the first character", "Converts the string to uppercase", "Reverses the string"],
        "answer": "Converts the string to uppercase"
    },
   
    {
        "topic": "Python Booleans",
        "question": "What is the output of the following code? \nprint(bool(0))",
        "choices": ["True", "False", "0", "None"],
        "answer": "False"
    },
    {
        "topic": "Python Booleans",
        "question": "Which of the following expressions will return True?",
        "choices": ["5 < 2", "10 == '10'", "3 >= 3", "bool('')"],
        "answer": "3 >= 3"
    },
    {
        "topic": "Python Operators",
        "question": "What is the result of the following operation? \n7 % 3",
        "choices": ["2.33", "1", "0", "4"],
        "answer": "1"
    },
    {
        "topic": "Python Operators",
        "question": " What is the result of this expression? \nTrue and False or True",
        "choices": ["True", "False", "None", "Error"],
        "answer": "True"
    },
    {
        "topic": "Python Lists",
        "question": "What does the following code output? \nfruits = ['apple', 'banana', 'cherry'] \nprint(fruits[-1])",
        "choices": ["apple", "banana", "cherry", "IndexError"],
        "answer": "cherry"
    },
    {
        "topic": "Python Lists",
        "question": "Which method is used to add an element to the end of a list in Python?",
        "choices": ["add()", " insert()", "append()", "push()"],
        "answer": "append()"
    },

    {
        "topic": "Python Tuples",
        "question": "What happens if you try to modify an element in a Python tuple? \ny_tuple = (1, 2, 3) \nmy_tuple[0] = 9",
        "choices": ["It changes the first element to 9", "It adds 9 to the tuple", "It throws a TypeError", "It changes the tuple into a list"],
        "answer": "It throws a TypeError"
    },
    {
        "topic": "Python Tuples",
        "question": "Which of the following correctly creates a tuple with one element?",
        "choices": ["my_tuple = (5)", "my_tuple = (5,)", "my_tuple = [5]", "my_tuple = tuple[5]"],
        "answer": "my_tuple = (5,)"
    },

 
    {
        "topic": "Python Sets",
        "question": "Which of the following statements about sets is true?",
        "choices": ["Sets allow duplicate elements", "Sets maintain insertion order", "Sets are mutable and unordered", "Sets are indexed"],
        "answer": "Sets are mutable and unordered"
    },
    {
        "topic": "Python Sets",
        "question": "What will be the result of the following code? \nmy_set = set([1, 2, 2, 3, 3, 3]) \nprint(my_set)",
        "choices": ["[1, 2, 3, 3, 2, 1]", "{1, 2, 3}", "{1, 2, 2, 3, 3, 3}", "set([1, 2, 2, 3, 3, 3])"],
        "answer": "{1, 2, 3}"
    },

  
    {
        "topic": "Python Dictionaries",
        "question": "What will the following code print? \nperson = {'name': 'Alice', 'age': 25} \nprint(person['name'])",
        "choices": ["Alice", "25", "name", "Error"],
        "answer": "Alice"
    },
    {
        "topic": "Python Dictionaries",
        "question": "Which of the following can not be used as a dictionary key in Python?",
        "choices": ["42", "'key'", "[1, 2]", "(1, 2)"],
        "answer": "[1, 2]"
    },
    

    {
        "topic": "Python If...Else",
        "question": "What will be printed by the following code?/nx = 7 /nif x > 10: /nprint('High') /nelse: /nprint('Low')",
        "choices": ["high", "low", "x", "error"],
        "answer": "low"
    },
    {
        "topic": "Python If...Else",
        "question": "What is the output of the following code? /nx = 5 /nif x > 3: /nif x < 10: /nprint('Yes') /nelse: /n/print/'No')",
        "choices": ["Yes", "No", "Error", "Nothing is printed"],
        "answer": "Yes"
    },
    
 
    {
        "topic": "Python Match",
        "question": "What will the following code print? /nvalue = 2 /nmatch value: /ncase 1: /nprint('One') /ncase 2: /nprint('Two') /ncase _: /nprint('Other')",
        "choices": ["One", "Two", "Other", "Error"],
        "answer": "Two"
    },
    {
        "topic": "Python Match",
        "question": " What is printed when the code below runs? /nlanguage = 'Ruby' /nmatch language: /ncase 'Python': /nprint('Snake') /ncase 'Java': /nprint('Coffee') /ncase _: /nprint('Unknown')",
        "choices": ["Snake", "Coffee", "Unknown", "Ruby"],
        "answer": "Unknown"
    },
    
  
    {
        "topic": "Python While Loops",
        "question": "How many times will this loop run? /ncount = 0 /nwhile count < 3: /nprint(count) /ncount += 1",
        "choices": ["2", "3", "4", "Infinite"],
        "answer": "3"
    },
    {
        "topic": "Python While Loops",
        "question": "What is the output of the following code? /nx = 0 /nwhile x < 5: /nif x == 3: /nbreak /nprint(x) /nx += 1",
        "choices": ["0 1 2 3 4", "0 1 2 3", "0 1 2", "Infinite loop"],
        "answer": "0 1 2"
    },
    

    {
        "topic": "Python For Loops",
        "question": "What will be the output of the following code? /nfor i in range(3): /nprint(i)",
        "choices": ["1 2 3", "0 1 2", "0 1 2 3", "1 2"],
        "answer": "0 1 2"
    },
    {
        "topic": "Python For Loops",
        "question": "Which of the following for-loops will correctly print each item in the list fruits = ['apple', 'banana', 'cherry']?",
        "choices": ["for x in range(fruits): print(x)", "for x in fruits: print(x)", "for fruits in x: print(x)", "for x in len(fruits): print(x)"],
        "answer": "for x in fruits: print(x)"
    },
    

    {
        "topic": "Python Functions",
        "question": "What is the correct way to define a function in Python that takes no arguments and prints 'Hello'?",
        "choices": ["import module_name", "from module_name import", "require module_name", "use module_name"],
        "answer": "import module_name"
    },
    {
        "topic": "Python Functions",
        "question": "What will the following function return? /ndef add(a, b): /nreturn a + b /nresult = add(2, 3) /nprint(result)",
        "choices": ["2", "3", "5", "None"],
        "answer": "5"
    },
    {
        "topic": "Python Lambda",
        "question": "What does the following lambda function do? /nsquare = lambda x: x ** 2 /nprint(square(4))",
        "choices": ["8", "16", "4", "Error"],
        "answer": "16"
    },
    {
        "topic": "Python Lambda",
        "question": "Which line correctly sorts the list by the second element in each tuple? /nitems = [(1, 'b'), (3, 'a'), (2, 'c')]",
        "choices": ["items.sort(key=lambda x: x[1])", "items.sort(lambda x: x[1])", "sort.items(key=x[1])", "items = sort(lambda x[1])"],
        "answer": "items.sort(key=lambda x: x[1])"
    },

    {
        "topic": "Python Arrays",
        "question": "What is the correct way to create an array of integers in Python using the array module?",
        "choices": ["arr = array('i', [1, 2, 3])", "arr = [1, 2, 3]", "arr = array[int](1, 2, 3)", "arr = array('int', [1, 2, 3])"],
        "answer": "arr = array('i', [1, 2, 3])"
    },
    {
        "topic": "Python Arrays",
        "question": "What is a key difference between a Python list and a Python array from the array module?",
        "choices": ["Arrays can hold multiple data types, lists cannot", "Lists use less memory than arrays", "Arrays can only hold elements of the same data type", "Lists require import, arrays do not"],
        "answer": "Arrays can only hold elements of the same data type"
    },


    {
        "topic": "Python Classes/Objects",
        "question": "How do you correctly define a class in Python?",
        "choices": ["class MyClass[]:", "def class MyClass:", "class MyClass:", "MyClass = class():"],
        "answer": "class MyClass:"
    },
    {
        "topic": "Python Classes/Objects",
        "question": "What is the correct way to create an object from a class named Car?",
        "choices": ["car = Car()", "Car = car()", "object car = new Car()", "car <- Car()"],
        "answer": "car = Car()"
    },

   
    {
        "topic": "Python Inheritance",
        "question": "What is the output of the following code? /nclass Animal: /ndef speak(self): /nprint('Animal speaks') /nclass Dog(Animal): /npass /nd = Dog() /nd.speak()",
        "choices": ["Error", "Dog speaks", "Animal speaks", "Nothing is printed"],
        "answer": "Animal speaks"
    },
    {
        "topic": "Python Inheritance",
        "question": "What happens if a child class overrides a method from the parent class?",
        "choices": ["The method in the child class is ignored", "Both methods are executed", "The child class method replaces the parent class method", "An error occurs"],
        "answer": "The child class method replaces the parent class method"
    },

   
    {
        "topic": "Python Iterators",
        "question": "What will the following code output? /nmylist = [10, 20, 30] /nit = iter(mylist) /nprint(next(it)) /nprint(next(it))",
        "choices": ["10 20", "20 30", "10 30", "Error"],
        "answer": "10 20"
    },
    {
        "topic": "Python Iterators",
        "question": "What is true about Python iterators?",
        "choices": ["All Python data types are iterators", "An iterator object must implement __iter__() and __next__() methods", "Iterators can only be used with strings", "Iterators can’t be used in loops"],
        "answer": "An iterator object must implement __iter__() and __next__() methods"
    },

    {
        "topic": "Python Polymorphism",
        "question": "What is the main idea of polymorphism in Python?",
        "choices": ["One function or method can behave differently based on object type", "A function can only take integer arguments", "You can write code without using classes", "It allows variables to be declared without data types"],
        "answer": "One function or method can behave differently based on object type"
    },
    {
        "topic": "Python Polymorphism",
        "question": "What will this code output? /nclass Animal: /ndef sound(self): /nprint('Some sound') /nclass Cat(Animal): /ndef sound(self): /nprint('Meow') /nc = Cat() /nc.sound()",
        "choices": ["Some sound", "Meow", "Cat", "Error"],
        "answer": "Meow"
    },

 
    {
        "topic": "Python Scope",
        "question": "What will be printed by the following code? /ndef my_func(): /nx = 5 /nprint(x) /nmy_func()",
        "choices": ["5", "x", "Error", "Nothing"],
        "answer": "5"
    },
    {
        "topic": "Python Scope",
        "question": "What is the output of the code below? /nx = 10 /ndef my_func(): /nx = 20 /nprint(x) /nmy_func() /nprint(x)",
        "choices": ["20 10", "10 20", "20 20", "10 10"],
        "answer": "20 10"
    },

    {
        "topic": "Python Modules",
        "question": "What is the correct way to import a built-in Python module named math?",
        "choices": ["include math", "import math", "use math", "math.import()"],
        "answer": "import math"
    },
    {
        "topic": "Python Modules",
        "question": "What does the following code print? /nimport math /nprint(math.sqrt(16))",
        "choices": ["8", "4", "256", "Error"],
        "answer": "4"
    },

  
    {
        "topic": "Python Dates",
        "question": "What is the correct way to get the current date using the datetime module?",
        "choices": ["datetime.now()", "date.today()", "datetime.datetime.now()", "time.now()"],
        "answer": "datetime.datetime.now()"
    },
    {
        "topic": "Python Dates",
        "question": "Which of the following is a correct way to import only the date class from the datetime module?",
        "choices": ["import date from datetime", "datetime import date", "from datetime import date", "include date from datetime"],
        "answer": "from datetime import date"
    },


    {
        "topic": "Python Math",
        "question": "What is the result of round(3.75) in Python?",
        "choices": ["3", "4", "3.7", "3.8"],
        "answer": "4"
    },
    {
        "topic": "Python Math",
        "question": "What will pow(2, 3) return?",
        "choices": ["6", "8", "9", "5"],
        "answer": "8"
    },

 
    {
        "topic": "Python JSON",
        "question": "What does the following code do? /nimport json /nx = '{'name': 'Alice', 'age': 25}' /ny = json.loads(x) /nprint(y['name'])",
        "choices": ["Prints '{'name': 'Alice', 'age': 25}'", "Prints 'y'", "Prints 'Alice'", "Returns an error"],
        "answer": "Prints 'Alice'"
    },
    {
        "topic": "Python JSON",
        "question": "What does json.dumps() do in Python?",
        "choices": ["Converts JSON to a Python object", "Converts a Python object to a JSON string", "Deletes a JSON file", "Parses an XML file"],
        "answer": "Converts a Python object to a JSON string"
    },
  
    {
        "topic": "Python RegEx",
        "question": "What will this code return? /nimport re /ntxt = 'The rain in Spain' /nx = re.search('ai', txt) /nprint(x.group())",
        "choices": ["ai", "Rain", "Spain", "Error"],
        "answer": "ai"
    },
    {
        "topic": "Python RegEx",
        "question": "What does re.findall() return in Python?",
        "choices": ["A single match as a string", "All matches as a list", "The number of matches", "Boolean True/False"],
        "answer": "All matches as a list"
    },
  
    {
        "topic": "Python PIP",
        "question": "Which command is used to install a Python package using pip?",
        "choices": ["python install requests", "pip install requests", "pip get requests", "install pip requests"],
        "answer": "pip install requests"
    },
    {
        "topic": "Python PIP",
        "question": "What does the command pip list do?",
        "choices": ["Lists all pip commands", "Lists all files in your project", "Lists all installed Python packages", "Uninstalls pip"],
        "answer": "Lists all installed Python packages"
    },
    
 
    {
        "topic": "Python Try...Except",
        "question": "What will this code output? /ntry: /nx = 1 / 0 /nexcept ZeroDivisionError: /nprint('Cannot divide by zero!')",
        "choices": ["0", "Error", "Cannot divide by zero!", "None"],
        "answer": "Cannot divide by zero!"
    },
    {
        "topic": "Python Try...Except",
        "question": "What happens if no error occurs in a try block?",
        "choices": ["The except block is still executed", "The program crashes", "The code runs normally, and except is skipped", "An error is raised anyway"],
        "answer": "The code runs normally, and except is skipped"
    },
    
 
    {
        "topic": "Python String Formatting",
        "question": "What is the correct way to use an f-string in Python?",
        "choices": ["print(f'Hello', name)", "print('Hello {name}')", "print(f'Hello {name}')", "print('f'Hello {name}'')"],
        "answer": "print(f'Hello {name}')"
    },
    {
        "topic": "Python String Formatting",
        "question": "What does the following code print? /nname = 'Alice' /nprint('Hello, {}!'.format(name))",
        "choices": ["Hello, {name}!", "Hello, Alice!", "Hello, !", "Error"],
        "answer": "Hello, Alice!"
    },
 
    {
        "topic": "Python User Input",
        "question": "What is the correct way to get user input in Python?",
        "choices": ["input('Enter your name: ')", "get('Enter your name: ')", "scan('Enter your name: ')", "read('Enter your name: ')"],
        "answer": "input('Enter your name: ')"
    },
    {
        "topic": "Python User Input",
        "question": "What is the output of this code if the user enters 5? /nx = input('Enter a number: ') /nprint(x * 2)",
        "choices": ["10", "55", "Error", "5 5"],
        "answer": "55"
    },

    {
        "topic": "Python VirtualEnv",
        "question": "Why would you use a Python virtual environment?",
        "choices": ["To run Python scripts faster", "To isolate project dependencies and avoid conflicts between packages", "To use multiple CPUs", "To avoid using Python entirely"],
        "answer": "To isolate project dependencies and avoid conflicts between packages"
    },
    {
        "topic": "Python VirtualEnv",
        "question": "Which command correctly creates a virtual environment named env in your current directory?",
        "choices": ["virtualenv env", "create venv env", "python -run env", "venv.create(env)"],
        "answer": "virtualenv env"
    }    

]