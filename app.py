import streamlit as st
import datetime
import time

# ==========================================
# PAGE CONFIGURATION & THEME SETUP
# ==========================================
st.set_page_config(
    page_title="MedAssist AI - Medical Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for SaaS Medical Theme (#2563EB, #10B981, #F8FAFC)
CUSTOM_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Container Background */
    .stApp {
        background-color: #F8FAFC;
        color: #1E293B;
    }

    /* Hide default Streamlit header & footer elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.02);
    }
    
    /* Top Header Styling */
    .header-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%);
        padding: 1.8rem 2.2rem;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.05);
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
    }

    .header-title-section {
        display: flex;
        flex-direction: column;
        gap: 0.2rem;
    }

    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }

    .header-subtitle {
        font-size: 0.95rem;
        color: #64748B;
        margin: 0;
        font-weight: 400;
    }

    .model-badge {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        padding: 0.45rem 0.9rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.25);
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }

    .model-badge-dot {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        display: inline-block;
    }

    /* Sidebar Logo & Elements */
    .sidebar-logo-card {
        text-align: center;
        padding: 1.2rem;
        background: #F8FAFC;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 1.5rem;
    }

    .sidebar-logo-icon {
        font-size: 2.5rem;
        margin-bottom: 0.3rem;
    }

    .sidebar-logo-text {
        font-size: 1.2rem;
        font-weight: 700;
        color: #2563EB;
    }

    .sidebar-section-header {
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748B;
        margin-top: 1.2rem;
        margin-bottom: 0.6rem;
    }

    .tech-chip {
        display: inline-block;
        background-color: #EFF6FF;
        color: #2563EB;
        font-size: 0.8rem;
        font-weight: 500;
        padding: 0.3rem 0.65rem;
        border-radius: 6px;
        margin: 0.2rem 0.1rem;
        border: 1px solid #BFDBFE;
    }

    .stat-card {
        background-color: #FFFFFF;
        padding: 0.8rem 1rem;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        margin-bottom: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .stat-label {
        font-size: 0.85rem;
        color: #64748B;
    }

    .stat-value {
        font-size: 0.95rem;
        font-weight: 700;
        color: #2563EB;
    }

    /* Welcome Banner & Cards */
    .welcome-container {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 2.5rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        margin-bottom: 2rem;
        text-align: center;
    }

    .welcome-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.4rem;
    }

    .welcome-subtitle {
        font-size: 1rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }

    .topics-pills {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 2rem;
    }

    .topic-pill {
        background-color: #F1F5F9;
        color: #475569;
        font-size: 0.85rem;
        font-weight: 500;
        padding: 0.35rem 0.8rem;
        border-radius: 20px;
        border: 1px solid #CBD5E1;
    }

    .suggestion-grid-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 1rem;
    }

    /* Custom Response Card */
    .response-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 1.4rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 0.8rem;
    }

    .medical-disclaimer {
        background-color: #FEF2F2;
        border-left: 4px solid #EF4444;
        color: #991B1B;
        padding: 0.65rem 1rem;
        border-radius: 6px;
        font-size: 0.82rem;
        font-weight: 500;
        margin-top: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Footer Styling */
    .app-footer {
        text-align: center;
        padding: 1.5rem 0;
        color: #94A3B8;
        font-size: 0.85rem;
        border-top: 1px solid #E2E8F0;
        margin-top: 3rem;
    }

    .app-footer span {
        font-weight: 600;
        color: #64748B;
    }

    /* Buttons styling override */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        font-weight: 500;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #2563EB;
        color: #2563EB;
        background-color: #EFF6FF;
    }
</style>
"""

# Inject custom styles
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==========================================
# BACKEND PLACEHOLDER FUNCTION
# ==========================================
def get_bot_response(question: str) -> str:
    """
    Placeholder function for backend integration.
    Will be replaced with LangChain RAG pipeline.
    """
    return (
        f"**Backend response placeholder** for query: *'{question}'*\n\n"
        "This function is ready to be connected to your **LangChain RAG chain** using Pinecone vector store "
        "and Gemini LLM. Currently running frontend simulation."
    )


# ==========================================
# HEADER RENDERER
# ==========================================
def render_header():
    """Renders the styled top header banner."""
    header_html = """
    <div class="header-container">
        <div class="header-title-section">
            <h1 class="header-title">🩺 MedAssist AI</h1>
            <p class="header-subtitle">AI-Powered Medical Assistant using Retrieval-Augmented Generation (RAG)</p>
        </div>
        <div class="model-badge">
            <span class="model-badge-dot"></span>
            Gemini 3.5 Flash Lite
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)


# ==========================================
# SIDEBAR RENDERER
# ==========================================
def render_sidebar():
    """Renders the interactive sidebar with about, stats, tech stack & prompt shortcuts."""
    with st.sidebar:
        # Project Logo & Title Card
        st.markdown(
            """
            <div class="sidebar-logo-card">
                <div class="sidebar-logo-icon">🩺</div>
                <div class="sidebar-logo-text">MedAssist AI</div>
                <small style="color: #64748B;">Trusted Clinical Knowledge Base</small>
            </div>
            """,
            unsafe_allow_html=True
        )

        # About Section
        st.markdown('<div class="sidebar-section-header">About</div>', unsafe_allow_html=True)
        st.info("This chatbot answers medical questions using trusted medical documents.")

        # Technologies Used
        st.markdown('<div class="sidebar-section-header">Technologies Used</div>', unsafe_allow_html=True)
        tech_stack = ["Gemini API", "LangChain", "Pinecone", "HuggingFace Embeddings", "Streamlit"]
        tech_html = "".join([f'<span class="tech-chip">{tech}</span>' for tech in tech_stack])
        st.markdown(f'<div>{tech_html}</div>', unsafe_allow_html=True)

        st.markdown("---")

        # Example Questions
        st.markdown('<div class="sidebar-section-header">Example Questions</div>', unsafe_allow_html=True)
        example_questions = [
            "What is Diabetes?",
            "Symptoms of Asthma",
            "What is Pneumonia?",
            "Causes of Hypertension",
            "Migraine Symptoms"
        ]

        for q in example_questions:
            if st.button(f"📌 {q}", key=f"side_btn_{q}", use_container_width=True):
                handle_user_query(q)

        st.markdown("---")

        # Controls & Clear Chat
        st.markdown('<div class="sidebar-section-header">Session Controls</div>', unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat", type="secondary", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        # Chat Statistics
        st.markdown('<div class="sidebar-section-header">Chat Statistics</div>', unsafe_allow_html=True)
        msg_count = len(st.session_state.get("messages", []))
        session_time = st.session_state.get("session_start_time", "Active")
        
        st.markdown(
            f"""
            <div class="stat-card">
                <span class="stat-label">Messages Sent</span>
                <span class="stat-value">{msg_count}</span>
            </div>
            <div class="stat-card">
                <span class="stat-label">Current Session</span>
                <span class="stat-value">{session_time}</span>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# WELCOME SCREEN RENDERER
# ==========================================
def render_welcome_screen():
    """Renders the initial welcome view before any question is asked."""
    st.markdown(
        """
        <div class="welcome-container">
            <div class="welcome-title">Welcome to MedAssist AI</div>
            <div class="welcome-subtitle">Your intelligent medical knowledge assistant.</div>
            
            <p style="font-weight: 500; color: #475569; margin-bottom: 0.6rem;">You can ask questions related to:</p>
            <div class="topics-pills">
                <span class="topic-pill">• Diseases</span>
                <span class="topic-pill">• Symptoms</span>
                <span class="topic-pill">• Medicines</span>
                <span class="topic-pill">• Medical Conditions</span>
                <span class="topic-pill">• Treatments</span>
                <span class="topic-pill">• Anatomy</span>
            </div>
            
            <div class="suggestion-grid-title">Or click a sample question to get started</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 4 Clickable Suggestion Cards
    col1, col2 = st.columns(2)

    suggestions = [
        (" What is Diabetes?", "Learn about types, symptoms, and blood sugar management."),
        (" Symptoms of Asthma", "Discover common warning signs and respiratory indicators."),
        (" What is Pneumonia?", "Understand lung infection causes, diagnostic tests, and care."),
        (" Causes of Hypertension", "Explore high blood pressure triggers and risk factors.")
    ]

    with col1:
        if st.button(suggestions[0][0], help=suggestions[0][1], use_container_width=True, key="welcome_card_1"):
            handle_user_query(suggestions[0][0].strip())
        if st.button(suggestions[2][0], help=suggestions[2][1], use_container_width=True, key="welcome_card_3"):
            handle_user_query(suggestions[2][0].strip())

    with col2:
        if st.button(suggestions[1][0], help=suggestions[1][1], use_container_width=True, key="welcome_card_2"):
            handle_user_query(suggestions[1][0].strip())
        if st.button(suggestions[3][0], help=suggestions[3][1], use_container_width=True, key="welcome_card_4"):
            handle_user_query(suggestions[3][0].strip())


# ==========================================
# MAIN CHAT AREA RENDERER
# ==========================================
def render_chat():
    """Renders the chat history and messages."""
    if not st.session_state.messages:
        render_welcome_screen()
        return

    # Render message history
    for idx, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(f"**{msg['content']}**")

        elif msg["role"] == "assistant":
            with st.chat_message("assistant", avatar="🩺"):
                # Styled Response Card
                st.markdown(
                    f"""
                    <div class="response-card">
                        {msg['content']}
                    </div>
                    <div class="medical-disclaimer">
                        <span>⚠️</span>
                        <span><strong>Educational purposes only.</strong> Consult a healthcare professional for diagnosis or treatment.</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Expandable Sources Section
                with st.expander("📚 Sources"):
                    st.caption("Source citations will appear here after backend integration.")


# ==========================================
# FOOTER RENDERER
# ==========================================
def render_footer():
    """Renders the footer at the bottom of the page."""
    st.markdown(
        """
        <div class="app-footer">
            Powered by <span>Gemini</span> • <span>LangChain</span> • <span>Pinecone</span> • <span>Streamlit</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# QUERY HANDLER HELPER
# ==========================================
def handle_user_query(user_text: str):
    """Adds user query to history and triggers backend response execution."""
    st.session_state.messages.append({"role": "user", "content": user_text})
    st.rerun()


# ==========================================
# MAIN APPLICATION ENTRYPOINT
# ==========================================
def main():
    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "session_start_time" not in st.session_state:
        st.session_state.session_start_time = datetime.datetime.now().strftime("%I:%M %p")

    # Render UI Layout
    render_header()
    render_sidebar()
    render_chat()

    # Process pending assistant response if last message is from user
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        user_query = st.session_state.messages[-1]["content"]
        
        with st.chat_message("assistant", avatar="🩺"):
            with st.spinner("Searching medical knowledge..."):
                time.sleep(0.6)  # Subtle realistic loading effect
                response_text = get_bot_response(user_query)
            
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            st.rerun()

    # User Chat Input
    if user_input := st.chat_input("Ask a medical question (e.g., What are the symptoms of Asthma?)..."):
        handle_user_query(user_input)

    render_footer()


if __name__ == "__main__":
    main()
