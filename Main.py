from QuanLySinhVien import QuanLySinhVien

# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlsv = QuanLySinhVien()
while (True):
    print(" ")
    print(" ..............Nhập yêu cầu..............")
    print("|    0. Thoát chương trình               |")
    print("|    1. Nhập thông tin sinh viên         |")
    print("|    2. Cập nhật thông tin sinh viên     |")
    print("|    3. Xóa sinh viên                    |")
    print("|    4. Tìm kiếm sinh viên               |")
    print("|    5. Hiển thị danh sách sinh viên     |")
    print(" ''''''''''''''''''''''''''''''''''''''''")

    chon = int(input(" Mời bạn chọn: "))
    if (chon == 0):
        break
    if (chon == 1):
        print("\n 1. Nhập thông tin sinh viên.")
        qlsv.nhapSinhVien()
        print("\n Thêm sinh viên thành công!")
    elif (chon == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n 2. Cập nhật thông tin sinh viên. ")
            print("\n Nhập mã của sinh viên cần sửa: ")
            id = input()
            qlsv.updateSinhVien(id)
        else:
            print("\n Danh sách rỗng!")
    elif (chon == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n 3. Xóa sinh viên.")
            print("\n Nhập mã sinh viên cần xóa: ")
            id = input()
            if (qlsv.deleteById(id)):
                print("\n Sinh viên có mã: ", id, " đã bị xóa.")
            else:
                print("\n Không có sinh viên nào có mã:", id)
        else:
            print("\n Danh sách rỗng!")
    elif (chon == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n 4. Tìm kiếm sinh viên.")
            print("\n Nhập tên sinh viên cần tìm: : ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\n Danh sách rỗng!")

    elif (chon == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n 5. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
            soluong = qlsv.soLuongSinhVien()
            print(" Hiện có {} sinh viên trong danh sách".format(soluong))
        else:
            print("\n Danh sách rỗng!")
    else:
        print("\n Hãy chọn đúng chức năng trong menu.")