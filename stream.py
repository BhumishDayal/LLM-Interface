import streamlit as st

# ---------- Page Setup ----------
st.set_page_config(page_title="Graph Enhancement", layout="wide")

# ---------- Remove default top padding & style ----------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
    }
    textarea {
        font-family: monospace;
        font-size: 14px;
    }
    .stButton>button {
        width: 100%;
        height: 3rem;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Title ----------
st.title("Graph Enhancement - Task 206")

# ---------- Row 1: Buttons + Search ----------
row1_col1, row1_col2, row1_col3, row1_col4 = st.columns([0.5, 0.5, 0.5, 3.0])

with row1_col1:
    if st.button("💾 Save"):
        st.success("Edges saved!")  
with row1_col2:
    if st.button("⬅️ Prev"):
        st.info("Previous task loaded")  
with row1_col3:
    if st.button("➡️ Next"):
        st.info("Next task loaded")  
with row1_col4:
    search_query = st.text_input("Search Nodes (format: '11D' or keyword):", "")

# ---------- Row 2: Meme + Input + Nodes ----------
row2_col1, row2_col2, row2_col3, row2_col4 = st.columns([1.3, 0.6, 1.2, 1.2])

# Meme
with row2_col1:
    st.subheader("Meme")
    st.image("image.png", caption="Input Image", use_container_width=True)

# Edges Input
with row2_col2:
    st.subheader("Edges Input")
    edges = st.text_area(
        "Enter edges (format: '1 2' or 'T 1 3'):",
        height=550,
        label_visibility="collapsed"
    )

# Nodes data
nodes_list = [
    "[0E] The image shows Brett Kavanaugh smiling and wearing a judicial robe.",
    "[1E] The text overlay reads: 'Well hi there Kamala, it's been a little while.'",
    "[2B] Brett Kavanaugh is an Associate Justice of the Supreme Court of the United States.",
    "[3B] Kamala Harris is the current Vice President of the United States.",
    "[4B] Kavanaugh and Harris had a high-profile and contentious interaction...",
    "[5B] A Supreme Court Justice position is a powerful, lifetime appointment.",
    "[6B] The phrase 'it's been a little while' implies passage of time...",
    "[7B] Judicial robes are the official attire for judges.",
    "[8B] A smiling expression can convey triumph, smugness, or 'last laugh.'",
    "[9D] The person in the image is identifiable as Brett Kavanaugh.",
    "[10D] Kavanaugh is depicted in his official capacity as a judge/Justice.",
    "[11D] The caption is directed at Kamala Harris, referencing a past interaction.",
    "[12D] Despite opposition, Kavanaugh secured a lifetime Supreme Court seat.",
    "[13D] His smile + caption suggest smugness or 'had the last laugh.'",
    "[14D] Kamala Harris has risen to Vice President.",
    "[15D] The meme highlights contrasting career trajectories.",
    "[16D] The meme underscores sarcasm, irony, and political payback."
]

# Filter nodes by search
filtered_nodes = [n for n in nodes_list if search_query.lower() in n.lower()] if search_query else nodes_list
midpoint = len(filtered_nodes) // 2
nodes_left = filtered_nodes[:midpoint]
nodes_right = filtered_nodes[midpoint:]

# Nodes
with row2_col3:
    st.subheader("Nodes")
    st.text_area("Nodes Left", "\n\n".join(nodes_left), height=550, label_visibility="collapsed")

with row2_col4:
    st.subheader("")  # avoid duplicate heading
    st.text_area("Nodes Right", "\n\n".join(nodes_right), height=550, label_visibility="collapsed")

# ---------- Row 3: Graph + Errors ----------
row3_col1, row3_col2 = st.columns([2.0, 2.0])

with row3_col1:
    st.subheader("Graph")
    st.image("graph.png", use_container_width=True)
    st.markdown(
        """
        <style>
        [data-testid="stImage"] img {
            max-height: 1000px;  
            max-width: 100%;     
            object-fit: contain; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

with row3_col2:
    st.subheader("Errors")
    st.markdown("#### Structural Errors")
    st.error("""
- The graph must have exactly one conclusion node (currently 2 found).
- Skip edge detected: edge 1→13 is skipping the path 1 to 13.
    """)
    st.markdown("#### Semantic Errors")
    st.warning("These will be checked against the rubric later.")
