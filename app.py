import streamlit as st
import base64

# 1. Hàm xử lý âm thanh (Giữ nguyên tên file của bạn)
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

# 2. Cấu hình trang và Hiệu ứng cánh hoa hồng rơi
st.set_page_config(page_title="Thư Mời Kỷ Yếu - Hoàng Bảo Nam", layout="centered")

st.markdown("""
    <style>
    /* Nền sáng hồng nhạt dịu dàng */
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #fef0f0 100%);
        overflow: hidden;
    }

    /* Hiệu ứng cánh hoa rơi */
    .petal {
        position: fixed; background-color: #ffc0cb; border-radius: 150% 0 150% 0;
        opacity: 0.6; z-index: 0; pointer-events: none; animation: fall linear infinite;
    }
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }

    /* Vị trí các cánh hoa */
    .p1 { left: 10%; width: 15px; height: 15px; animation-duration: 7s; }
    .p2 { left: 30%; width: 10px; height: 10px; animation-duration: 9s; animation-delay: 2s; }
    .p3 { left: 50%; width: 20px; height: 20px; animation-duration: 6s; animation-delay: 4s; }
    .p4 { left: 70%; width: 12px; height: 12px; animation-duration: 10s; }
    .p5 { left: 90%; width: 18px; height: 18px; animation-duration: 8s; animation-delay: 3s; }

    /* Khung thiệp trắng sáng */
    .card {
        background: rgba(255, 255, 255, 0.95);
        padding: 40px; border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        border: 1px solid #eee; position: relative; z-index: 1;
    }

    /* TIÊU ĐỀ CHÍNH MÀU ĐEN */
    .main-title {
        color: #000000; 
        text-align: center; 
        font-family: 'Times New Roman', serif;
        font-size: 2.8rem; 
        font-weight: bold; 
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    /* NỘI DUNG CHỮ MÀU ĐEN */
    .content-text {
        line-height: 1.8; 
        font-size: 1.15rem; 
        color: #000000; /* Đổi sang màu đen rõ nét */
    }

    .stButton>button {
        background-color: #333; color: white; border-radius: 10px;
        font-weight: bold; border: none; padding: 10px 30px; width: 100%;
    }
    .stButton>button:hover {
        background-color: #000; color: #ffd700;
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
    st.markdown("<h1 style='text-align:center; color:#000;'>GRADUATION</h1>", unsafe_allow_html=True)
    name = st.text_input("Gửi tới bạn:", placeholder="Nhập tên người nhận...")
    
    if st.button("MỞ THƯ MỜI ❤️"):
        if name:
            st.session_state.target_name = name
            st.session_state.step = 'card'
            st.rerun()
        else:
            st.warning("Bạn quên nhập tên rồi kìa!")

else:
    # Phát nhạc (Nam nhớ để file nhạc cùng thư mục nhé)
    try:
        play_audio("nhac.mp3")
    except:
        st.error("Không tìm thấy file nhac.mp3!")

    # Nội dung thiệp
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#db7093; font-weight:bold;'>2022 - 2026</p>", unsafe_allow_html=True)
    st.markdown("<div class='main-title'>THƯ MỜI KỶ YẾU</div>", unsafe_allow_html=True)
    
    st.write(f"### Thân gửi bạn: **{st.session_state.target_name}**")
    
    st.markdown(f"""
    <div class="content-text">
    Mình là: <b>Hoàng Bảo Nam</b>.<br>
    Học sinh lớp: <b>12 Lý, THPT Chuyên Hưng Yên</b>.<br><br>
    Thời gian trôi thật nhanh, thấm thoắt đã đến lúc chúng mình phải chia xa mái trường. 
    Để lưu giữ những kỷ niệm đẹp nhất của thời học sinh, mình trân trọng mời bạn đến dự buổi lễ kỷ yếu của mình.<br><br>
    Sự hiện diện của bạn là niềm vui rất lớn đối với mình!<br><br>
    <p style="text-align: right;">
        <i>Hưng Yên, ngày 11/01/2026</i><br>
        <b>Bạn của bạn: Bảo Nam</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Quay lại"):
        st.session_state.step = 'start'
        st.rerun()

