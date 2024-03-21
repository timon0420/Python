# def dekor(func):
#     def wew(*args):
#         print('to jest dekorator 1')
#         func(*args)
#         print('to jest dekorator 2')
#     return wew

# @dekor
# def funkcja(*args):
#     print(args)
#     print(sum(args))
# funkcja(1,2,3,4,5,6)

def dekor(func):
    def wew(*args):
        if len([x for x in args if type(x) == int]) == len(args):
            func(*args)
            if len([x for x in args if x >= 97 and x <= 122]) == len(args):
                print(' '.join(list(map(chr,args))))
            print(f'Nazwa funkcji to: {func.__name__}')
        else:
            print('Nie prawidłowe argumenty')
            print(f'Nazwa funkcji to: {func.__name__}')
    return wew

@dekor
def funkcja(*args):
    print(args)
    print(sum(args))
funkcja(97,1)