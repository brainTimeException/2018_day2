import numpy as np
from maxima import find_maxima

def test1():
    x = [0, 1, 2, 1, 2, 1, 0]
    expected = [2, 4]
    res = find_maxima( x )

    if res != expected:
        printErrorMessage( "test1", "", expected, res )
        return

    


    x = [-i**2 for i in range(-3, 4)]
    expected = [ 3 ]
    res = find_maxima( x )

    if res != expected:
        printErrorMessage( "test1", "", expected, res )
        return

    
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]

    expected = [16, 78]
    res = find_maxima( x )

    if res != expected:
        printErrorMessage( "test1", "", expected, res )
        return

    print( "test1 PASSED" )



def printErrorMessage( test, message, expected, actual ):
    print( 'test "' + test + '" FAILED!' )
    if message != "":
        print( message )
    print( "the expected result is:" )
    print( expected )
    print( "the actual result was:" )
    print( actual )


test1()
