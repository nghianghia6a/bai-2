print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import math

# Nhập tọa độ điểm thứ nhất
x1 = int(input("Enter x1 ---> "))
y1 = int(input("Enter y1 ---> "))

# Nhập tọa độ điểm thứ hai
x2 = int(input("Enter x2 ---> "))
y2 = int(input("Enter y2 ---> "))

# Tính các bình phương khoảng cách trên từng trục
d1 = (x2 - x1) ** 2
d2 = (y2 - y1) ** 2

# Tính khoảng cách giữa hai điểm
res = math.sqrt(d1 + d2)

# In kết quả
print("Distance between two points:", res)
