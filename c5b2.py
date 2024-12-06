print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập vào số tự nhiên n > 0
n = int(input("Nhập vào một số tự nhiên n > 0: "))

# Kiểm tra điều kiện n > 0
if n > 0:
    while n >= 0:
        print(n)  # In số hiện tại
        n -= 1  # Giảm n đi 1
else:
    print("Vui lòng nhập số tự nhiên lớn hơn 0!")
