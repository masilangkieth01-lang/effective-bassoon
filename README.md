 AEGIS-VISION // INTEGRATED TRACKING SYSTEM

Aegis-Vision is a high-performance, real-time object detection and tracking application built with **Streamlit** and **YOLOv8**. Designed with a high-tech, cyberpunk-inspired HUD, this system utilizes unique ID tracking to ensure objects are counted once and never duplicated within a session.

---

 *Key Features*

*   *Unique ID Tracking*: Uses the YOLOv8 tracking system to assign persistent IDs to objects.
*   *Zero-Duplicate Counter*: A session-state managed "Set" ensures the count only increments for new unique objects.
*   *Performance Optimized*: Pre-configured with asynchronous processing and optimized image resolution to minimize CPU lag.
*   *Auto-Reset Logic*: Tactical memory automatically clears when the camera stream is disconnected or stopped.
*   *High-Accuracy Mode*: Tuned sensitivity and enhanced processing size for precise target identification.

---

*Prerequisites*

Before launching the HUD, ensure you have the following dependencies installed:
```bash
pip install streamlit streamlit-webrtc ultralytics av
