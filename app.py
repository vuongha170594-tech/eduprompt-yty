import streamlit as st

# 1. Cấu hình trang
st.set_page_config(
    page_title="EduPrompt Y Tý - Trợ lý Tạo Prompt Infographic",
    page_icon="🎨",
    layout="wide"
)

# 2. Trang trí Giao diện CSS Nâng cao
st.markdown("""
<style>
    /* Nền toàn trang web: Dải màu Gradient Chuyên nghiệp */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 40%, #0284C7 80%, #0D9488 100%);
        background-attachment: fixed;
    }

    /* Giới hạn độ rộng khối nội dung chính ở giữa */
    .main .block-container {
        max-width: 950px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* BỎ KHUNG 1: Dòng chữ Nổi Trực Tiếp trên Nền Gradient */
    .borderless-info-header {
        text-align: center;
        margin-bottom: 25px;
        padding: 10px;
    }

    .borderless-info-header .sub-title {
        color: #FDE047; /* Màu vàng tươi nổi bật trên nền xanh */
        font-size: 1.05rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
    }

    .borderless-info-header .author-title {
        color: #FFFFFF; /* Màu trắng sắc nét */
        font-size: 1.25rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.7);
    }

    /* KHUNG 2: Banner Tiêu đề EDUPROMPT Y TÝ */
    .header-banner {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFFBEB 100%);
        border-radius: 20px;
        padding: 25px 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 30px;
        border: 3px solid #F59E0B;
    }

    .header-banner h1 {
        color: #1E3A8A !important;
        font-weight: 900;
        font-size: 2.3rem;
        margin: 0;
    }
    
    .header-banner p {
        color: #059669;
        font-size: 1.15rem;
        margin-top: 8px;
        margin-bottom: 0;
        font-weight: 700;
    }

    /* Phong cách Khung Thẻ (Card) Cao Cấp */
    .card-box {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 22px 25px;
        margin-bottom: 22px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
        border: 2px solid #E2E8F0;
    }

    /* Tiêu đề từng mục */
    .section-header {
        font-weight: 800;
        font-size: 1.15rem;
        color: #FFFFFF;
        padding: 10px 16px;
        border-radius: 10px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    .sh-1 { background: linear-gradient(135deg, #EF4444, #DC2626); }
    .sh-2 { background: linear-gradient(135deg, #F59E0B, #D97706); }
    .sh-3 { background: linear-gradient(135deg, #10B981, #059669); }
    .sh-4 { background: linear-gradient(135deg, #3B82F6, #2563EB); }
    .sh-5 { background: linear-gradient(135deg, #8B5CF6, #7C3AED); }
    .sh-6 { background: linear-gradient(135deg, #EC4899, #DB2777); }
    .sh-7 { background: linear-gradient(135deg, #06B6D4, #0891B2); }

    /* Nút bấm Tạo Prompt rực rỡ */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #10B981 0%, #059669 50%, #047857 100%);
        color: white !important;
        font-weight: 900;
        font-size: 1.3rem;
        padding: 16px 25px;
        border-radius: 14px;
        border: 2px solid #F59E0B;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 30px rgba(16, 185, 129, 0.7);
    }

    /* Khung Hướng dẫn Copy Nổi Bật */
    .copy-instruction-box {
        background-color: #FEF3C7;
        border: 2px dashed #D97706;
        border-radius: 12px;
        padding: 12px 18px;
        margin-top: 15px;
        margin-bottom: 10px;
        color: #92400E;
        font-weight: 800;
        font-size: 1.05rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Khung Mẹo & Hướng dẫn Nổi bật Chữ Đậm Rõ */
    .tip-box {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 16px;
        padding: 24px;
        border: 3px solid #F59E0B;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-top: 25px;
    }
    
    .tip-box h3 {
        color: #B45309 !important;
        font-weight: 800;
        margin-top: 0;
        font-size: 1.3rem;
    }

    .tip-box ol {
        color: #1E293B !important;
        font-weight: 600;
        font-size: 1.05rem;
        line-height: 1.8;
    }

    .tip-box a {
        color: #0284C7 !important;
        font-weight: 700;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# 3. PHẦN THÔNG TIN TÁC GIẢ & SÁNG KIẾN (NỔI TRÊN NỀN - BỎ KHUNG)
st.markdown("""
<div class='borderless-info-header'>
    <div class='sub-title'>✨ Mô hình sáng kiến chuyển đổi số và đổi mới sáng tạo giáo dục xã Y Tý, 2026 ✨</div>
    <div class='author-title'>👩‍🏫 Ứng dụng của cô Vương Thị Hà - Giáo viên Trường PTNT TH&THCS Y TÝ 🏫</div>
</div>
""", unsafe_allow_html=True)

# 4. KHUNG BANNER TÊN ỨNG DỤNG EDUPROMPT Y TÝ
st.markdown("""
<div class='header-banner'>
    <h1>🏔️ EDUPROMPT Y TÝ</h1>
    <p>🎓 Trợ lý AI: Tạo Prompt Thiết kế Infographic & Poster Giáo dục Rực rỡ</p>
</div>
""", unsafe_allow_html=True)

# 5. Các Khung Nhập Liệu 1 đến 7

# --- MỤC 1 ---
st.markdown("<div class='card-box'><div class='section-header sh-1'>📌 1. Nội dung / Ý nghĩa Infographic hoặc Poster (*)</div>", unsafe_allow_html=True)
noi_dung = st.text_area(
    "Nhập nội dung bài học:",
    placeholder="Ví dụ: Vòng tuần hoàn của nước trong tự nhiên, Các hệ thức lượng trong tam giác, Quy trình rửa tay 6 bước...",
    label_visibility="collapsed"
)
st.markdown("</div>", unsafe_allow_html=True)

# --- MỤC 2 ---
st.markdown("<div class='card-box'><div class='section-header sh-2'>📐 2. Hình thức thể hiện (Layout)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box'><div class='section-header sh-3'>🖼️ 3. Kích thước / Tỷ lệ khung hình (Aspect Ratio)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box'><div class='section-header sh-4'>🎨 4. Phong cách nghệ thuật (Art Style)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box'><div class='section-header sh-5'>⛰️ 5. Dấu ấn Văn hóa / Vùng miền (Tùy chọn đặc sắc)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box'><div class='section-header sh-6'>✨ 6. Trạng thái & Sắc thái màu sắc (Mood & Tone)</div>", unsafe_allow_html=True)
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
st.markdown("<div class='card-box'><div class='section-header sh-7'>🎓 7. Độ tuổi & Khối lớp mục tiêu (Target Audience)</div>", unsafe_allow_html=True)
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
    "THCS: Lớp 9 (Chuyên sâu, hiện đại, phục vụ ôn tập)": "9th-grade middle school students (aged 14), comprehensive study poster",
    "Tuyên truyền cộng đồng / Mọi độ tuổi người dân (Dễ hiểu, trực quan, thân thiện)": "general public and local community, universal highly visual friendly design"
}
khoi_lop_chon = st.selectbox("Chọn khối lớp / đối tượng:", list(khoi_lop_dict.keys()), label_visibility="collapsed")
khoi_lop_en = khoi_lop_dict[khoi_lop_chon]
st.markdown("</div>", unsafe_allow_html=True)

# 6. Nút Bấm & Kết Quả Đầu Ra
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

        st.success("🎉 Tạo thành công! Dưới đây là Prompt Tiếng Anh chuẩn dành cho các AI vẽ ảnh:")
        
        # Hướng dẫn bấm Copy trực quan nổi bật
        st.markdown("""
        <div class='copy-instruction-box'>
            <span>📋 CÂU LỆNH ĐÃ SẴN SÀNG</span>
            <span>👉 BẤM VÀO BIỂU TƯỢNG Ở GÓC TRÊN BÊN PHẢI NẰM TRONG Ô ĐEN DƯỚI ĐÂY ĐỂ COPY LỆNH 👈</span>
        </div>
        """, unsafe_allow_html=True)

        # Hiển thị Prompt trong khung code
        st.code(prompt_en_final, language="text")

        # Khung Mẹo & Đường Link Nổi Bật Sắc Nét
        st.markdown("""
        <div class='tip-box'>
            <h3>💡 MẸO & HƯỚNG DẪN SỬ DỤNG LỆNH PROMPT</h3>
            <ol>
                <li><b>Sao chép câu lệnh</b>: Bấm vào biểu tượng <b>Copy</b> ở góc trên bên phải của ô màu xám đen chứa đoạn mã Tiếng Anh ở trên.</li>
                <li><b>Bấm vào các liên kết ứng dụng bên dưới để dán câu lệnh tạo ảnh:</b>
                    <ul>
                        <li><a href="https://chatgpt.com" target="_blank">🤖 ChatGPT (OpenAI)</a> - Trò chuyện và yêu cầu tạo ảnh Infographic trực tiếp.</li>
                        <li><a href="https://gemini.google.com" target="_blank">✨ Google Gemini</a> - Công cụ AI đa năng hỗ trợ vẽ ảnh giáo dục.</li>
                        <li><a href="https://www.canva.com" target="_blank">🎨 Canva AI (Magic Media)</a> - Dán prompt vào mục Tạo ảnh tự động của Canva.</li>
                        <li><a href="https://www.bing.com/images/create" target="_blank">🖼 Bing Image Creator</a> - Công cụ tạo ảnh DALL-E 3 hoàn toàn miễn phí.</li>
                        <li><a href="https://designer.microsoft.com" target="_blank">🎯 Microsoft Designer</a> - Thiết kế Poster & Infographic chuyên nghiệp.</li>
                    </ul>
                </li>
                <li><b>Mẹo nhỏ:</b> Cô có thể thử đổi lại các thông số ở Mục 2 (Hình thức) hoặc Mục 4 (Phong cách) để tạo ra nhiều phương án ảnh phong phú khác nhau!</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# Chân trang
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #F1F5F9; font-weight: 600;'>Ứng dụng hỗ trợ giảng dạy trực quan - Trường PTNT TH&THCS Y Tý</p>", unsafe_allow_html=True)
