from dogDao import dogDao

dog = {
    'ID': 1234,
    'Breed': 'Pug',
    'Ownedby': 'Marian Dineen',
    'Price': 230
}

dog2 = {
    'ID': 1234,
    'Breed': 'Collie',
    'Ownedby': 'Eva McGrath',
    'Price': 300
}

#returnValue = dogDao.create(dog)
returnValue = dogDao.getAll()
print(returnValue)

returnValue = dogDao.findbyID(dog2['ID'])
print(returnValue)

returnValue = dogDao.update(dog2)
print(returnValue)

returnValue = dogDao.findbyID(dog2['ID'])
print(returnValue)

returnValue = dogDao.delete(dog2['ID'])
print(returnValue)

returnValue = dogDao.getAll()
print(returnValue)

