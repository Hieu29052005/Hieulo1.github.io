import math
from main.SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien()>0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId<sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        age = int(input("Nhap tuoi sinh vien: "))
        diemToan = float(input("Nhap diem toan sinh vien: "))
        diemLy = float(input("Nhap diem ly cua ban: "))
        diemHoa = float(input("Nhap diem hoa sinh vien: "))
        sv = SinhVien(svId,name,sex,age,diemToan,diemLy,diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    def updateSinhVien(self,ID):
        sv:SinhVien = self.findById(ID)
        if(sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            age = int(input("Nhap tuoi sinh vien: "))
            diemToan = float(input("Nhap diem toan sinh vien: "))
            diemLy = float(input("Nhap diem ly sinh vien: "))
            diemHoa = float(input("Nhap diem hoa cua ban: "))
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID={} khong ton tai".format(ID))
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse = False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse = False)
    def sortByDiemTB(self):
        self.listSinhVien.sort(key =lambda x: x._diemTB, reverse = False)
    def findByID(self,ID):
        searchResult = None
        if (self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    def findByName(self,keyword):
        listSV = []
        if(self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteById(self,ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    def tinhDTB(self,sv:SinhVien):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa)/3
        sv._diemTB = math.ceil(diemTB*100)/100
    def xepLoaiHocLuc(self,sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._diemTB = "Gioi"
        elif(sv._diemTB >= 6.5):
            sv._diemTB = "Kha"
        elif(sv._diemTB >= 5):
            sv._diemTB = "Trung binh"
        else:
            sv._diemTB = "Yeu"
    def showSinhVien(self,listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}".format("ID","Sex","Age","Toan","Ly","Hoa","Diem TB","Hoc Luc"))
        if(listSV.__len__()>0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}".format(sv._id,sv._name,sv._sex,sv._diemToan,sv._diemLy,sv._diemHoa,sv._diemTB,sv._hocLuc))
        print("\n")
    def getListSinhVien(self):
        return self.getListSinhVien                         