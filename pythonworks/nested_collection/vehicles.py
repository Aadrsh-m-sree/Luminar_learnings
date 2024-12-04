cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt","dct"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt","torque"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

# count of vehicles 
print(f"total vehicles = {len(cars)}")

# print available colours of baleno

baleno_colour = [car.get('colors') for car in cars if car.get('name') == 'baleno'][0]
print(baleno_colour)
# print all brands

brands_name = {car.get('brand') for car in cars}
print(brands_name)

# all cars in available in amt

amt_transm = [car.get('name') for car in cars if 'amt' in car.get('transmissions')]
print(set(amt_transm))

# avalable in blue color

blue_cars = [car.get('name')for car in cars if 'blue' in car.get('colors')]
print(set(blue_cars))

# all transmission types

# all_transmissions = [trans for car in cars for trans in car.get('transmissions')]
# print(set(all_transmissions))

all_colours = [color for car in cars for color in car.get('colors')]
print(set(all_colours))

color_count = {color:all_colours.count(color) for car in cars for color in car.get('colors')}
print(color_count)

popular = max(color_count,key=lambda count:color_count.get(count))
print(f"most popular colour is {popular}")

# costly car

# cost_of_cars = {car.get('name'):car.get('price')for car in cars}
# print(cost_of_cars)

# costly_car = max(cost_of_cars,key=lambda costly:cost_of_cars.get(costly))
costly_car = max(cars,key=lambda d:d.get('price'))
print(f"car with maximum cost is {costly_car}")

# car with minimum
cost_of_cars = {car.get('name'):car.get('price')for car in cars}
print(cost_of_cars)

costly_car = min(cost_of_cars,key=lambda costly:cost_of_cars.get(costly))
min_cost_car = min(cars,key=lambda d:d.get('price'))
print(f"car with minimum cost is {min_cost_car}")

# # sort cars with price

all_cars = [car.get('name') for car in cars]
all_prices = [car.get('price') for car in cars]
after_sorting = {car:price for car,price in sorted(zip(all_cars,all_prices),reverse=True)} 
print(after_sorting)

sorted_cars=sorted(cars,key=lambda c:c.get("price"),reverse=True)
sorted_car={car.get("name"):car.get("price") for car in sorted_cars}
print(sorted_car)



