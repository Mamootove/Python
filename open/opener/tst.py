import pickle

data = {"Username":"Password"
        }

with open("users.txt", "wb") as file:
    pickle.dump(data, file)
