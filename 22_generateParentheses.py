def get(n):
    string = 2*n*[" "]
    for i in xrange(n):
        for j in xrange(i, 2*i+1, 1):
            string[j] = 'c'
            print j, string
    print string

get(2)
