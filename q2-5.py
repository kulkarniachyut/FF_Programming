'''
QUESTION : 2
'''

def convert(s) :
    try :
        if int(s) == float(s) :
            return int(s)
    except :
        try :
            float(s)
            return float(s)
        except :
            return str(s)

'''
QUESTION : 3
'''

def change(abc) :
    animal_obj = {'animal' : abc[0], 'name' : abc[1], 'age' : abc[2]}
    print ("{0:s} the {1:s} is {2:03d} years old").format(animal_obj['name'],animal_obj['animal'],animal_obj['age'])
    return animal_obj

'''
QUESTION : 4
'''

def minimum(a,b,c) :
    value = a if a < b else b
    return (c if c < value else value)



'''
QUESTION : 5
'''

def apply_operation(left_operand, operator, right_operand) :
    s= str(left_operand)+operator+str(right_operand)
    return eval(s)



def main() :
    print
    print ' ------  QUESTION 2 -----'
    print 100 , type(convert("100"))
    print 100.23 , type(convert("100.23"))
    print "100.123s", type(convert("100.123s"))
    print "achyut" , type(convert("achyut"))
    print ' ------  ------  ------  ------  -----'
    print
    print ' ------  QUESTION 3 -----'
    abc = ['dog','fido',100]
    change(abc)
    print ' ------  ------  ------  ------  -----'
    print
    print ' ------  QUESTION 4 -----'
    print "minimum of (100,1.3,123123) "
    print minimum(100,1.3,123123)
    print ' ------  ------  ------  ------  -----'
    print
    print ' ------  QUESTION 5 -----'
    print apply_operation (5.0,'/',7)
    print apply_operation (5.0,'+',7)
    print apply_operation (5.0,'*',7)
    print apply_operation (5.0,'-',7)
    print ' ------  ------  ------  ------  -----'
    print

if __name__ == '__main__':
    main()
