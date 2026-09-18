import streamlit as st
from datetime import datetime


st.set_page_config(
    page_title="Mạng Xã Hội Hà Tĩnh - Official",
    page_icon="🌐",
    layout="wide"
)


TU_KHOA_CAM = ["lồn", "cặc", "cu", "đụ", "địt", "đm", "vcl", "vl", "ngu", "óc chó", "chó", "súc vật"]

def kiem_tra_tu_bay(noi_dung):
    if not noi_dung:
        return False
    noi_dung_lower = noi_dung.lower()
    return any(tu in noi_dung_lower for tu in TU_KHOA_CAM)


if 'danh_sach_bai_viet' not in st.session_state:
    st.session_state.danh_sach_bai_viet = [
        {
            "id": 1,
            "ten": "Cristiano Ronaldo",
            "tich_xanh": "✅",
            "avatar": "⚽",
            "noi_dung": "Siuuuuu! Mạng Xã Hội Hà Tĩnh của Gia Hưng quá đỉnh, chúc mừng em trai đạt giải Quốc gia môn Tiếng Anh nhé!",
            "thoi_gian": "Hôm nay, 10:15",
            "binh_luan": [
                {
                    "ten": "Lionel Messi ✅", 
                    "noi_dung": "Tuyệt vời quá! Chúc mừng chủ nhà Gia Hưng nhé! 🐐",
                    "phan_hoi": [
                        {"ten": "Nguyễn Trương Gia Hưng ✅", "noi_dung": "Em cảm ơn anh Messi nhiều lắm ạ! Chúc anh luôn đỉnh cao!"}
                    ]
                },
                {
                    "ten": "Sơn Tùng M-TP ✅", 
                    "noi_dung": "Quá chuẩn anh CR7 ơi, trang web rất xịn!",
                    "phan_hoi": []
                },
                {
                    "ten": "Nguyễn Trương Gia Hưng ✅", 
                    "noi_dung": "Em cảm ơn anh Ronaldo, anh Messi và anh Tùng nhiều ạ! 🔥",
                    "phan_hoi": []
                }
            ]
        },
        {
            "id": 2,
            "ten": "Sơn Tùng M-TP",
            "tich_xanh": "✅",
            "avatar": "🎤",
            "noi_dung": "Muôn năm ánh sáng! Chào cộng đồng Hà Tĩnh nhé, bài viết rất chất lượng, truyền cảm hứng cho tuổi trẻ!",
            "thoi_gian": "Hôm nay, 11:00",
            "binh_luan": [
                {
                    "ten": "Jisoo BLACKPINK ✅", 
                    "noi_dung": "So cool! Hello Hà Tĩnh! ✨",
                    "phan_hoi": [
                        {"ten": "Sơn Tùng M-TP ✅", "noi_dung": "Thank you Jisoo! Let's make it awesome! 🌟"}
                    ]
                },
                {
                    "ten": "Cristiano Ronaldo ✅", 
                    "noi_dung": "Let's go! 🚀",
                    "phan_hoi": []
                }
            ]
        }
    ]


if 'dang_tra_ lời' not in st.session_state:
    st.session_state.dang_tra_loi = None


st.title("🌐 MẠNG XÃ HỘI HÀ TĨNH - SOCIAL CỘNG ĐỒNG")
st.markdown(f"📍 *Thạch Khê, Hà Tĩnh | 📅 Ngày cập nhật: {datetime.now().strftime('%d/%m/%Y')} | Năm học: 2025 - 2026*")
st.markdown("---")


st.info("🔥 **BẢNG TIN CHÍNH:** Không gian kết nối cộng đồng, chia sẻ tri thức học tập, cập nhật kinh tế - xã hội và giao lưu cùng các ngôi sao lớn có tích xanh chính chủ!")


col1, col2 = st.columns([2, 1])

with col1:
    
    st.header("📝 Đăng trạng thái mới (Post Feed)")
    
    col_input1, col_input2 = st.columns([2, 1])
    with col_input1:
        ten_dang_bai = st.text_input("Tên hiển thị của bạn (Bắt buộc):", placeholder="Nhập tên của bạn...")
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
            st.success(f"🎉 Cảm ơn **{ten_dang_bai}**! Bài viết của bạn đã được kiểm duyệt và đăng công khai thành công.")

    st.markdown("---")
    
 
    st.header("📈 Kinh Tế - Xã Hội & Nền Văn Minh Hà Tĩnh")
    st.markdown("*(Tổng hợp thông tin định hướng phát triển từ Báo Hà Tĩnh Điện Tử)*")
    
    st.subheader("🌾 1. Vóc dáng một vùng quê đổi mới và phát triển")
    st.write(
        "Hà Tĩnh đang vươn mình mạnh mẽ trên con đường công nghiệp hóa, hiện đại hóa nhưng vẫn giữ gìn trọn vẹn "
        "bản sắc văn hóa truyền thống xứ Nghệ. Các phong trào xây dựng nông thôn mới nâng cao, đô thị văn minh "
        "đã tạo nên diện mạo khang trang từ thành thị đến nông thôn, khẳng định tinh thần đoàn kết, ý chí tự lực "
        "và khát vọng vươn lên của người dân Hà Tĩnh."
    )
    
    st.subheader("💡 2. Đột phá về kinh tế biển, công nghiệp và tri thức trẻ")
    st.write(
        "Với các khu kinh tế trọng điểm, hạ tầng giao thông đồng bộ cùng tiềm năng lớn từ du lịch và kinh tế biển, "
        "Hà Tĩnh đang là điểm đến thu hút đầu tư uy tín. Đặc biệt, nguồn nhân lực trẻ năng động, ham học hỏi – tiêu biểu "
        "như thế hệ học sinh đạt giải cao trong các kỳ thi học sinh giỏi Quốc gia – chính là nền tảng tri thức vững chắc "
        "để đưa quê hương ngày càng giàu đẹp, văn minh."
    )

    st.markdown("---")

   
    st.header("📢 Bảng Tin Cộng Đồng & Tương Tác")
    
    for i, bai in enumerate(st.session_state.danh_sach_bai_viet):
        with st.container():
            st.markdown(f"### {bai['avatar']} **{bai['ten']}** {bai.get('tich_xanh', '')}  \n*{bai['thoi_gian']}*")
            st.write(bai['noi_dung'])
            
            st.markdown("💬 **Bình luận từ cộng đồng:**")
            if bai['binh_luan']:
                for j, bl in enumerate(bai['binh_luan']):
                    st.markdown(f"> **{bl['ten']}:** {bl['noi_dung']}")
                    
                   
                    if 'phan_hoi' in bl and bl['phan_hoi']:
                        for ph in bl['phan_hoi']:
                            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ 💬 **{ph['ten']}:** {ph['noi_dung']}")
                    
                  
                    col_nut_tra_loi, col_trong = st.columns([1, 5])
                    with col_nut_tra_loi:
                        if st.button("↪️ Trả lời", key=f"btn_reply_{i}_{j}"):
                            st.session_state.dang_tra_loi = f"{i}_{j}"
                    
                  
                    if st.session_state.dang_tra_loi == f"{i}_{j}":
                        with st.form(key=f"form_reply_{i}_{j}"):
                            st.markdown(f"**Đang trả lời bình luận của {bl['ten']}:**")
                            r_ten = st.text_input("Tên của bạn:", placeholder="Nhập tên...", key=f"rt_ten_{i}_{j}")
                            r_nd = st.text_input("Nội dung phản hồi:", placeholder="Nhập câu trả lời cho idol/bạn bè...", key=f"rt_nd_{i}_{j}")
                            submitted_reply = st.form_submit_button("Gửi phản hồi")
                            if submitted_reply:
                                if not r_ten.strip() or not r_nd.strip():
                                    st.warning("Vui lòng điền đủ tên và nội dung!")
                                elif kiem_tra_tu_bay(r_nd):
                                    st.error("Từ ngữ không hợp lệ!")
                                else:
                                    t_x = "✅" if "hưng" in r_ten.lower() else ""
                                    if 'phan_hoi' not in st.session_state.danh_sach_bai_viet[i]['binh_luan'][j]:
                                        st.session_state.danh_sach_bai_viet[i]['binh_luan'][j]['phan_hoi'] = []
                                    st.session_state.danh_sach_bai_viet[i]['binh_luan'][j]['phan_hoi'].append({
                                        "ten": f"{r_ten} {t_x}",
                                        "noi_dung": r_nd
                                    })
                                    st.session_state.dang_tra_loi = None
                                    st.success("Đã phản hồi thành công!")
                                    st.rerun()
            else:
                st.markdown("> *Chưa có bình luận nào. Hãy là người đầu tiên bình luận!*")
            
           
            with st.form(key=f"form_bl_{i}"):
                col_bl1, col_bl2 = st.columns([1, 2])
                with col_bl1:
                    ten_nguoi_bl = st.text_input("Tên của bạn:", placeholder="Nhập tên...", key=f"ten_{i}")
                with col_bl2:
                    noi_dung_bl = st.text_input("Viết bình luận:", placeholder="Nhập bình luận lịch sự...", key=f"nd_{i}")
                
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
                            "noi_dung": noi_dung_bl,
                            "phan_hoi": []
                        })
                        st.success("Đã gửi bình luận thành công!")
                        st.rerun()
                        
            st.markdown("---")
            
 
    st.header("📌 Câu Chuyện Nổi Bật & Tự Hào Quê Hương")
    st.subheader("🌟 Hành trình tự hào của tuổi trẻ Thạch Khê, Hà Tĩnh")
    st.write(
        "Sinh ra và lớn lên tại mảnh đất hiếu học Thôn Đình Hòe, xã Thạch Khê, tỉnh Hà Tĩnh, "
        "Nguyễn Trương Gia Hưng (học sinh lớp 8) đã xuất sắc ghi dấu ấn mạnh mẽ với danh hiệu "
        "**Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh** trong năm học 2025 - 2026. "
        "Đây là niềm tự hào lớn, minh chứng cho ý chí tự lực, tinh thần ham học hỏi và khát vọng vươn xa tầm quốc tế."
    )
    
    st.subheader("🍃 Góc Thơ Ca & Cảm Xúc Thanh Xuân")
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

    st.markdown("---")
    
 
    st.header("⏱️ Dòng thời gian hoạt động trong ngày (Timeline)")
    st.markdown("🔹 **08:00 sáng:** Cập nhật bản tin kinh tế - xã hội và xu hướng học tập mới.")
    st.markdown("🔹 **10:30 sáng:** Phát động phong trào xây dựng văn minh đô thị tại Thạch Khê, Hà Tĩnh.")
    st.markdown("🔹 **14:00 chiều:** Chia sẻ tài liệu ôn thi học sinh giỏi cấp Quốc gia môn Tiếng Anh.")
    st.markdown("🔹 **20:00 tối:** Giao lưu trực tuyến cùng cộng đồng mạng xã hội và các ngôi sao lớn.")

with col2:
    # --- CỘT PHẢI: THỐNG KÊ & THÀNH TÍCH ---
    st.header("📊 Thống Kê Cộng Đồng")
    st.metric(label="Thành viên trực tuyến", value="15,420", delta="+320 hôm nay")
    st.metric(label="Ngôi sao tích xanh", value="Ronaldo, Messi, Tùng, Jisoo ✅", delta="Chính chủ 🌟")
    st.metric(label="Hệ thống kiểm duyệt", value="Đang bật 🛡️", delta="An toàn 100%")
    
    st.markdown("---")
    st.header("🏆 Bảng Vàng Danh Dự")
    st.success("✨ **Nguyễn Trương Gia Hưng** ✅\n\n📌 Học sinh xuất sắc cấp Quốc gia môn Tiếng Anh (Năm học 2026 - 2027)\n\n📍 Thạch Khê, Hà Tĩnh")
    st.info("🎯 Tấm gương sáng trong học tập và rèn luyện của tuổi trẻ địa phương.")
    
    st.markdown("---")
    st.header("🎵 Góc Phát Nhạc Lofi Chill")
    st.write("🎧 Mở nhạc lofi cực chill để lướt feed nào:")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3", format="audio/mp3")
        
    st.markdown("---")
    st.header("🔗 Các Đường Link Tiện Ích Thật")
    st.markdown("- 📰 [Báo Hà Tĩnh Điện Tử](https://baohatinh.vn)")
    st.markdown("- 📖 [Từ Điển Tiếng Anh Cambridge](https://dictionary.cambridge.org)")
    st.markdown("- 🌐 [Cổng Thông Tin Chính Phủ](https://chinhphu.vn)")


st.markdown("---")
st.markdown("© 2026 - 2027 **Mạng Xã Hội Hà Tĩnh**. Nơi kết nối tri thức, ngôi sao tích xanh và tuổi trẻ học đường.")
