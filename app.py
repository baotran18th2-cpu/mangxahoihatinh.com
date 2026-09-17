import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Mạng Xã Hội Hà Tĩnh",
    page_icon="🌐",
    layout="wide"
)

TU_KHOA_CAM = ["lồn", "cặc", "cu", "đụ", "địt", "đm", "vcl", "vl", "ngu", "óc chó", "oc cho", "chó", "súc vật", "ngu ngốc"]

def kiem_tra_tu_bay(noi_dung):
    noi_dung_lower = noi_dung.lower()
    for tu in TU_KHOA_CAM:
        if tu in noi_dung_lower:
            return True
    return False
st.title("🌐 MẠNG XÃ HỘI HÀ TĨNH - SOCIAL HÀ TĨNH")
st.markdown(f"📍 *Thạch Khê, Hà Tĩnh | Ngày cập nhật: {datetime.now().strftime('%d/%m/%Y')} | Năm học: 2025 - 2026*")
st.markdown("---")

st.info("🔥 **BẢNG TIN CHÍNH:** Không gian kết nối cộng đồng, chia sẻ niềm đam mê học tập và lan tỏa những giá trị tốt đẹp tại Hà Tĩnh!")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Đăng trạng thái mới (Post Feed)")
    ten_dang_bai = st.text_input("Tên của bạn (Bắt buộc):", placeholder="Nhập tên hiển thị...")
    noi_dung_status = st.text_area("Hôm nay bạn muốn chia sẻ điều gì?", placeholder="Nhập nội dung trạng thái văn minh, lịch sự...")
    
    if st.button("Đăng bài viết lên mạng xã hội"):
        if not ten_dang_bai.strip():
            st.warning("⚠️ Bạn vui lòng nhập tên của mình trước khi đăng bài!")
        elif not noi_dung_status.strip():
            st.warning("⚠️ Nội dung bài viết không được để trống!")
        elif kiem_tra_tu_bay(noi_dung_status) or kiem_tra_tu_bay(ten_dang_bai):
            st.error("🚫 **Cảnh báo hệ thống:** Bài viết chứa từ ngữ không phù hợp hoặc kém văn minh! Mạng Xã Hội Hà Tĩnh nghiêm cấm các từ ngữ tục tữu.")
        else:
            st.balloons()
            st.success(f"🎉 Cảm ơn **{ten_dang_bai}**! Bài viết của bạn đã được kiểm duyệt và đăng công khai thành công.")
            st.write(f"💬 **[{ten_dang_bai}] vừa đăng:** \"{noi_dung_status}\"")
            
    st.markdown("---")
    
    st.header("📌 Bảng Tin Nổi Bật & Câu Chuyện")
    
    st.subheader("🌟 Hành trình tự hào của tuổi trẻ Thạch Khê, Hà Tĩnh")
    st.write(
        "Sinh ra và lớn lên tại mảnh đất hiếu học Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh, "
        "Nguyễn Trương Gia Hưng (học sinh lớp 8) đã xuất sắc ghi dấu ấn mạnh mẽ với danh hiệu "
        "**Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh** trong năm học 2025 - 2026. "
        "Đây là niềm tự hào lớn, minh chứng cho ý chí tự lực, tinh thần ham học hỏi và khát vọng vươn xa."
    )
    
    st.subheader("🍃 Góc Thơ Ca & Cảm Xúc Quê Hương")
    st.write(
        "\"Hà Tĩnh quê mình biển biếc trời xanh,\n"
        "Thạch Khê yêu dấu bước chân anh hình.\n"
        "Sách vở miệt mài gieo con chữ mới,\n"
        "Vươn tầm thế giới, rạng danh tình quê!\n\n"
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
    st.markdown("🔹 **08:00 sáng:** Cập nhật xu hướng học tập mới cho học sinh khối THCS tại Hà Tĩnh.")
    st.markdown("🔹 **10:30 sáng:** Phát động phong trào 'Giỏi tiếng Anh - Vững tương lai'.")
    st.markdown("🔹 **14:00 chiều:** Chia sẻ tài liệu ôn thi học sinh giỏi cấp Quốc gia.")
    st.markdown("🔹 **20:00 tối:** Giao lưu trực tuyến cùng cộng đồng mạng xã hội.")

with col2:

    st.header("📊 Thống Kê Cộng Đồng")
    st.metric(label="Thành viên trực tuyến", value="15,420", delta="+320 hôm nay")
    st.metric(label="Bài viết tổng cộng", value="1,280", delta="+45 bài mới")
    st.metric(label="Chế độ kiểm duyệt từ bấy", value="Đang bật 🛡️", delta="An toàn 100%")
    
    st.markdown("---")
    st.header("🏆 Bảng Vàng Thành Tích")
    st.success("✨ **Nguyễn Trương Gia Hưng**\n\n📌 Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh (Năm học 2025 - 2026)\n\n📍 Thạch Khê, Hà Tĩnh")
    st.info("🎯 Tấm gương sáng trong học tập và rèn luyện của tuổi trẻ địa phương.")
    
    st.markdown("---")
    st.header("🎵 Góc Giải Trí & Âm Nhạc")
    st.write("🎧 Thư giãn cùng âm nhạc khi lướt mạng xã hội.")
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
    ten_chuc = st.text_input("Tên của bạn (Bắt buộc để gửi lời chúc):", placeholder="Nhập tên của bạn...")
    loi_nhan = st.text_area("Lời chúc / Cảm nhận khi lướt web:", placeholder="Nhập lời chúc văn minh...")
    
    if st.button("Gửi lời chúc lên hệ thống"):
        if not ten_chuc.strip():
            st.warning("⚠️ Bạn vui lòng nhập tên trước khi gửi lời chúc!")
        elif not loi_nhan.strip():
            st.warning("⚠️ Lời chúc không được để trống!")
        elif kiem_tra_tu_bay(loi_nhan) or kiem_tra_tu_bay(ten_chuc):
            st.error("🚫 **Cảnh báo hệ thống:** Lời chúc chứa từ ngữ không phù hợp! Vui lòng sử dụng ngôn từ lịch sự.")
        else:
            st.balloons()
            st.success(f"Cảm ơn bạn **{ten_chuc}** đã gửi lời chúc tuyệt vời! Hệ thống đã ghi nhận.")

with col_b:
    st.subheader("📬 Quy tắc cộng đồng")
    st.write("- Mọi ý kiến đóng góp, bài viết chia sẻ lịch sự đều được hoan nghênh.")
    st.write("- **Hệ thống tự động từ chối** các từ ngữ tục tữu, phản cảm để xây dựng môi trường mạng trong sạch.")
    st.write("🌐 **Phiên bản:** 3.1 (Bảo mật & Kiểm duyệt thông minh - Năm học 2025 - 2026)")

st.markdown("---")
st.markdown("© 2025 - 2026 **Mạng Xã Hội Hà Tĩnh**. Nơi kết nối tri thức, chia sẻ đam mê và lan tỏa tuổi trẻ học đường.")
