def main():
    num = 1
    add = 0
    def func(num, add):
        if add> 100000000:
            return True
        else:   
            print(add)    
            func(add + num, num )

    func(num,add)
main()