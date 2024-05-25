"""'Destination city.
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] Output: "Sao Paulo" Explanation: Starting at "London" city you will reach "Sao Paulo" city which is t the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".'"""



# def Solution(paths : list[list[str]]) -> str : 
#     out = set()
#     ins = set()
    
#     for a, b in paths:
#         #print(a)
#         #print(b)
#         out.add(a)
#         ins.add(b)
#     return [b for b in ins if b not in out][0]
    


# import test


# paths = [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]
# print(Solution(paths))
    

# Test if we have 3 value in the same List , exp : 
# paths = [["London", "New York", "Lima"], ["Lima", "Paris", "Alger"]]

def Solution(paths : list[list[str]]) -> str : 
    out = set()
    ins = set()
    
    for path in paths:
        a, b, c = path
        # print(a)
        # print(b)
        # print(c)
        out.add(a)
        ins.add(c)
    
    return [c for c in ins if c not in out][0]


import test


paths = [["London", "New York", "Lima"], ["Lima", "Paris", "Alger"]]
print(Solution(paths))