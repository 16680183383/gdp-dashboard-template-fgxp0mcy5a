import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

def main():
    st.title("WebRTC Example")

    webrtc_ctx = webrtc_streamer(key="example")
    if webrtc_ctx.video_receiver:
        while True:
            frame = webrtc_ctx.video_receiver.get_frame()
            if frame is not None:
                # Process the frame if needed
                processed_frame = frame.to_ndarray(format="bgr24")
                st.image(processed_frame, channels="BGR")

if __name__ == "__main__":
    main()
