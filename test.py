import streamlit as st

# WebRTC HTML and JavaScript code for live video stream
webrtc_html = """
<video id="video" width="100%" height="auto" autoplay></video>
<script>
    // Check if the browser supports WebRTC
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Get user media (video)
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            // Get the video element and set the stream as the source
            var video = document.getElementById('video');
            video.srcObject = stream;
        })
        .catch(function(error) {
            console.log("Error accessing media devices.", error);
            alert("Failed to access the webcam. Please check permissions.");
        });
    } else {
        alert("WebRTC not supported by this browser.");
    }
</script>
"""

# Display the WebRTC stream in Streamlit using unsafe HTML
st.markdown(webrtc_html, unsafe_allow_html=True)