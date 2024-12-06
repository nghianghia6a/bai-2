print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Yêu cầu người dùng nhập số nguyên n
n = int(input("Nhập vào một số: "))

# Tạo dictionary rỗng
d = dict()

# Duyệt qua các số từ 1 đến n
for i in range(1, n + 1):
    d[i] = i * i  # Gán giá trị i*i cho key i

# In ra dictionary
print(d)
