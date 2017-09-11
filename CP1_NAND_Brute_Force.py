#NAND BruteForce
#Author: Jake Smith (jts5np)
#Date: 9-5-2017
#Last Date: 9-10-2017
#Class: Discrete Math

def nand(exp):
    code1 = 'a = 1; b = 1; ' + exp
    code1 = code1.replace('print','f1 =')
    code2 = 'a = 1; b = 0; ' + exp
    code2 = code2.replace('print','t1 =')
    code3 = 'a = 0; b = 1; ' + exp
    code3 = code3.replace('print','t2 =')
    code4 = 'a = 0; b = 0; ' + exp
    code4 = code4.replace('print','f2 =')
    exec(code1)
    exec(code2)
    exec(code3)
    exec(code4)
    if (t1 and t2) and not (f1 or f2):
        exp = exp.replace('not (','NAND(')
        exp = exp.replace(' and ',', ')
        exp = exp.replace('print','')
        print 'NANDs used: ' + str(exp.count('NAND')) + ' Expression: ' + exp

def brute_force(string):
    if string.count('{}') == 0:
        nand(string)
        return
    else:
        s1 = string.replace('{}','a',1)
        s2 = string.replace('{}','b',1)
        s3 = string.replace('{}','1',1)
        brute_force(s1)
        brute_force(s2)
        brute_force(s3)
        if string.count('not') < 5:
            s4 = string.replace('{}','not ({} and {})',1)
            brute_force(s4)

init = 'print not ({} and {})'

brute_force(init)
