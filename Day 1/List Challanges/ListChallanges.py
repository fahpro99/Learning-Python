# row1 = ["😀", "😍", "😁"]
# row2 = ["🤑", "😅", "😌"]
# row3 = ["😎", "😩", "🥱"]
#
# map = [row1, row2, row3]
# x = int(input("Select row :\n")) - 1
# y = int(input("Select column: \n")) - 1
#
# map[x][y] = "x"
#
# print(f"{row1}\n{row2}\n{row3}")

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = [[9, 8, 7], [6, 5, 4], [1, 2, 3]]
# c = []
# for i in range(len(A)):
#     s = []
#     for j in range(len(A[0])):
#         s.append(A[i][j] + B[i][j])
#     c.append(s)
#
# print(c)

work_hours = [int(x) for x in input("Enter hours per day in entire week, Separated by comma").split(",")]
wages = int(input("Enter Hourly Wage"))

total = sum(work_hours)

salary = total * wages
print("Salary is ", salary)
