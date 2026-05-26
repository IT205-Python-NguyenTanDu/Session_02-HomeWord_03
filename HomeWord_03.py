# 1. PHÂN TÍCH INPUT / OUTPUT

# Input:
# - Họ và tên bệnh nhân (String)
# - Tuổi bệnh nhân (Integer)

# Output:
# - Phiếu khám bệnh điện tử gồm:
#   + Tên
#   + Tuổi
#   + Kết quả phân luồng
# - Nếu dữ liệu sai -> thông báo lỗi


# 2. ĐỀ XUẤT GIẢI PHÁP

# Sử dụng:
# - if - elif - else
# - Toán tử logic or
# - strip() để kiểm tra tên rỗng

# Quy tắc:
# - Tuổi < 6 -> Ưu tiên bệnh nhi
# - Tuổi >= 80 -> Ưu tiên người cao tuổi
# - Còn lại -> Khám thường

# Kiểm tra lỗi:
# - Tên rỗng hoặc chỉ chứa khoảng trắng
# - Tuổi âm hoặc > 150


# 3. THUẬT TOÁN (PSEUDOCODE)

# B1: Nhập tên và tuổi bệnh nhân
# B2: Kiểm tra dữ liệu hợp lệ
#     - Nếu sai -> báo lỗi và kết thúc
# B3: Phân luồng theo độ tuổi
# B4: In phiếu khám bệnh điện tử

# ==============================
# HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN
# ==============================

# Nhập thông tin bệnh nhân
patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))

# KIỂM TRA DỮ LIỆU KHÔNG HỢP LỆ
if patient_name.strip() == "" or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else:

    # PHÂN LUỒNG BỆNH NHÂN
    if patient_age < 6:
        classification = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."

    elif patient_age >= 80:
        classification = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."

    else:
        classification = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    # IN PHIẾU KHÁM BỆNH
    print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
    print(f"Họ và tên: {patient_name}")
    print(f"Tuổi: {patient_age}")
    print(f"Kết quả phân luồng: {classification}")