import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from ultralytics import YOLO
import av
import queue

@st.cache_resource
def load_yolo():
    return YOLO("yolov8n.pt")

model = load_yolo()
result_queue = queue.Queue()

if "unique_ids" not in st.session_state:
    st.session_state.unique_ids = set()

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    results = model.track(
        img, 
        persist=True, 
        imgsz=480, 
        conf=0.3, 
        iou=0.5, 
        verbose=False
    )
    
    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.int().cpu().tolist()
        for obj_id in ids:
            if obj_id not in st.session_state.unique_ids:
                st.session_state.unique_ids.add(obj_id)
                result_queue.put(len(st.session_state.unique_ids))

    annotated_frame = results[0].plot()
    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

st.title("🛡️ AEGIS-VISION // LIVE HUD")

col1, col2 = st.columns([2, 1])

with col2:
    st.subheader("Tactical Data")
    metric_place = st.empty()
    metric_place.metric("Unique Objects", len(st.session_state.unique_ids))
    st.info("Accuracy: HIGH | Sensitivity: 0.3")

with col1:
    ctx = webrtc_streamer(
        key="aegis-vision",
        mode=WebRtcMode.SENDRECV,
        video_frame_callback=video_frame_callback,
        media_stream_constraints={"video": {"width": 640, "height": 480}, "audio": False},
        async_processing=True,
    )

if not ctx.state.playing:
    st.session_state.unique_ids = set()

while ctx.state.playing:
    try:
        new_count = result_queue.get(timeout=1)
        metric_place.metric("Unique Objects", new_count)
    except queue.Empty:
        pass