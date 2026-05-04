#    py -m streamlit run python_code.py

import streamlit as st
from scipy.io import loadmat
import numpy as np
import os
os.system("cls")
import time



# ..................................................................................



data = loadmat("clock_data.mat")
t = data["t"]

def get_7_segment_values(data,name):
    D = data[name]
    return [D[:,i] for i in range(0,7,1)]
    # a = [:,0] and g = [:,1] 

def seg(on):
        if on: # When segment value is 1 then bright red
            return "background:#ff2b2b; box-shadow:0 0 12px #ff2b2b;"
        else: # When segment value is 0 then grey color
            return "background:#2a0000;"
        
segment_positions = [

    # g 
    "top:60px;left:18px;width:34px;height:6px;",

    # f
    "top:6px;left:5px;width:6px;height:50px;",

    # e
    "bottom:6px;left:5px;width:6px;height:50px;",

    # d
    "bottom:5px;left:18px;width:34px;height:6px;",

    # c
    "bottom:6px;right:5px;width:6px;height:50px;",

    # b
    "top:6px;right:5px;width:6px;height:50px;",

    # a
    "top:5px;left:18px;width:34px;height:6px;"
]


def draw_digit(array, i):

    def get_style(on):
        return "background:#ff2b2b; box-shadow:0 0 12px #ff2b2b;" if on else "background:#2a0000;"

    inner_html = ""
    for seg_num in range(7):
        
        is_on = array[seg_num][i] 
        inner_html += f"""
        <div style="position:absolute; {segment_positions[seg_num]} border-radius:5px; {get_style(is_on)}"></div>
        """
    
    return f'<div style="position:relative;width:70px;height:130px;">{inner_html}</div>'

def display_clock(hour_tens, hour_ones, min_tens, min_ones, sec_tens, sec_ones):
    placeholder = st.empty()
    total_frames = len(sec_ones[0])

    for i in range(total_frames):
    
        full_html = f"""
        <div style="display:flex; justify-content:center; align-items:center; gap:15px; background:black; padding:20px; border-radius:10px;">
            {draw_digit(hour_tens, i)}
            {draw_digit(hour_ones, i)}
            <div style="font-size:90px; color:#ff2b2b; line-height:220px;">:</div>
            {draw_digit(min_tens, i)}
            {draw_digit(min_ones, i)}
            <div style="font-size:90px; color:#ff2b2b; line-height:220px;">:</div>
            {draw_digit(sec_tens, i)}
            {draw_digit(sec_ones, i)}
        </div>
        """
        placeholder.markdown(full_html, unsafe_allow_html=True)
        time.sleep(10e-5) 


# ..................................................................................


st.sidebar.header("DIGITAL CLOCK")
st.sidebar.write("---")
option = st.sidebar.radio(label = "",
    options = ["HOME","ABOUT APP",
               "SUMMARY"])

st.sidebar.write("---")
st.sidebar.write("~ SAMRAT MALLA")

if option == "HOME":

    st.header("DIGITAL CLOCK")

    st.write("---")

    choice = st.radio(label = "SELECT YOUR CHOICE",
                    options = ["START CLOCK","STOP CLOCK"],
                    index =  1)

    st.write("---")

    if choice == "START CLOCK" :

        clock_space = st.container()

        st.write("<br>",unsafe_allow_html=True)
        st.write("---")

        st.write("By | Samrat Malla")




























        ones_array_seconds = get_7_segment_values(data,"So")
        tens_array_seconds = get_7_segment_values(data,"St")

        ones_array_minutes = get_7_segment_values(data,"Mo")
        tens_array_minutes = get_7_segment_values(data,"Mt")

        ones_array_hours = get_7_segment_values(data,"Ho")
        tens_array_hours = get_7_segment_values(data,"Ht")

        with clock_space:

            display_clock(tens_array_hours,ones_array_hours,
                tens_array_minutes,ones_array_minutes,
                tens_array_seconds,ones_array_seconds)



# ..................................................................................




if option == "ABOUT APP":


    st.write("""
        <h1>About App</h1>

""",unsafe_allow_html = True)
    
    st.write("---")



    st.write("""
        

<h5>
             
- This application is a real-time digital clock visualization
system built by coupling Simulink-based digital logic simulation with 
a Python + Streamlit rendering engine.
<br><br>
             
- At its core, the system is not just a UI clock — it is a full digital 
electronics pipeline simulation, where time is generated, processed, and visualized 
across two engineering domains.
</h5>
            

""",unsafe_allow_html = True)
    
    st.write("---")
    





    st.write("""


<h2>⚙️ System Architecture Detail </h2><br><br>
<h3>
🔌 1. Signal Generation (Simulink Side) </h3>
             <h5>

- The time base is derived from a 50 Hz clock signal, representing a 
             hardware-like system clock.
<br>To convert this into human-readable time:
- The 50 Hz signal is scaled and processed into a 1-second time base.<br>
- A hierarchy of mod counters (MOD-10, MOD-6, MOD-60 logic) is implemented
Cascaded counters generate:
Seconds 
Minutes 
Hours 

Each stage uses:<br>
Enable-trigger cascading
Reset logic propagation
Zero-order hold for stable discrete outputs""",unsafe_allow_html=True)
    
    st.write("---")
             
    st.write("""

<h3>🔢 2. Digital Encoding Layer</h3><h5>

The Simulink model outputs:

- Binary-coded signals
- Segment activation vectors (a–g for 7-segment display)
- Decoded decimal values for each digit stage

These are exported using MATLAB .mat files for Python integration.""",
unsafe_allow_html=True)


    st.write("---")


    st.write("""
         <h3>
             🧩 3. Python Processing Layer </h3>
<h5>
In Python:<br>
         
- Binary signals are reconstructed into decimal values
         
- Segment activation arrays are parsed for:
    - Tens digit display
    - Ones digit display
         
- Data is synchronized with simulation time vector ' t '<br>

This acts as a hardware-to-software interface layer, 
         mimicking embedded system data acquisition.""",unsafe_allow_html=True)


    st.write("---")

    st.write("""

<h3>🎨 4. Visualization Engine (Streamlit UI)</h3>
             <h5>

The final stage is a real-time 7-segment display emulator built using:

- HTML + inline CSS rendering
- Streamlit dynamic update loop
- Segment-wise LED simulation using boolean activation

Each digit is rendered as a virtual 7-segment LED module, where:
             
1 → glowing red segment

0 → inactive dark segment<br>

The result is a hardware-accurate visual representation of a digital counter system.
             """,unsafe_allow_html=True)
    
    st.write("---")

    st.write("""

<h3>🚀 Key Engineering Highlights</h3><h5>
             
- Real-time simulation-to-UI pipeline
- Multi-domain integration (MATLAB + Simulink + Python + Web UI)
- Digital logic design implemented using cascaded modular counters
Embedded-system-like architecture using software tools
- Custom 7-segment display rendering engine

        """,unsafe_allow_html=True)
    
    st.write("---")

    st.write("By | Samrat Malla")

    
if option == "SUMMARY":





    st.write("""
<h1>🔥 Summary""",unsafe_allow_html=True)
    st.write("---")
    st.write("""
<h5>
             
- This project demonstrates how a simple concept — a clock — becomes a full 
             digital systems pipeline

- WORKFLOW : Signal processing → digital logic design → software decoding → real-time visualization

- It is a bridge between theoretical electronics and modern software
              visualization systems.
             """,unsafe_allow_html=True)
    
    st.write("---")

    st.write("By | Samrat Malla")
 

# ..................................................................................
