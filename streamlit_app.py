import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
import base64

# 在 Streamlit 侧边栏添加新的选项
options = st.sidebar.radio('Options:', ('Webcam', 'Browser Webcam', 'Image', 'Video', 'RTSP'), index=1)

# 处理来自浏览器的摄像头数据
if options == 'Browser Webcam':
    # HTML/JavaScript 代码用于访问和显示摄像头，并发送帧到Python端
    HTML = """
    <div>
        <video id='video' width='640' height='480' autoplay></video>
        <button id='capture'>Capture</button>
        <script>
            var video = document.getElementById('video');
            var capture = document.getElementById('capture');

            capture.onclick = function() {
                var canvas = document.createElement('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
                var imageData = canvas.toDataURL('image/jpeg').split(',')[1];
                google.colab.kernel.invokeFunction('notebook.Invoker', [imageData], {});
            };

            if (navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ video: true })
                    .then(function (stream) {
                        video.srcObject = stream;
                    })
                    .catch(function (error) {
                        console.error('Error accessing the camera.', error);
                    });
            } else {
                alert('getUserMedia not supported by your browser!');
            }
        </script>
    </div>
    """
    components.html(HTML, height=520)

    # 接收Base64图像数据
    image_data = st.text_input("Paste the Base64 Image data here")
    if image_data:
        # Base64解码并转换为OpenCV图像
        img_data = base64.b64decode(image_data)
        nparr = np.fromstring(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # 这里可以进行图像处理
        if st.button("Analyze Image"):
            # 假设有一个处理函数process_image来处理图像
            st.image(img, channels="BGR", caption="Processed Image")
