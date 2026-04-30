def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object is None:
        print(f"Nothing : None {obj_type}")
    elif obj_type == float and object != object:
        print(f"Cheese : nan {obj_type}")
    elif obj_type == int and object == 0:
        print(f"Zero : 0 {obj_type}")
    elif obj_type == str and object == "":
        print(f"Empty : {obj_type}")
    elif obj_type == bool and object == False:
        print(f"Fake : False {obj_type}")
    else:
        print("Type not found")
    return 1