import streamlit as st
import base64

# 1. Hàm xử lý âm thanh
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio id="myAudio" autoplay="true" loop="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <script>
                var audio = document.getElementById("myAudio");
                audio.play();
            </script>
            """
        st.markdown(md, unsafe_allow_html=True)

# 2. Cấu hình trang và Hiệu ứng cánh hoa rơi
st.set_page_config(page_title="Thư Mời Kỷ Yếu - Hoàng Bảo Nam", layout="centered")

st.markdown("""
    <style>
    /* Nền sáng hồng nhạt dịu dàng */
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #fef0f0 100%);
        overflow: hidden;
    }

    /* Hiệu ứng cánh hoa rơi (Petals falling) */
    .petal {
        position: fixed; background-color: #ffc0cb; border-radius: 150% 0 150% 0;
        opacity: 0.7; z-index: 0; pointer-events: none; animation: fall linear infinite;
    }
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }

    /* Tạo nhiều cánh hoa với vị trí và tốc độ khác nhau */
    .p1 { left: 10%; width: 15px; height: 15px; animation-duration: 7s; animation-delay: 0s; }
    .p2 { left: 30%; width: 10px; height: 10px; animation-duration: 9s; animation-delay: 2s; }
    .p3 { left: 50%; width: 20px; height: 20px; animation-duration: 6s; animation-delay: 4s; }
    .p4 { left: 70%; width: 12px; height: 12px; animation-duration: 10s; animation-delay: 1s; }
    .p5 { left: 90%; width: 18px; height: 18px; animation-duration: 8s; animation-delay: 3s; }

    /* Nội dung thiệp */
    .card {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px; border-radius: 25px;
        box-shadow: 0 10px 40px rgba(255, 182, 193, 0.3);
        border: 2px solid #ffe4e1; position: relative; z-index: 1;
    }
    .title-gold {
        color: #d4af37; text-align: center; font-family: 'Times New Roman', serif;
        font-size: 3rem; font-weight: bold; margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #ffb6c1; color: white; border-radius: 20px;
        font-weight: bold; border: none; padding: 10px 30px; width: 100%;
    }
    </style>
    
    <div class="petal p1"></div><div class="petal p2"></div>
    <div class="petal p3"></div><div class="petal p4"></div>
    <div class="petal p5"></div>
    """, unsafe_allow_html=True)

# 3. Logic điều hướng
if 'step' not in st.session_state:
    st.session_state.step = 'start'

if st.session_state.step == 'start':
    st.markdown("<h1 class='title-gold'>The Invitation</h1>", unsafe_allow_html=True)
    name = st.text_input("Gửi tới người bạn đặc biệt:", placeholder="Nhập tên người nhận...")
    
    if st.button("MỞ THƯ MỜI"):
        if name:
            st.session_state.target_name = name
            st.session_state.step = 'card'
            st.rerun()
        else:
            st.warning("Vui lòng cho Nam biết tên bạn nhé!")

else:
    # Phát nhạc (file nhac.mp3 cùng thư mục)
    try:
        play_audio("nhac.mp3")
    except:
        st.error("Thiếu file nhac.mp3 trong thư mục!")

    # Nội dung thiệp
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#db7093; letter-spacing:3px;'>KỶ NIỆM TUỔI HỌC TRÒ</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='title-gold' style='font-size:2.2rem;'>THƯ MỜI KỶ YẾU</h1>", unsafe_allow_html=True)
    
    st.write(f"### Thân gửi bạn: **{st.session_state.target_name}**")
    
    st.markdown(f"""
    <div style="line-height: 2; font-size: 1.15rem; color: #555;">
    Mình là: <b>Hoàng Bảo Nam</b>.<br>
    Học sinh lớp: <b>12 Lý, THPT Chuyên Hưng Yên</b>.<br><br>
    Những ngày cuối cấp đang dần trôi qua, mình rất muốn bạn có mặt trong buổi lễ kỷ yếu này để cùng nhau lưu giữ những tấm hình đẹp nhất.<br><br>
    Sự hiện diện của bạn là niềm hạnh phúc lớn nhất đối với mình!<br>
    <p style="text-align: right; color: #db7093; margin-top: 20px;">
        <i>Hưng Yên, ngày 11/01/2026</i><br>
        <b>Ký tên: Bảo Nam</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Quay lại"):
        st.session_state.step = 'start'
        st.rerun()


