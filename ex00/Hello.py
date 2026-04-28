ft_list = ["Hello", "tata!"]   #lists can be sorted/changed
ft_tuple = ("Hello", "toto!")  #tuple cannot be changed
ft_set = {"Hello", "tutu!"}    #set cannot have dups and order doesn't matter
ft_dict = {"Hello" : "titi!"}  #like map in c#

#your code here

ft_list[1] = "World"
ft_tuple = (ft_tuple[0], "Portugal")

ft_set.remove("tutu!")
ft_set.add("Porto!")

ft_dict["Hello"] = "42Porto"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)