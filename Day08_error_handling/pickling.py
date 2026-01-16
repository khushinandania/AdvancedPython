import pickle


#store data in file
data = {'name' : 'Khushi' ,
        'age' : 21 , 
        'city' : 'Ahmedabad' , 
        'skills' : ['Python' , 'C++' , 'Java']}


with open('data.pkl' , 'wb') as f:
    pickle.dump(data , f)
    print("data has been stored in pickle file")


with open('data.pkl' , 'rb') as f:
    loaded_data = pickle.load(f)
    print("data has been loaded from pickle file")
    print(loaded_data)
print()



#stores data in bytes
marks = [85, 90, 78, 92, 88]

bytes_data = pickle.dumps(marks)
print("Marks have been stored to bytes")
print(bytes_data)

loaded_data = pickle.loads(bytes_data)
print("Marks have been loaded from bytes")
print(loaded_data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          