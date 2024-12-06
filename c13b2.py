print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import math

def solve_quadratic():
    print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
    
    # Nhập hệ số a, b, c
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
    except ValueError:
        print("Vui lòng nhập các số hợp lệ!")
        return

    # Kiểm tra nếu a = 0 (không phải phương trình bậc 2)
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình trở thành bậc 1, nghiệm là: x = {x}")
        return

    # Tính delta
    delta = b**2 - 4*a*c

    # Xét các trường hợp của delta
    if delta < 0:
        print("Phương trình vô nghiệm (Delta < 0).")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

# Gọi hàm để giải phương trình
solve_quadratic()
