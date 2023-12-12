list_student = [
    {
        "msv": 1, "ten": "Sinh vien 1", "toan": 9, "van": 7, "hoa": 8
    },
    {   "msv": 2, "ten": "Sinh vien 2", "toan": 8, "van": 8, "hoa": 8
    },
    {   "msv": 3, "ten": "Sinh vien 3", "toan": 5, "van": 7, "hoa": 6
    },
    {
        "msv": 4,
        "ten": "Sinh vien 4",
        "toan": 7,
        "van": 8,
        "hoa": 4
    }
    ,{
        "msv": 5,
        "ten": "Sinh vien 5",
        "toan": 10,
        "van": 5,
        "hoa": 7
    }
]

for student in list_student:
    diem_trung_binh = (student["toan"] + student["van"] + student["hoa"]) / 3
    if diem_trung_binh > 5:
        print("Sinh vien co diem trung binh hon 5: ", student)
    if student["hoa"] < 5:
        print("Sinh vien co diem hoa duoi 5: ", student)

