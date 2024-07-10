import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2

def main():
    st.title("WebRTC Example")

    webrtc_ctx = webrtc_streamer(key="example")
    if webrtc_ctx.video_receiver:
        while True:
            frame = webrtc_ctx.video_receiver.get_frame()
            if frame is not None:
                img = frame.to_ndarray(format="bgr24")
                st.image(img, channels="BGR")

if __name__ == "__main__":
    main()
