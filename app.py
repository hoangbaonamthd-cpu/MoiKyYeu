import streamlit as st
import base64

# Hàm để nhúng nhạc vào giao diện
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Giao diện thiệp
st.set_page_config(page_title="Thư Mời Kỷ Yếu - Hoàng Bảo Nam", layout="centered")

# CSS để tạo màu Đen & Vàng kim
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1 { color: #ffd700; text-align: center; font-family: 'Times New Roman'; }
    .content { font-size: 1.2rem; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    st.markdown("<h1>GRADUATION INVITE</h1>", unsafe_allow_html=True)
    name = st.text_input("Nhập tên người nhận:", placeholder="Ví dụ: Dương Thị Ngọc Chi")
    if st.button("MỞ THƯ MỜI ✉️"):
        if name:
            st.session_state.name = name
            st.session_state.clicked = True
            st.rerun()
else:
    # Khi nhấn nút, nhạc sẽ phát và hiện thiệp
    play_audio("nhac.mp3")
    st.markdown(f"<h1>THƯ MỜI KỶ YẾU</h1>", unsafe_allow_html=True)
    st.write(f"### Kính gửi bạn: **{st.session_state.name}**")
    st.markdown(f"""
    <div class="content">
    Tôi tên là: <b>Hoàng Bảo Nam</b>.<br>
    Tôi là học sinh lớp 12 Lý trường THPT Chuyên Hưng Yên.<br><br>
    Tôi làm thiệp này để kính mời bạn đến dự lễ kỉ yếu của tôi. 
    Sự hiện diện của bạn sẽ là niềm vui lớn đối với tôi.<br><br>
    Rất mong bạn có thể tham gia. Tôi xin chân thành cảm ơn!
    </div>
    """, unsafe_allow_html=True)