import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

def main():
    st.title('WebRTC live video stream example')

    # 使用 Google 的 STUN 服务器
    rtc_configuration = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    # 启动 WebRTC 视频流
    webrtc_ctx = webrtc_streamer(key="example", rtc_configuration=rtc_configuration)

    # 这里可以添加更多的 Streamlit 组件或逻辑处理
    if webrtc_ctx.video_receiver:
        st.write("Webcam is running.")
    else:
        st.write("Please start the webcam.")

if __name__ == "__main__":
    main()
