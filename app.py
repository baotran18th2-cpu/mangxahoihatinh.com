import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Mạng Xã Hội Hà Tĩnh",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 MẠNG XÃ HỘI HÀ TĨNH - SOCIAL HÀ TĨNH")
st.markdown(f"**Người sáng lập & Quản trị viên:** Nguyễn Trương Gia Hưng | **Trụ sở:** Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh")
st.markdown(f"📅 *Ngày tham gia: {datetime.now().strftime('%d/%m/%Y')} | Năm học: 2025 - 2026 (Lớp 8)*")
st.markdown("---")

st.info("🔥 **BẢNG TIN CHÍNH:** Chào mừng cộng đồng mạng đến với không gian chia sẻ của Nguyễn Trương Gia Hưng. Nơi kết nối niềm đam mê công nghệ và tiếng Anh tại Hà Tĩnh!")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Đăng trạng thái (Post Feed)")
  
    noi_dung_status = st.text_area("Hôm nay bạn muốn chia sẻ điều gì với cộng đồng Hà Tĩnh?", placeholder="Nhập trạng thái của bạn ở đây...")
    if st.button("Đăng bài viết (Post)"):
        if noi_dung_status:
            st.balloons()
            st.success("🎉 Bài viết của bạn đã được đăng lên Mạng Xã Hội Hà Tĩnh thành công!")
            st.write(f"**Trạng thái vừa đăng:** \"{noi_dung_status}\"")
        else:
            st.warning("Bạn hãy viết gì đó trước khi đăng nhé!")
            
    st.markdown("---")
    st.header("📰 Bài viết nổi bật từ Quản trị viên")
    
    st.subheader("🌟 Hành trình tự hào của chàng trai Thạch Khê")
    st.write(
        "Sinh ra và lớn lên tại Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh, "
        "Gia Hưng (sinh năm 2013, học sinh lớp 8) đã xuất sắc giành danh hiệu "
        "**Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh** trong năm học 2025-2026. "
        "Đây là một cột mốc tự hào không chỉ của riêng cá nhân mà còn lan tỏa năng lượng tích cực đến cộng đồng mạng Hà Tĩnh!"
    )

with col2:
    st.header("👤 Hồ sơ (Profile)")
    st.markdown("**Chủ tài khoản:** Nguyễn Trương Gia Hưng")
    st.markdown("📍 **Đến từ:** Thạch Khê, Hà Tĩnh")
    st.markdown("🏆 **Danh hiệu:** Siêu sao Tiếng Anh cấp Quốc gia")
    
    st.markdown("---")
    st.header("📊 Thống kê mạng xã hội")
    st.metric(label="Người theo dõi (Followers)", value="10,250", delta="+120 hôm nay")
    st.metric(label="Bài viết (Posts)", value="1", delta="Mới")
    st.metric(label="Độ uy tín", value="100%", delta="Verified ✅")

st.markdown("---")
st.markdown("© 2025 - 2026 **Mạng Xã Hội Hà Tĩnh**. Phát triển và quản lý bởi ÔNG ÍCH KHIÊM.")
