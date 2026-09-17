import streamlit as st
st.set_page_config(page_title="Trang web của Nguyễn Trương Gia Hưng", page_icon="🌟")
st.balloons()
st.title("📰 BÁO HÀ TĨNH XIN CHÀO 🌟")
st.write("---")
st.header("👤 Sơ yếu lý lịch siêu ngầu")
st.markdown("**Họ và tên:** Nguyễn Trương Gia Hưng")
st.markdown("**Năm sinh:** 2013")
st.markdown("**Năm học:** 2025 - 2026 (Học sinh lớp 8)")
st.markdown("**Quê quán:** Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh")
st.header("🏆 Góc Flex Thành Tích")
st.success("✨ Đã giành danh hiệu **Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh**!")
st.write("Đây là thành quả của sự nỗ lực không ngừng nghỉ và niềm đam mê lớn với ngoại ngữ của mình trong năm học vừa qua.")
st.header("💬 Lời chia sẻ của tôi")
st.info(
    "\"Xin chào mọi người, mình là Gia Hưng đến từ Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh đây! "
    "Hành trình học tập năm 2025-2026 của mình có rất nhiều điều thú vị. "
    "Mình rất vui được chia sẻ niềm đam mê tiếng Anh và những kỷ niệm này cùng tất cả các bạn!\"")
st.header("❤️ Gửi lời chúc cho chủ web nhé")
if st.button("Bấm vào đây để tặng tim cho Gia Hưng"):
    st.balloons()
    st.success("Cảm ơn bạn đã ghé thăm và tặng tim cho mình! Chúc bạn một năm học 2025-2026 thật rực rỡ nhé!")
