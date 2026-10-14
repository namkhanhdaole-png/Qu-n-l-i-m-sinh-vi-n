
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# 2. Tao du lieu sinh vien
data = {
    "Ho_ten": [
        "Nguyen Hoang Anh",
        "Tran Binh",
        "Ga Sinh Ton",
        "Khanh Sky",
        "Hieuthuhai",
        "Ngo Minh Duc",
        "Trinh Tong",
        "Ha Linh",
        "Son Tung",
        "Jack"
    ],
    "Chuyen_can": [9, 8, 10, 7, 8, 9, 6, 10, 7, 8],
    "Giua_ky": [8, 7, 9, 6, 8, 7, 5, 9, 6, 8],
    "Cuoi_ky": [9, 8, 9, 5, 7, 8, 6, 10, 5, 9]
}

df = pd.DataFrame(data)

# 3. Tinh diem tong ket
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# 4. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Tieu de web
st.title("QUAN LY DIEM SINH VIEN")
st.write("Thong tin va ket qua hoc tap cua sinh vien.")

# 6. Hien thi bang diem
st.subheader("1. Bang diem sinh vien")

bang_diem = df.rename(columns={
    "Ho_ten": "Ho va ten",
    "Chuyen_can": "Chuyen can",
    "Giua_ky": "Giua ky",
    "Cuoi_ky": "Cuoi ky",
    "Tong_ket": "Tong ket",
    "Xep_loai": "Xep loai"
})

st.dataframe(bang_diem, use_container_width=True)

# 7. Thong ke ket qua
st.subheader("2. Thong ke ket qua hoc tap")

diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Diem trung binh", f"{diem_tb:.2f}")
c2.metric("So sinh vien dat", f"{so_sv_dat}/10")
c3.metric("Diem cao nhat", f"{sv_max['Tong_ket']:.2f}")
c4.metric("Diem thap nhat", f"{sv_min['Tong_ket']:.2f}")

st.write(
    f"Sinh vien cao nhat: {sv_max['Ho_ten']} "
    f"({sv_max['Tong_ket']:.2f} diem)"
)

st.write(
    f"Sinh vien thap nhat: {sv_min['Ho_ten']} "
    f"({sv_min['Tong_ket']:.2f} diem)"
)

# 8. Chon sinh vien bang Selectbox
st.subheader("3. Tra cuu diem sinh vien")

ten_sv = st.selectbox(
    "Chon sinh vien:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("Ho va ten:", sv["Ho_ten"])
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", f"{sv['Tong_ket']:.2f}")
st.write("Xep loai:", sv["Xep_loai"])

# 9. Bieu do cot diem tong ket
st.subheader("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Diem tong ket cua 10 sinh vien")
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 10. Thong tin nguoi tao
st.divider()
st.caption("Nguoi tao: Đào Lê Nam Khánh| MSSV: 038208011474")
