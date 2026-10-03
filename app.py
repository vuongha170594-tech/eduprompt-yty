import streamlit as st

# 1. Cấu hình trang
st.set_page_config(
    page_title="EduPrompt Y Tý - Trợ lý Tạo Prompt Infographic",
    page_icon="🎨",
    layout="centered"
)

# 2. Trang trí Giao diện bằng CSS nâng cao (Hình nền Y Tý & Khung màu sắc)
st.markdown("""
<style>
    /* Tải ảnh nền Y Tý mờ nghệ thuật */
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)), 
                          url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=1600');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Tiêu đề chính */
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 2.3rem;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .sub-title {
        text-align: center;
        color: #059669;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* Phong cách Khung The (Card) cho từng mục */
    .card-box {
        background: rgba(255, 255, 255, 0.95);
        border-left: 6px solid #2563EB;
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 18px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .card-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.15);
    }

    /* Đổi màu viền cho các khung khác nhau */
    .card-1 { border-left-color: #EF4444; } /* Đỏ */
    .card-2 { border-left-color: #F59E0B; } /* Vàng Cam */
    .card-3 { border-left-color: #10B981; } /* Xanh Lá */
    .card-4 { border-left-color: #3B82F6; } /* Xanh Dương */
    .card-5 { border-left-color: #8B5CF6; } /* Tím */
    .card-6 { border-left-color: #EC4899; } /* Hồng */
    .card-7 { border-left-color: #14B8A6; } /* Xanh Ngọc */

    /* Tiêu đề mục */
    .section-header {
        font-weight: 700;
        font-size: 1.05rem;
        color: #1F2937;
        margin-bottom: 8px;
    }

    /* Nút bấm tạo prompt */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 12px 20px;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%);
        box-shadow: 0 6px 18px rgba(29, 78, 216, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. Tiêu đề ứng dụng
st.markdown("<h1 class='main-title'>🏔️ EDUPROMPT Y TÝ</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Trợ lý AI Đổi mới Sáng tạo: Tạo Prompt Thiết kế Infographic & Poster Giáo dục</p>", unsafe_allow_html=True)

# 4. Các mục nhập liệu dạng Khung Thẻ bo góc

# --- MỤC 1 ---
st.markdown("<div class='card-box card-1'><div class='section-header'>📌 1. Nội dung / Ý nghĩa Infographic hoặc Poster (*)</div>", unsafe_allow_html=True)
noi_dung = st.text_area(
    "Nhập chủ đề hoặc bài học cần truyền tải:",
    placeholder="Ví dụ: Vòng tuần hoàn của nước trong tự nhiên, Các hệ thức lượng trong tam giác, Quy trình rửa tay 6 bước...",
    label_visibility="collapsed"
)
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 2 ---
st.markdown("<div class='card-box card-2'><div class='section-header'>📐 2. Hình thức thể hiện (Layout)</div>", unsafe_allow_html=True)
hinh_thuc = st.selectbox(
    "Chọn cấu trúc hiển thị:",
    [
        "Sơ đồ tư duy (Mindmap)",
        "Dòng thời gian (Timeline / Cột mốc lịch sử)",
        "Quy trình / Sơ đồ vòng tròn (Cyclic Flowchart)",
        "Bảng So sánh / Sơ đồ Venn",
        "Tóm tắt kiến thức trọng tâm (Key Summary Sheet)",
        "Infographic liệt kê / Giới thiệu khái niệm",
        "Poster tuyên truyền / Thông điệp trực quan"
    ],
    label_visibility="collapsed"
)
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 3 ---
st.markdown("<div class='card-box card-3'><div class='section-header'>🖼️ 3. Kích thước / Tỷ lệ khung hình (Aspect Ratio)</div>", unsafe_allow_html=True)
kich_thuoc_dict = {
    "16:9 (Ngang - Slide bài giảng, Máy chiếu, TV, Youtube)": ("16:9", "16:9"),
    "9:16 (Dọc - Màn hình điện thoại, TikTok, Reels, Story)": ("9:16", "9:16"),
    "4:3 (Ngang chuẩn - Máy chiếu truyền thống)": ("4:3", "4:3"),
    "3:4 (Dọc chuẩn - Poster dán tường, tờ rơi)": ("3:4", "3:4"),
    "1:1 (Hình vuông - Đăng Zalo, Facebook, Avatar)": ("1:1", "1:1")
}
kich_thuoc_chon = st.selectbox("Chọn kích thước:", list(kich_thuoc_dict.keys()), label_visibility="collapsed")
ar_str, ar_param = kich_thuoc_dict[kich_thuoc_chon]
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 4 ---
st.markdown("<div class='card-box card-4'><div class='section-header'>🎨 4. Phong cách nghệ thuật (Art Style)</div>", unsafe_allow_html=True)
phong_cach_options = [
    "3D Claymation (Đắp nổi đất nặn ngộ nghĩnh, nổi bật)",
    "2D Vector phẳng, hiện đại, tối giản",
    "Trực quan hóa khoa học sinh động (Scientific visualization)",
    "Nghệ thuật Màu sáp / Màu nước học trò (Watercolor & Crayon)",
    "Truyện tranh Việt Nam tươi sáng (Vietnamese Comic style)",
    "Hiện đại & Công nghệ số (Digital Tech / Neon Theme)",
    "Khác (Tự nhập)"
]
phong_cach_chon = st.selectbox("Chọn phong cách vẽ:", phong_cach_options, label_visibility="collapsed")
if phong_cach_chon == "Khác (Tự nhập)":
    phong_cach = st.text_input("Nhập phong cách riêng của bạn:", "Chibi đáng yêu, nhiều màu sắc")
else:
    phong_cach = phong_cach_chon
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 5 ---
st.markdown("<div class='card-box card-5'><div class='section-header'>⛰️ 5. Dấu ấn Văn hóa / Vùng miền (Tùy chọn đặc sắc)</div>", unsafe_allow_html=True)
van_hoa_options = {
    "Mặc định (Trung tính, không yêu cầu vùng miền)": "",
    "Văn hóa & Cảnh quan Tây Bắc / Y Tý (Ruộng bậc thang, trang phục Mông/Hà Nhì, mây vờn núi, hoa tớ dày)": "incorporating Northwest Vietnam mountain culture, terraced rice fields, foggy Y Ty scenery, vibrant ethnic motifs",
    "Nông thôn Việt Nam gần gũi, mộc mạc (Lũy trúc, đồng quê, mái nhà tranh)": "featuring peaceful Vietnamese countryside elements, bamboo trees, rustic aesthetic",
    "Hiện đại, Toàn cầu & Công nghệ": "clean global modern aesthetic with subtle digital tech elements"
}
van_hoa_chon = st.selectbox("Chọn yếu tố văn hóa:", list(van_hoa_options.keys()), label_visibility="collapsed")
van_hoa_str = van_hoa_options[van_hoa_chon]
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 6 ---
st.markdown("<div class='card-box card-6'><div class='section-header'>✨ 6. Trạng thái & Sắc thái màu sắc (Mood & Tone)</div>", unsafe_allow_html=True)
trang_thai_options = [
    "Tươi sáng & Đáng yêu (Bright, cheerful & cute)",
    "Sinh động & Vui tươi (Vibrant & energetic)",
    "Nghiêm túc, Khoa học & Chuyên nghiệp (Professional & scientific)",
    "Ấm áp & Gần gũi (Warm, friendly & gentle)",
    "Khác (Tự nhập)"
]
trang_thai_chon = st.selectbox("Chọn tông màu & cảm xúc:", trang_thai_options, label_visibility="collapsed")
if trang_thai_chon == "Khác (Tự nhập)":
    trang_thai = st.text_input("Nhập trạng thái màu sắc riêng:", "Tông màu pastel nhẹ nhàng")
else:
    trang_thai = trang_thai_chon
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 7 ---
st.markdown("<div class='card-box card-7'><div class='section-header'>🎓 7. Độ tuổi & Khối lớp mục tiêu (Target Audience)</div>", unsafe_allow_html=True)
khoi_lop_dict = {
    "Mầm non / Tiền tiểu học (Hình ảnh cực to, ngộ nghĩnh, rất ít chữ)": "kindergarten pupils, extremely simple visuals, cute icons, bold lines",
    "Tiểu học: Lớp 1 (Trực quan, hình ảnh to, đơn giản)": "1st-grade primary students (aged 6), simple bright visual diagram",
    "Tiểu học: Lớp 2 (Nhiều hình ảnh, màu sắc tươi sáng)": "2nd-grade primary students (aged 7), engaging colorful visuals",
    "Tiểu học: Lớp 3 (Trực quan hóa sinh động)": "3rd-grade primary students (aged 8), clear visual hierarchy",
    "Tiểu học: Lớp 4 (Chi tiết, rõ ràng, giàu thông tin)": "4th-grade primary students (aged 9), informative educational chart",
    "Tiểu học: Lớp 5 (Chuẩn bị chuyển cấp, khoa học, bài bản)": "5th-grade primary students (aged 10), structured educational infographic",
    "THCS: Lớp 6 (Khởi đầu cấp 2, hiện đại, sinh động)": "6th-grade middle school students (aged 11), modern educational chart",
    "THCS: Lớp 7 (Khoa học, tư duy hình học / hệ thống)": "7th-grade middle school students (aged 12), structured academic graphic",
    "THCS: Lớp 8 (Chi tiết, chuẩn kiến thức phổ thông)": "8th-grade middle school students (aged 13), detailed scientific infographic",
    "THCS: Lớp 9 (Chuyên sâu, hiện đại, phục vụ ôn tập)": "9th-grade middle school students (aged 14), comprehensive study poster"
}
khoi_lop_chon = st.selectbox("Chọn khối lớp:", list(khoi_lop_dict.keys()), label_visibility="collapsed")
khoi_lop_en = khoi_lop_dict[khoi_lop_chon]
st.markdown("</div>", unsafe_allow_html=True)

# 5. Nút bấm tạo Prompt
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 XUẤT PROMPT TIẾNG ANH CHUYÊN NGHIỆP", type="primary"):
    if not noi_dung.strip():
        st.warning("⚠️ Vui lòng nhập nội dung chủ đề ở Mục 1!")
    else:
        # Xử lý ghép Prompt Tiếng Anh chuẩn AI vẽ ảnh
        cultural_tag = f", {van_hoa_str}" if van_hoa_str else ""
        
        prompt_en_final = (
            f"An educational {hinh_thuc} infographic poster about '{noi_dung}'. "
            f"Designed specifically for {khoi_lop_en}. "
            f"Art style: {phong_cach}, {trang_thai} mood, bright aesthetic educational color palette. "
            f"Clean layout, sharp vector graphics, highly intuitive layout, easy to understand{cultural_tag}, "
            f"high resolution, 8k quality --ar {ar_param}"
        )

        st.success("🎉 Tạo thành công! Dưới đây là Prompt Tiếng Anh chuẩn tối ưu cho các công cụ AI vẽ ảnh (Canva AI, Midjourney, Bing Image Creator, DALL-E 3):")
        
        # Hiển thị Prompt trong khung Code có nút Copy
        st.code(prompt_en_final, language="text")
        
        st.info("💡 **Mẹo sử dụng**: Bấm vào biểu tượng **Copy** ở góc trên bên phải khung chữ màu đen ở trên, sau đó dán (Paste) trực tiếp vào ô vẽ ảnh của Bing Image Creator / ChatGPT / Midjourney để tạo ảnh đẹp nhất!")

# Chân trang
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("✨ Mô hình Sáng kiến Chuyển đổi số & Đổi mới Sáng tạo Giáo dục - Xã Y Tý, 2026.")
