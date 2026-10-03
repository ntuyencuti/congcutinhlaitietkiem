import streamlit as st
st.image("logo.jpg.HEIC")
# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM NGÂN HÀNG")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

# =========================
# NHẬP DỮ LIỆU
# =========================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    if tien_gui <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")
    elif lai_suat < 0:
        st.error("Lãi suất không hợp lệ.")
    else:

        # Đổi lãi suất % sang số thập phân
        lai_suat_nam = lai_suat / 100

        # Tính tổng tiền lãi
        # Lãi đơn theo công thức:
        # Tiền lãi = Tiền gửi × Lãi suất năm × Số tháng / 12
        tong_lai = tien_gui * lai_suat_nam * ky_han / 12

        # =========================
        # TÍNH LÃI ĐỊNH KỲ
        # =========================

        if hinh_thuc == "Cuối kỳ":

            tien_lai_dinh_ky = tong_lai
            so_ky = 1

        elif hinh_thuc == "Hàng tháng":

            tien_lai_dinh_ky = tong_lai / ky_han
            so_ky = ky_han

        else:  # Hàng quý

            so_quy = ky_han / 3
            tien_lai_dinh_ky = tong_lai / so_quy
            so_ky = so_quy

        # Tổng tiền gốc + lãi
        tong_goc_lai = tien_gui + tong_lai

        # =========================
        # HIỂN THỊ KẾT QUẢ
        # =========================

        st.success("✅ TÍNH TOÁN THÀNH CÔNG")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "💰 Tiền lãi định kỳ",
                f"{tien_lai_dinh_ky:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "📈 Tổng tiền lãi",
                f"{tong_lai:,.0f} VNĐ"
            )

        st.metric(
            "🏦 Tổng tiền gốc + lãi",
            f"{tong_goc_lai:,.0f} VNĐ"
        )

        # =========================
        # THÔNG TIN CHI TIẾT
        # =========================

        st.subheader("📋 Thông tin khoản gửi")

        st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
        st.write(f"**Kỳ hạn:** {ky_han} tháng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

        if hinh_thuc == "Cuối kỳ":
            st.info(
                f"Bạn nhận toàn bộ tiền lãi {tong_lai:,.0f} VNĐ "
                f"vào cuối kỳ."
            )

        elif hinh_thuc == "Hàng tháng":
            st.info(
                f"Mỗi tháng bạn nhận khoảng "
                f"{tien_lai_dinh_ky:,.0f} VNĐ tiền lãi."
            )

        else:
            st.info(
                f"Mỗi quý bạn nhận khoảng "
                f"{tien_lai_dinh_ky:,.0f} VNĐ tiền lãi."
            )

# =========================
# CÔNG THỨC
# =========================

with st.expander("📖 Xem công thức tính"):

    st.write("**Tổng tiền lãi:**")

    st.latex(
        r"\text{Tiền lãi} = "
        r"\text{Tiền gửi} \times "
        r"\text{Lãi suất năm} \times "
        r"\frac{\text{Số tháng}}{12}"
    )

    st.write("**Tổng tiền nhận được:**")

    st.latex(
        r"\text{Gốc + Lãi} = "
        r"\text{Tiền gửi} + \text{Tổng tiền lãi}"
    )
