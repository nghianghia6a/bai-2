print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import re

# Hàm kiểm tra mật khẩu
def kiem_tra_mat_khau(mat_khau):
    # Kiểm tra độ dài
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        return False
    # Kiểm tra ít nhất 1 chữ cái [a-z]
    if not re.search("[a-z]", mat_khau):
        return False
    # Kiểm tra ít nhất 1 số [0-9]
    if not re.search("[0-9]", mat_khau):
        return False
    # Kiểm tra ít nhất 1 chữ cái [A-Z]
    if not re.search("[A-Z]", mat_khau):
        return False
    # Kiểm tra ít nhất 1 ký tự [$#@]
    if not re.search("[$#@]", mat_khau):
        return False
    # Kiểm tra khoảng trắng
    if re.search("\s", mat_khau):
        return False
    return True

# Nhập mật khẩu từ người dùng
mat_khau_nguoi_dung = input("Nhập mật khẩu: ")

# Tách các mật khẩu ra
danh_sach_mat_khau = mat_khau_nguoi_dung.split(',')

# Danh sách mật khẩu hợp lệ
mat_khau_hop_le = []

for mk in danh_sach_mat_khau:
    if kiem_tra_mat_khau(mk):
        mat_khau_hop_le.append(mk)

# In ra các mật khẩu hợp lệ
print(",".join(mat_khau_hop_le))
