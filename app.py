import streamlit as st

st.set_page_config(page_title="Tính Thuế TNCN", page_icon="💰", layout="centered")

st.image("LOGOO.jpg", use_container_width=True)

st.title("💰 TÍNH THUẾ THU NHẬP CÁ NHÂN - ĐỀ TÀI 4 TRẦN THỊ THẢO VY")

thu_nhap = st.number_input(
"Nhập thu nhập trước thuế (VNĐ):",
min_value=0,
value=20000000
)

so_phu_thuoc = st.number_input(
"Nhập số người phụ thuộc:",
min_value=0,
value=0
)

st.divider()

if st.button("📊 Tính toán"):
    thue = thu_nhap_tinh_thue * 0.05
    st.write(thue)
giam_tru_ban_than = 11000000
giam_tru_phu_thuoc = 4400000 * so_phu_thuoc

thu_nhap_tinh_thue = max(
    0,
    thu_nhap - giam_tru_ban_than - giam_tru_phu_thuoc
)

thue = thu_nhap_tinh_thue * 0.05

st.header("📈 Kết quả tính toán")

st.success("Tính toán thành công!")

st.write(f"📌 Thu nhập tính thuế: **{thu_nhap_tinh_thue:,.0f} VNĐ**")
st.write(f"📌 Thuế TNCN phải nộp: **{thue:,.0f} VNĐ**")
st.write(f"📌 Thu nhập sau thuế: **{thu_nhap - thue:,.0f} VNĐ**")
if st.button("📊 Tính toán"):

