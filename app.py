import streamlit as st

# 1. Cấu hình trang (Mở rộng tràn màn hình rộng để hình nền tràn 2 bên)
st.set_page_config(
    page_title="EduPrompt Y Tý - Trợ lý Tạo Prompt Infographic",
    page_icon="🎨",
    layout="wide"
)

# 2. Trang trí Giao diện CSS Nâng cao: Nền Ruộng Bậc Thang Y Tý Rực Rỡ & Khung Gradient
st.markdown("""
<style>
    /* Nền toàn trang web: Cảnh sắc Ruộng Bậc Thang Y Tý tươi sáng, rực rỡ */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0.75)), 
                    url('https://images.unsplash.com/photo-1544644181-1484b3fdfc62?q=80&w=1920');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Giới hạn độ rộng khối nội dung chính ở giữa để dễ nhìn */
    .main .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Khung Tiêu đề Banner Hoành tráng */
    .header-banner {
        background: linear-gradient(135deg, #0284C7 0%, #0D9488 50%, #16A34A 100%);
        border-radius: 20px;
        padding: 25px 20px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 25px rgba(13, 148, 136, 0.3);
        margin-bottom: 25px;
    }
    
    .header-banner h1 {
        color: #FFFFFF !important;
        font-weight: 900;
        font-size: 2.2rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-banner p {
        color: #F0FDFA;
        font-size: 1.1rem;
        margin-top: 8px;
        margin-bottom: 0;
        font-weight: 500;
    }

    /* Phong cách Khung Thẻ (Card) Cao Cấp, Màu Sắc Nổi Bật */
    .card-box {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        border: 2px solid #E2E8F0;
        transition: all 0.3s ease;
    }

    .card-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.12);
    }

    /* Màu viền trái và icon cho từng mục */
    .card-1 { border-left: 8px solid #EF4444; } /* Đỏ tươi */
    .card-2 { border-left: 8px solid #F59E0B; } /* Cam vàng */
    .card-3 { border-left: 8px solid #10B981; } /* Xanh lá */
    .card-4 { border-left: 8px solid #3B82F6; } /* Xanh dương */
    .card-5 { border-left: 8px solid #8B5CF6; } /* Tím đậm */
    .card-6 { border-left: 8px solid #EC4899; } /* Hồng rực */
    .card-7 { border-left: 8px solid #06B6D4; } /* Xanh ngọc */

    /* Tiêu đề từng mục */
    .section-title {
        font-weight: 800;
        font-size: 1.15rem;
        color: #1E293B;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    /* Nút bấm Tạo Prompt rực rỡ */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #16A34A 0%, #0D9488 50%, #0284C7 100%);
        color: white !important;
        font-weight: 800;
        font-size: 1.25rem;
        padding: 15px 25px;
        border-radius: 14px;
        border: none;
        box-shadow: 0 8px 20px rgba(13, 148, 136, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 28px rgba(13, 148, 136, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. Banner Tiêu đề Đầu trang
st.markdown("""
<div class='header-banner'>
    <h1>🏔️ EDUPROMPT Y TÝ</h1>
    <p>🎓 Trợ lý AI Chuyển đổi Số: Tạo Prompt Thiết kế Infographic & Poster Giáo dục Rực rỡ</p>
</div>
""", unsafe_allow_html=True)

# 4. Các Khung Nhập Liệu

# --- MỤC 1 ---
st.markdown("<div class='card-box card-1'><div class='section-title'>📌 1. Nội dung / Ý nghĩa Infographic hoặc Poster (*)</div>", unsafe_allow_html=True)
noi_dung = st.text_area(
    "Nhập nội dung bài học:",
    placeholder="Ví dụ: Vòng tuần hoàn của nước trong tự nhiên, Các hệ thức lượng trong tam giác, Quy trình rửa tay 6 bước...",
    label_visibility="collapsed"
)
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 2 ---
st.markdown("<div class='card-box card-2'><div class='section-title'>📐 2. Hình thức thể hiện (Layout)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box card-3'><div class='section-title'>🖼️ 3. Kích thước / Tỷ lệ khung hình (Aspect Ratio)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box card-4'><div class='section-title'>🎨 4. Phong cách nghệ thuật (Art Style)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box card-5'><div class='section-title'>⛰️ 5. Dấu ấn Văn hóa / Vùng miền (Tùy chọn đặc sắc)</div>", unsafe_allow_html=True)
van_hoa_options = {
    "Mặc định (Trung tính, không yêu cầu vùng miền)": "",
    "Văn hóa & Cảnh quan Tây Bắc / Y Tý (Ruộng bậc thang vàng óng, trang phục Mông/Hà Nhì, mây vờn núi)": "incorporating Northwest Vietnam mountain culture, golden terraced rice fields, foggy Y Ty scenery, vibrant ethnic motifs",
    "Nông thôn Việt Nam gần gũi, mộc mạc (Lũy trúc, đồng quê, mái nhà tranh)": "featuring peaceful Vietnamese countryside elements, bamboo trees, rustic aesthetic",
    "Hiện đại, Toàn cầu & Công nghệ": "clean global modern aesthetic with subtle digital tech elements"
}
van_hoa_chon = st.selectbox("Chọn yếu tố văn hóa:", list(van_hoa_options.keys()), label_visibility="collapsed")
van_hoa_str = van_hoa_options[van_hoa_chon]
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 6 ---
st.markdown("<div class='card-box card-6'><div class='section-title'>✨ 6. Trạng thái & Sắc thái màu sắc (Mood & Tone)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box card-7'><div class='section-title'>🎓 7. Độ tuổi & Khối lớp mục tiêu (Target Audience)</div>", unsafe_allow_html=True)
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

# 5. Nút Bấm & Kết Quả Đầu Ra
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 XUẤT PROMPT TIẾNG ANH CHUYÊN NGHIỆP", type="primary"):
    if not noi_dung.strip():
        st.warning("⚠️ Vui lòng nhập nội dung chủ đề ở Mục 1!")
    else:
        cultural_tag = f", {van_hoa_str}" if van_hoa_str else ""
        
        prompt_en_final = (
            f"An educational {hinh_thuc} infographic poster about '{noi_dung}'. "
            f"Designed specifically for {khoi_lop_en}. "
            f"Art style: {phong_cach}, {trang_thai} mood, bright aesthetic educational color palette. "
            f"Clean layout, sharp vector graphics, highly intuitive layout, easy to understand{cultural_tag}, "
            f"high resolution, 8k quality --ar {ar_param}"
        )

        st.success("🎉 Tạo thành công! Dưới đây là Prompt Tiếng Anh chuẩn dành cho các AI vẽ ảnh (Canva AI, Midjourney, Bing Image Creator, DALL-E 3):")
        st.code(prompt_en_final, language="text")

# Chân trang
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'>✨ Mô hình Sáng kiến Chuyển đổi số & Đổi mới Sáng tạo Giáo dục - Xã Y Tý, 2026.</p>", unsafe_allow_html=True)
