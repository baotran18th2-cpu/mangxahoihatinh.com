import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Mạng Xã Hội Hà Tĩnh",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 MẠNG XÃ HỘI HÀ TĨNH - SOCIAL HÀ TĨNH")
st.markdown(f"📅 *Ngày cập nhật: {datetime.now().strftime('%d/%m/%Y')} | Năm học: 2025 - 2026 | Không gian kết nối tuổi trẻ*")
st.markdown("---")

st.info("🔥 **BẢNG TIN CHÍNH:** Chào mừng các bạn đến với không gian chia sẻ thông tin, học tập và kết nối cộng đồng mạng xã hội lớn nhất năm học 2025 - 2026!")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Đăng trạng thái mới (Post Feed)")
    noi_dung_status = st.text_area("Hôm nay bạn muốn chia sẻ điều gì với cộng đồng?", placeholder="Nhập suy nghĩ, câu chuyện hoặc khoảnh khắc của bạn ở đây...")
    if st.button("Đăng bài viết lên mạng xã hội"):
        if noi_dung_status:
            st.balloons()
            st.success("🎉 Bài viết của bạn đã được đăng công khai thành công!")
            st.write(f"**Trạng thái vừa đăng:** \"{noi_dung_status}\"")
        else:
            st.warning("Bạn hãy viết gì đó trước khi bấm đăng nhé!")
            
    st.markdown("---")

    st.header("📌 Bảng Tin Nổi Bật & Câu Chuyện")
    
    st.subheader("🌟 Hành trình tự hào của tuổi trẻ học đường")
    st.write(
        "Với tinh thần ham học hỏi và niềm đam mê lớn đối với ngoại ngữ, hành trình chinh phục tri thức "
        "của lứa tuổi học sinh luôn tràn đầy những trải nghiệm rực rỡ và sáng tạo. "
        "Đặc biệt, thành tích xuất sắc trong môn Tiếng Anh cấp Quốc gia chính là minh chứng sống động cho sự nỗ lực "
        "không ngừng nghỉ, vượt qua mọi giới hạn bản thân để vươn tới những đỉnh cao mới."
    )
    
    st.subheader("🍃 Góc Thơ Ca & Cảm Xúc Thanh Xuân")
    st.write(
        "\"Sách vở miệt mài gieo con chữ mới,\n"
        "Vươn tầm thế giới, rạng danh non sông.\n"
        "Tuổi trẻ hôm nay chung tay viết tới,\n"
        "Khát vọng bay cao, thỏa chí tang bồng!\n\n"
        "Bước qua thử thách, vững chãi niềm tin,\n"
        "Tương lai rộng mở phía trước đang nhìn.\n"
        "Đồng hành tri thức, bay xa muôn lối,\n"
        "Tự hào ý chí, bản lĩnh học sinh!\""
    )
    
    st.subheader("💡 Bí quyết & Kinh nghiệm học tập hiệu quả điểm cao")
    st.write(
        "1. **Chăm chỉ mỗi ngày:** Dành ít nhất 30 phút để luyện nghe, đọc và phản xạ tiếng Anh liên tục.\n"
        "2. **Không ngại vấp ngã:** Sai ở đâu sửa ở đó, biến lỗi sai thành bài học kinh nghiệm đắt giá.\n"
        "3. **Kết nối bạn bè:** Lập các nhóm học tập online/offline để cùng nhau trao đổi kiến thức khó.\n"
        "4. **Sử dụng công nghệ thông minh:** Tận dụng internet, các nền tảng mạng xã hội lành mạnh để học từ vựng và trau dồi kỹ năng mềm."
    )

    st.markdown("---")

    st.header("⏱️ Dòng thời gian hoạt động (Timeline)")
    st.markdown("🔹 **08:00 sáng:** Cập nhật xu hướng học tập mới cho học sinh khối THCS.")
    st.markdown("🔹 **10:30 sáng:** Phát động phong trào 'Giỏi tiếng Anh - Vững tương lai'.")
    st.markdown("🔹 **14:00 chiều:** Chia sẻ tài liệu ôn thi học sinh giỏi cấp Quốc gia.")
    st.markdown("🔹 **20:00 tối:** Giao lưu trực tuyến cùng cộng đồng mạng xã hội.")

with col2:
    st.header("📊 Thống Kê Cộng Đồng")
    st.metric(label="Thành viên trực tuyến", value="15,420", delta="+320 hôm nay")
    st.metric(label="Bài viết tổng cộng", value="1,280", delta="+45 bài mới")
    st.metric(label="Độ uy tín mạng xã hội", value="100%", delta="Verified ✅")
    
    st.markdown("---")
    st.header("🏆 Bảng Vàng Thành Tích")
    st.success("✨ **Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh** (Năm học 2025 - 2026)")
    st.info("🎯 Đạt giải thưởng cao trong các kỳ thi học sinh giỏi cấp toàn quốc.")
    
    st.markdown("---")
    st.header("🎵 Góc Giải Trí & Âm Nhạc")
    st.write("🎧 Nghe nhạc lofi thư giãn khi lướt mạng xã hội.")
    if st.button("Bật nhạc thư giãn 🎶"):
        st.success("Đang phát nhạc lofi chill... Chúc bạn lướt web vui vẻ!")
        
    st.markdown("---")
    st.header("🔗 Chuyên Mục Nhanh")
    st.markdown("- [Cổng thông tin giáo dục toàn quốc](#)")
    st.markdown("- [Góc ôn thi Tiếng Anh chuyên sâu](#)")
    st.markdown("- [Câu lạc bộ lập trình & công nghệ](#)")
    st.markdown("- [Diễn đàn chia sẻ tâm sự học đường](#)")

st.markdown("---")
st.header("❤️ Gửi lời nhắn & Góp ý cho mạng xã hội")
col_a, col_b = st.columns(2)

with col_a:
    ten_ban = st.text_input("Tên của bạn:")
    loi_nhan = st.text_area("Lời chúc / Cảm nhận khi lướt web:")
    if st.button("Gửi lời chúc lên hệ thống"):
        if ten_ban:
            st.balloons()
            st.success(f"Cảm ơn bạn **{ten_ban}** đã gửi lời chúc tuyệt vời! Hệ thống đã ghi nhận.")
        else:
            st.warning("Bạn vui lòng nhập tên trước khi gửi nhé!")

with col_b:
    st.subheader("📬 Hòm Thư Đóng Góp Cộng Đồng")
    st.write("Mọi ý kiến đóng góp, bài viết chia sẻ hay hình ảnh đẹp đều có thể gửi về hệ thống để làm phong phú thêm nội dung trang mạng xã hội.")
    st.write("🌐 **Phiên bản:** 3.0 (Siêu dài & Hoành tráng - Năm học 2025 - 2026)")

st.markdown("---")
st.markdown("© 2025 - 2026 **Mạng Xã Hội Hà Tĩnh**. Nơi kết nối tri thức, chia sẻ đam mê và lan tỏa tuổi trẻ học đường.")
