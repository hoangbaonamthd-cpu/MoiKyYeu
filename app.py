import streamlit as st
import base64

# Hàm xử lý âm thanh để sửa lỗi không phát nhạc
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
                audio.volume = 0.7;
                audio.play();
            </script>
            """
        st.markdown(md, unsafe_allow_html=True)

# Cấu hình trang sáng sủa
st.set_page_config(page_title="Thư Mời Kỷ Yếu - Hoàng Bảo Nam", layout="centered")

# Giao diện CSS màu sáng (Light Theme)
st.markdown("""
    <style>
    /* Nền sáng gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        color: #2c3e50;
    }
    
    /* Tiêu đề vàng gold */
    .title-gold {
        color: #b8860b;
        text-align: center;
        font-family: 'Times New Roman', serif;
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Ô nhập liệu */
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #b8860b;
    }
    
    /* Nút bấm vàng gold sáng */
    .stButton>button {
        background-color: #ffd700;
        color: #000000;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #b8860b;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Khung nội dung thiệp */
    .card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

if 'status' not in st.session_state:
    st.session_state.status = 'input'

if st.session_state.status == 'input':
    st.markdown("<h1 class='title-gold'>Special Invitation</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Chào mừng bạn đến với thư mời của Hoàng Bảo Nam</p>", unsafe_allow_html=True)
    
    name = st.text_input("Nhập tên người nhận:", placeholder="Ví dụ: Dương Thị Ngọc Chi")
    
    if st.button("MỞ THƯ MỜI ✉️"):
        if name:
            st.session_state.name = name
            st.session_state.status = 'card'
            st.rerun()
        else:
            st.warning("Nam cần biết tên bạn để gửi lời mời nhé!")

else:
    # Phát bài Như Một Người Dưng Remix từ file của Nam
    try:
        play_audio("nhac.mp3")
    except:
        st.error("Không tìm thấy file nhac.mp3. Bạn nhớ để file nhạc cùng thư mục nhé!")

    # Nội dung thiệp sáng màu
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #7f8c8d; font-size: 0.8rem; letter-spacing: 2px;'>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='title-gold' style='font-size: 2.5rem;'>THƯ MỜI KỶ YẾU</h1>", unsafe_allow_html=True)
    
    st.write(f"### Thân gửi bạn: **{st.session_state.name}**")
    
    st.markdown(f"""
    <div style="line-height: 1.8; font-size: 1.1rem;">
    Mình là: <b>Hoàng Bảo Nam</b>.<br>
    Học sinh lớp: <b>12 Lý trường THPT Chuyên Hưng Yên</b>.<br><br>
    Để kỉ niệm quãng thời gian học sinh đầy ý nghĩa, mình trân trọng mời bạn đến dự buổi lễ kỉ yếu của mình. 
    Sự hiện diện của bạn sẽ là niềm vui và vinh dự rất lớn đối với mình.<br><br>
    Rất mong được gặp bạn!<br>
    <p style="text-align: right; color: #95a5a6;"><i>Hưng Yên, ngày 11/01/2026</i></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Quay lại"):
        st.session_state.status = 'input'
        st.rerun()
