import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

# 2. Tạo dữ liệu sinh viên
data = {
    "Ho_ten": [
        "Nguyễn Hoàng Anh",
        "Trần Bình",
        "Gà Sinh Tồn",
        "Khánh Sky",
        "Hieuthuhai",
        "Ngô Minh Đức",
        "Trịnh Tống",
        "Hà Linh",
        "Sơn Tùng",
        "Jack"
    ],
    "Chuyen_can": [9, 8, 10, 7, 8, 9, 6, 10, 7, 8],
    "Giua_ky": [8, 7, 9, 6, 8, 7, 5, 9, 6, 8],
    "Cuoi_ky": [9, 8, 9, 5, 7, 8, 6, 10, 5, 9]
}

df = pd.DataFrame(data)

# 3. Tính điểm tổng kết
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# 4. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Tiêu đề web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Thông tin và kết quả học tập của sinh viên.")

# 6. Hiển thị bảng điểm
st.subheader("1. Bảng điểm sinh viên")

bang_diem = df.rename(columns={
    "Ho_ten": "Họ và tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_diem, use_container_width=True)

# 7. Thống kê kết quả
st.subheader("2. Thống kê kết quả học tập")

diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
c3.metric("Điểm cao nhất", f"{sv_max['Tong_ket']:.2f}")
c4.metric("Điểm thấp nhất", f"{sv_min['Tong_ket']:.2f}")

st.write(
    f"Sinh viên cao nhất: {sv_max['Ho_ten']} "
    f"({sv_max['Tong_ket']:.2f} điểm)"
)

st.write(
    f"Sinh viên thấp nhất: {sv_min['Ho_ten']} "
    f"({sv_min['Tong_ket']:.2f} điểm)"
)

# 8. Chọn sinh viên bằng Selectbox
st.subheader("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("Họ và tên:", sv["Ho_ten"])
st.write("Điểm chuyên cần:", sv["Chuyen_can"])
st.write("Điểm giữa kỳ:", sv["Giua_ky"])
st.write("Điểm cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", f"{sv['Tong_ket']:.2f}")
st.write("Xếp loại:", sv["Xep_loai"])

# 9. Biểu đồ cột điểm tổng kết
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 10. Thông tin người tạo
st.divider()
st.caption("Người tạo: Đào Lê Nam Khánh | MSSV: 038208011474")
