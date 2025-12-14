import pickle

data = {"Username":"Password", 
        "Mahan":9090,
        "MMDreza":"MMD*rez90KHAFAN",
        "Paria":8462
        }


with open("user.txt", "wb") as file:
    pickle.dump(data, file)
    
    

    



