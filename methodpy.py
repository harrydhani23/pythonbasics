def mean(obj):
    #if type(obj) == dict:
    if isinstance(obj, dict):
        the_mean = sum(obj.values())/len(obj)
    else:
        the_mean = sum(obj)/len(obj)
    return the_mean

print(mean([1,2,3,4,5,6,7,8]))
print(mean({"Morning":3.4, "Noon":4.5, "Evening":5.5}))

#===============take input from user==========================
def weather_condition(temp):
    if temp > 25:
        return "It's hot outside"
    elif temp > 10:
        return "weather is amazing"
    else:
        return "it's cold outside"

#user_input = float(input("please eneter the temp:"))
#print(weather_condition(user_input))



#=============format a string with varibles===============================
def greetGuest(user_input):
    #return "hi "+user_input+"!"
    #return "Heloo %s, how are you !" % user_input
    return f"Heloo {user_input}, how are you !" #this will only work in python three {variable name}

user_input = input("please eneter your name:")
print(greetGuest(user_input))

#=============positional-arguments and keyword-arguments==================
def concat(a,b="dhani"):
    return a+b

print(concat("harry","dhani")) # positional-arguments
print(concat(b="dhani",a="harry")) #keyword-arguments
print(concat(a="harry")) # argument could have a fixed contant value, juts in case if we dont pass
print(concat("harry")) # argument could have a fixed contant value, juts in case if we dont pass

#============= n number of arguments======================================
def average(*args):
        for arg in args:
            arg = arg+arg
        return arg/len(args)
            
print(average(1,2,3,4,5,6,7,8,9))

# sort the given arguments
def average(*args):
        return sorted(args)           
print(average(1,2,3,4,5,6,7,8,9,12,3,5,6,5,5,6,7,77,6,87,6,7,6))

# n number of keyword arguments
def kargs(**kwargs):
        return kwargs           
print(kargs(f=4.1,b=2,c=3,d=4,e=4.2)) # this will return a dictonary
# sort using values
def kargs(**kwargs):
        return sorted(kwargs, key = kwargs.get)           
print(kargs(f=4.1,b=2,c=3,d=4,e=4.2))



