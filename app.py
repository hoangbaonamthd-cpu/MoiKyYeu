import streamlit as st
import base64

# 1. Hàm xử lý âm thanh (Nam nhớ để file nhạc cùng thư mục và đặt tên nhac.mp3)
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

# 2. Cấu hình trang và Hiệu ứng cánh hoa + Chữ hiện từ từ
st.set_page_config(page_title="Thư Mời Kỷ Yếu - Hoàng Bảo Nam", layout="centered")

st.markdown("""
    <style>
    /* Nền sáng hồng nhạt */
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
    .p1 { left: 10%; width: 15px; height: 15px; animation-duration: 7s; }
    .p2 { left: 30%; width: 10px; height: 10px; animation-duration: 9s; animation-delay: 2s; }
    .p3 { left: 50%; width: 20px; height: 20px; animation-duration: 6s; animation-delay: 4s; }
    .p4 { left: 70%; width: 12px; height: 12px; animation-duration: 10s; }
    .p5 { left: 90%; width: 18px; height: 18px; animation-duration: 8s; animation-delay: 3s; }

    /* HIỆU ỨNG CHỮ HIỆN TỪ TỪ */
    .fade-in {
        animation: fadeIn ease 3s;
        -webkit-animation: fadeIn ease 3s;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform: translateY(20px);}
        100% {opacity:1; transform: translateY(0);}
    }

    /* Khung thiệp */
    .card {
        background: rgba(255, 255, 255, 0.95);
        padding: 40px; border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        border: 1px solid #eee; position: relative; z-index: 1;
    }

    .main-title {
        color: #000000; 
        text-align: center; 
        font-family: 'Times New Roman', serif;
        font-size: 2.8rem; 
        font-weight: bold; 
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    .content-text {
        line-height: 1.8; 
        font-size: 1.15rem; 
        color: #000000;
    }

    .stButton>button {
        background-color: #333; color: white; border-radius: 10px;
        font-weight: bold; border: none; padding: 10px 30px; width: 100%;
    }
    </style>
    
    <div class="petal p1"></div><div class="petal p2"></div>
    <div class="petal p3"></div><div class="petal p4"></div>
    <div class="petal p5"></div>
    """, unsafe_allow_html=True)

# 3. Điều hướng
if 'step' not in st.session_state:
    st.session_state.step = 'start'

if st.session_state.step == 'start':
    st.markdown("<h1 style='text-align:center; color:#000;'>GRADUATION</h1>", unsafe_allow_html=True)
    name = st.text_input("Gửi tới bạn:", placeholder="Nhập tên người nhận...")
    
    if st.button("MỞ THƯ MỜI"):
        if name:
            st.session_state.target_name = name
            st.session_state.step = 'card'
            st.rerun()
        else:
            st.warning("Bạn hãy nhập tên người nhận trước nhé!")

else:
    # Phát nhạc
    try:
        play_audio("nhac.mp3")
    except:
        st.error("Lưu ý: Nam cần để file nhạc tên 'nhac.mp3' cùng thư mục với file code này.")

    # Nội dung thiệp với class 'fade-in'
    st.markdown(f"""
    <div class='card fade-in'>
        <p style='text-align:center; color:#db7093; font-weight:bold;'>LƯU GIỮ KỶ NIỆM</p>
        <div class='main-title'>THƯ MỜI KỶ YẾU</div>
        <div class="content-text">
            <br>
            <h3>Thân gửi bạn: <b>{st.session_state.target_name}</b></h3>
            Mình là: <b>Hoàng Bảo Nam</b>.<br>
            Học sinh lớp: <b>12 Lý, THPT Chuyên Hưng Yên</b>.<br><br>
            Thời gian trôi thật nhanh, thấm thoắt đã đến lúc chúng mình phải tạm biệt tuổi học trò. 
            Để lưu giữ những khoảnh khắc đẹp nhất, mình trân trọng mời bạn đến dự buổi lễ kỷ yếu của mình.<br><br>
            Sự hiện diện của bạn là món quà ý nghĩa nhất đối với mình!<br><br>
            <p style="text-align: right;">
                <i>Hưng Yên,10h30 ngày 11/01/2026</i><br>
                <b>Ký Tên: Bảo Nam</b>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Quay lại"):
        st.session_state.step = 'start'
        st.rerun()



