from SinhVien import SinhVien
 
class QuanLySinhVien:
    listSinhVien = []
 
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
 
 # Hàm tạo sinh viên mới
    def nhapSinhVien(self):
        svid = input(" Nhập mã sinh viên: ")
        sv:SinhVien = self.findByID(svid)
        while (True):
            sv:SinhVien = self.findByID(svid)
            if sv != None:
                svid = input(" ID này đã tồn tại, vui lòng nhập lại: ")
            else:
                break
        name = input(" Nhập tên sinh viên: ")
        sex = input(" Nhập giới tính: ")
        while (sex != "Nam" and sex != "Nữ"):
            print(" Giới tính không hợp lệ vui lòng nhập lại")
            sex = input(" Nhập giới tính: ")
        else:
            age = int(input(" Nhập tuổi: "))
            while ( age <= 0 ):
                print(" Tuổi không hợp lệ, vui lòng nhập lại")
                age = int(input(" Nhập tuổi: "))
                    
            else:
                nganh = input(" Nhập nghành học: ")
                diemTB = float(input(" Nhập điểm tổng kết: "))
                while ( diemTB <= 0 ):
                    print(" Điểm tổng kết không hợp lệ, vui lòng nhập lại!")
                    diemTB = float(input(" Nhập điểm tổng kết: "))
                
                sv = SinhVien(svid, name, sex, age, nganh, diemTB)
                self.xepLoaiHocLuc(sv)
                self.listSinhVien.append(sv)

# Hàm sửa thông tin sinh viên
    def updateSinhVien(self, id):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv:SinhVien = self.findByID(id)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (sv != None):
            # nhập thông tin sinh viên
            name = input(" Nhập tên sinh viên: ")
            sex = input(" Nhập giới tính: ")
            while (sex != "Nam" and sex != "Nữ"):
                print(" Giới tính không hợp lệ vui lòng nhập lại")
                sex = input(" Nhập giới tính: ")
                age = int(input(" Nhập tuổi: "))
                nganh = input(" Nhập ngành học: ")
                diemTB = float(input(" Nhập điểm tổng kết: "))
            else:
                age = int(input(" Nhập tuổi: "))
                while (age <= 0):
                    print(" Tuổi không hợp lệ, vui lòng nhập lại")
                    age = input(" Nhập giới tính: ")
                else:
                    nganh = input(" Nhập nghành học: ")
                    diemTB = float(input(" Nhập điểm tổng kết: "))
                    while ( diemTB <= 0 ):
                        print(" Điểm tổng kết không hợp lệ, vui lòng nhập lại:")
                        diemTB = float(input(" Nhập điểm tổng kết: "))
            # cập nhật thông tin sinh viên
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._nganh = nganh
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print(" Sửa thành công!")


        else:
            print(" Sinh viên có mã: {} không có trong danh sách.".format(id))
 
# Hàm tìm kiếm sinh viên theo mã sv
# Trả về một sinh viên theo mã sv
    def findByID(self, id):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == id):
                    searchResult = sv
        return searchResult

# Hàm tìm kiếm sinh viên theo tên
# Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

# Hàm xóa sinh viên theo mã sv
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
 
#Hàm xếp loại học lực cho sinh vien
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "A"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "B"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "C"
        elif(sv._diemTB >= 4):
            sv._hocLuc = "D"
        else:
            sv._hocLuc = "F"
 
# Hàm hiển thị danh sách sinh viên ra màn hình console
    def showSinhVien(self, listSV):
        # hiển thij tiêu đề cột
        print("{:<10} {:<18} {:<10} {:<10} {:<15} {:<12} {:<8} "
              .format("Mã SV", "Họ và tên", "Giới tính", "tuổi", "Ngành", "Điểm tổng", "Học lực"))
        # Hiển thị danh sách sinh viên
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<10} {:<18} {:<10} {:<10} {:<15} {:<12} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._nganh, sv._diemTB,  sv._hocLuc))
        
# Hàm trả về danh sách sinh viên hiện tại
    def getListSinhVien(self):
        return self.listSinhVien