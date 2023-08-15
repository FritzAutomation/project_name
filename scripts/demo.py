"""
demo.py
-------

Demonstrates the functionality of module1 from our project.
"""

from project_name import module1

def run_demo():
    # Create an instance of MyClass from module1
    obj = module1.MyClass("DemoValue1", "DemoValue2")
    
    # Call some methods or functions from module1
    result = module1.my_function("value1", "value2")
    
    print(f"Result of my_function: {result}")

if __name__ == "__main__":
    run_demo()
