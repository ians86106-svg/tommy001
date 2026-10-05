# CREATE
arr_1d = [10, 20, 30, 40]
print("original:", arr_1d)

# ADD(Append to the end of the list)
print("append 50:", arr_1d.append(50))
print("after append:", arr_1d)

# EDIT(Change the Index 1 to 25)
arr_1d[1] = 25
print("after edit:", arr_1d)

#DELETE(Remove the value 30 from the list)
arr_1d.remove(30)
print("after delete:", arr_1d)

# CREATE (2rows, 3columns)
arr_2d = [[1, 2, 3], [4, 5, 6]]
print("2D array:", arr_2d)

#ADD (Append a new row to the 2D array)
arr_2d.append([7, 8, 9])
print("after append row:", arr_2d)

#EDIT (Change the value at row 1, column 2 to 10)
arr_2d[1][2] = 10
print("after edit:", arr_2d)

#DELETE (Remove the value at row 0, column 1)
arr__2d[0].pop(1) #Remove the value at row 0, column 1
arr_2d[0][1] = 99
print("after delete:", arr_2d)
print("After edit:\n", arr_2d)

# CREATE (3rows, 2columns)
arr_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
print("3D array:", arr_3d)

#ADD (Append a new 2D array to the 3D array)
arr_3d.append([[13, 14], [15, 16]])
print("after append 2D array:", arr_3d)

#EDIT (Change the value at row 1, column 0, depth 1 to 20)
arr_3d[1][0][1] = 20
print("after edit:", arr_3d)
arr_3d[0][1][0] = 99
#DELETE (Remove the value at row 0, column 1, depth 0) arr_3d[0] [1][0]
print ("after delete:", arr_3d)