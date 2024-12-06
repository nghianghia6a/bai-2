print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Tạo danh sách để lưu trữ các số thỏa mãn điều kiện
result = []

# Lặp qua các số trong khoảng từ 2000 đến 3200 (bao gồm cả 2000 và 3200)
for i in range(2000, 3201):
    # Kiểm tra nếu số đó chia hết cho 7 nhưng không phải bội số của 5
    if (i % 7 == 0) and (i % 5 != 0):
        # Thêm số đó vào danh sách dưới dạng chuỗi
        result.append(str(i))

# In danh sách các số dưới dạng chuỗi, cách nhau bởi dấu phẩy
print(','.join(result))
