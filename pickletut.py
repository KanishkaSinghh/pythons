import pickle
cars=["nano","bugatii","porche","bmw"]
file="mycars.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
#how to depickle
file="mycars.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)