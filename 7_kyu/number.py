
def number(bus_stops):
    entered = 0
    for i in bus_stops:
        entered = entered + i[0] - i[1]
    return entered


        
print(number([[10,0],[3,5],[5,8]]))
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
