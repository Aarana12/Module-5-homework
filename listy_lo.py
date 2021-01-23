if __name__ == "__main__":
    food = ['rice', 'beans']
    
    food.append('broccoli')
     
    more_food = 'bread', 'pizza'
    food.append(more_food)


    print(food)

    food = ['rice', 'beans', 'broccoli', 'bread', 'pizza']
    slicing = food[0:2]
    print(slicing)
    print(food[4])

    breakfast = "eggs,fruit,orange juice"
    my_breakfast = breakfast.split(',')
    print(my_breakfast)

    print(len(my_breakfast))

    new_list = []
    values = input("Please input values: \n")
    while not (values == "stop"):
        new_list.append(float(values))
    
    print('\n')
    print("Max:", max(new_list))
    print("Min:", min(new_list))
    print("Average", sum(new_list)/len(new_list))
