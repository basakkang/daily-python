import sys

# We can use raise to throw an exception if a condition occurs
def intend_exception(x):
    if x < 8:
        print('come')
    else:
        raise Exception('Under 8 only')

def linux_method():
    print(sys.platform)
    assert ('linux' in sys.platform), "Linux only"
        
if __name__ == "__main__":
    
    try:
        intend_exception(7)
        # the code in the try clause will stop as soon as an exception is encountered.
    except Exception as error:
        print(f'Err: {error}')
    else:
        try:
            linux_method()    
        except AssertionError as error:
            print(error)
            print('linux_method not executed')
    finally:
        print('Cleaning up.')
    


    
