class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi) -> None:
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"Mã khoá học: {self.maKhoaHoc} \nTên khoá học: {self.tenKhoaHoc} \nHình thức: {self.hinhThuc} \nHọc phí: {self.hocPhi}"

class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc = []) -> None:
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHocMoi):
        return self.khoaHoc.append(khoaHocMoi)

    def hienThiKhoaHoc(self):
        print("--------------------------------")
        print(f"Khoa hoc cua hoc vien {self.tenHV}")
        for k in self.khoaHoc:
            print("++++++++")
            print(k.thongTinKhoaHoc())

kh1 = KhoaHoc("KH01", "Lap trinh Python", "Offline", 500)
kh2 = KhoaHoc("KH02", "Lap trinh JavaScript", "Online", 400)
kh3 = KhoaHoc("KH03", "Lap trinh Java", "Online", 1000)


hv1 = HocVien("HV01", "Tran Van A", "01/01/1993")
hv2 = HocVien("HV02", "Le Thi B", "01/11/1998")

hv1.dangKyKhoaHoc(kh1)
hv1.dangKyKhoaHoc(kh2)

hv2.dangKyKhoaHoc(kh2)
hv2.dangKyKhoaHoc(kh3)

hv1.hienThiKhoaHoc()
hv2.hienThiKhoaHoc()