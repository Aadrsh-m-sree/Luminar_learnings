def display_mobile_data(**kwargs): #NOTE -  **kwargs used to takes any numbers of arguments as a dictionary
    print(kwargs.get("name"))
    print(kwargs.get("price"))

display_mobile_data(name="OnePlus",price=32000,display="Amoled")
