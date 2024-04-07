from machine_say import hello_from_module2

def test_hello_from_module2():
    assert hello_from_module2() == "Hello from Module 2!"

if __name__ == "__main__":
    test_hello_from_module2()

