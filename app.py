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

if 'danh_sach_bai_viet' not in st.session_state:
    st.session_state.danh_sach_bai_viet = [
        {
            "id": 1,
            "ten": "Cristiano Ronaldo",
            "tich_xanh": "✅",
            "avatar": "⚽",
            "noi_dung": "Siuuuuu! Trang Mạng Xã Hội Hà Tĩnh của Gia Hưng quá đỉnh, chúc mừng em trai đạt giải Quốc gia nhé!",
            "thoi_gian": "Hôm nay, 10:15",
            "binh_luan": [
                {"ten": "Lionel Messi ✅", "noi_dung": "Tuyệt vời quá! Chúc mừng chủ nhà Gia Hưng nhé! 🐐"},
                {"ten": "Sơn Tùng M-TP ✅", "noi_dung": "Quá chuẩn anh CR7 ơi, trang web rất xịn!"},
                {"ten": "Nguyễn Trương Gia Hưng ✅", "noi_dung": "Em cảm ơn anh Ronaldo, anh Messi và anh Tùng nhiều ạ! 🔥"}
            ]
        },
        {
            "id": 2,
            "ten": "Sơn Tùng M-TP",
            "tich_xanh": "✅",
            "avatar": "🎤",
            "noi_dung": "Muôn năm ánh sáng! Chào cộng đồng Hà Tĩnh nhé, bài viết rất chất lượng và truyền cảm hứng!",
            "thoi_gian": "Hôm nay, 11:00",
            "binh_luan": [
                {"ten": "Jisoo BLACKPINK ✅", "noi_dung": "So cool! Hello Hà Tĩnh! ✨"},
                {"ten": "Cristiano Ronaldo ✅", "noi_dung": "Let's go! 🚀"}
            ]
        }
    ]
st.title("🌐 MẠNG XÃ HỘI HÀ TĨNH - SOCIAL HÀ TĨNH")
st.markdown(f"📍 *Thạch Khê, Hà Tĩnh | Ngày cập nhật: {datetime.now().strftime('%d/%m/%Y')} | Năm học: 2025 - 2026*")
st.markdown("---")

st.info("🔥 **BẢNG TIN CHÍNH:** Không gian kết nối cộng đồng, chia sẻ niềm đam mê và giao lưu cùng các ngôi sao lớn đều có tích xanh chính chủ!")

col1, col2 = st.columns([2, 1])

with col1:
  
    st.header("📝 Đăng trạng thái mới (Post Feed)")
    
    col_input1, col_input2 = st.columns([2, 1])
    with col_input1:
        ten_dang_bai = st.text_input("Tên của bạn (Bắt buộc):", placeholder="Nhập tên hiển thị...")
    with col_input2:
        avatar_chon = st.selectbox("Chọn Avatar:", ["👤 Người dùng", "😎 Cool ngầu", "🚀 Phi hành gia", "🔥 Ngọn lửa", "🌟 Ngôi sao", "⚽ Cầu thủ", "🎤 Ca sĩ"])
        
    noi_dung_status = st.text_area("Hôm nay bạn muốn chia sẻ điều gì với cộng đồng?", placeholder="Nhập nội dung trạng thái văn minh, lịch sự...")
    
    if st.button("Đăng bài viết lên mạng xã hội"):
        if not ten_dang_bai.strip():
            st.warning("⚠️ Bạn vui lòng nhập tên của mình trước khi đăng bài!")
        elif not noi_dung_status.strip():
            st.warning("⚠️ Nội dung bài viết không được để trống!")
        elif kiem_tra_tu_bay(noi_dung_status) or kiem_tra_tu_bay(ten_dang_bai):
            st.error("🚫 **Cảnh báo hệ thống:** Bài viết chứa từ ngữ không phù hợp hoặc kém văn minh!")
        else:
            st.balloons()
            # Tự động cấp tích xanh nếu là Gia Hưng hoặc Admin
            co_tich_xanh = "✅" if "hưng" in ten_dang_bai.lower() or "admin" in ten_dang_bai.lower() else ""
            st.session_state.danh_sach_bai_viet.insert(0, {
                "id": len(st.session_state.danh_sach_bai_viet) + 1,
                "ten": ten_dang_bai,
                "tich_xanh": co_tich_xanh,
                "avatar": avatar_chon.split()[0],
                "noi_dung": noi_dung_status,
                "thoi_gian": "Vừa xong",
                "binh_luan": []
            })
            st.success(f"🎉 Cảm ơn **{ten_dang_bai}**! Bài viết đã được đăng thành công.")

    st.markdown("---")
  
    st.header("📢 Bảng Tin Cộng Đồng & Tương Tác")
    
    for i, bai in enumerate(st.session_state.danh_sach_bai_viet):
        with st.container():
            st.markdown(f"### {bai['avatar']} **{bai['ten']}** {bai.get('tich_xanh', '')}  \n*{bai['thoi_gian']}*")
            st.write(bai['noi_dung'])
            
            st.markdown("💬 **Bình luận:**")
            if bai['binh_luan']:
                for bl in bai['binh_luan']:
                    st.markdown(f"> **{bl['ten']}:** {bl['noi_dung']}")
            else:
                st.markdown("> *Chưa có bình luận nào. Hãy là người đầu tiên bình luận!*")
            
            with st.form(key=f"form_bl_{i}"):
                col_bl1, col_bl2 = st.columns([1, 2])
                with col_bl1:
                    ten_nguoi_bl = st.text_input("Tên của bạn:", placeholder="Nhập tên...", key=f"ten_{i}")
                with col_bl2:
                    noi_dung_bl = st.text_input("Viết bình luận:", placeholder="Nhập bình luận văn minh...", key=f"nd_{i}")
                
                nut_gui_bl = st.form_submit_button("Gửi bình luận")
                if nut_gui_bl:
                    if not ten_nguoi_bl.strip():
                        st.warning("⚠️ Vui lòng nhập tên trước khi bình luận!")
                    elif not noi_dung_bl.strip():
                        st.warning("⚠️ Nội dung bình luận không được để trống!")
                    elif kiem_tra_tu_bay(noi_dung_bl) or kiem_tra_tu_bay(ten_nguoi_bl):
                        st.error("🚫 Bình luận chứa từ ngữ không phù hợp!")
                    else:
                        ten_hien_thi_bl = f"{ten_nguoi_bl} ✅" if "hưng" in ten_nguoi_bl.lower() else ten_nguoi_bl
                        st.session_state.danh_sach_bai_viet[i]['binh_luan'].append({
                            "ten": ten_hien_thi_bl,
                            "noi_dung": noi_dung_bl
                        })
                        st.success("Đã gửi bình luận thành công!")
                        st.rerun()
                        
            st.markdown("---")
            
    st.header("📌 Câu Chuyện Nổi Bật")
    st.subheader("🌟 Hành trình tự hào của tuổi trẻ Thạch Khê, Hà Tĩnh")
    st.write(
        "Sinh ra và lớn lên tại mảnh đất hiếu học Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh, "
        "Nguyễn Trương Gia Hưng (học sinh lớp 8) đã xuất sắc ghi dấu ấn mạnh mẽ với danh hiệu "
        "**Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh** trong năm học 2025 - 2026. "
        "Đây là niềm tự hào lớn, lan tỏa năng lượng tích cực đến toàn thể cộng đồng mạng."
    )

with col2:
    st.header("📊 Thống Kê Cộng Đồng")
    st.metric(label="Thành viên trực tuyến", value="15,420", delta="+320 hôm nay")
    st.metric(label="Ngôi sao có tích xanh", value="Ronaldo, Messi, Tùng, Jisoo ✅", delta="Chính chủ 🌟")
    st.metric(label="Chế độ kiểm duyệt", value="Đang bật 🛡️", delta="An toàn 100%")
    
    st.markdown("---")
    st.header("🏆 Bảng Vàng Thành Tích")
    st.success("✨ **Nguyễn Trương Gia Hưng** ✅\n\n📌 Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh (Năm học 2025 - 2026)\n\n📍 Thạch Khê, Hà Tĩnh")
    st.info("🎯 Tấm gương sáng trong học tập và rèn luyện của tuổi trẻ địa phương.")
    
    st.markdown("---")
    st.header("🎵 Góc Phát Nhạc MP3 Trực Tuyến")
    st.write("🎧 Nghe bản nhạc lofi thư giãn trực tiếp trên web:")
    # Nhúng trực tiếp trình phát nhạc MP3 từ đường link mẫu công khai
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
        
    st.markdown("---")
    st.header("🔗 Các Đường Link Tiện Ích Thật")
    st.markdown("- 📰 [Báo Hà Tĩnh Điện Tử](https://baohatinh.vn)")
    st.markdown("- 📖 [Từ Điển Tiếng Anh Cambridge](https://dictionary.cambridge.org)")
    st.markdown("- 🌐 [Cổng Thông Tin Chính Phủ](https://chinhphu.vn)")
    st.markdown("- 💻 [Học Lập Trình Cùng Python](https://www.python.org)")

st.markdown("---")
st.markdown("© 2025 - 2026 **Mạng Xã Hội Hà Tĩnh**. Nơi kết nối tri thức, ngôi sao tích xanh và tuổi trẻ học đường.")
