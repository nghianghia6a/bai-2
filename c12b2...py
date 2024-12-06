import re

def validate_passwords():
    valid_passwords = []
    
    # Nhập mật khẩu từ giao diện điều khiển, cách nhau bởi dấu phẩy
    passwords = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ").split(',')
    
    for password in passwords:
        # Kiểm tra độ dài mật khẩu
        if len(password) < 6 or len(password) > 12:
            continue
        
        # Kiểm tra có ít nhất một chữ cái thường [a-z]
        if not re.search("[a-z]", password):
            continue
        
        # Kiểm tra có ít nhất một chữ số [0-9]
        if not re.search("[0-9]", password):
            continue
        
        # Kiểm tra có ít nhất một chữ cái in hoa [A-Z]
        if not re.search("[A-Z]", password):
            continue
        
        # Kiểm tra có ít nhất một ký tự đặc biệt [$ # @]
        if not re.search("[$#@]", password):
            continue
        
        # Kiểm tra không chứa khoảng trắng
        if re.search("\s", password):
            continue
        
        # Nếu vượt qua tất cả các kiểm tra, thêm vào danh sách hợp lệ
        valid_passwords.append(password)
    
    # In danh sách các mật khẩu hợp lệ, cách nhau bởi dấu phẩy
    print(",".join(valid_passwords))

# Gọi hàm
validate_passwords()
