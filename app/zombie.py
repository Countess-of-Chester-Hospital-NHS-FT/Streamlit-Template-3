import streamlit as st

st.set_page_config(layout="wide", page_title="Laura's Zombie Services Inc.")

# Custom CSS for a more "official" yet eerie feel
st.markdown(
    """
    <style>
    .stApp {
        background-color: #222; /* Professional dark background */
        color: #ddd; /* Readable light text */
    }
    .st-header {
        background-color: #444;
        padding: 1rem;
        border-bottom: 2px solid #666;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #b3ff66; /* Toxic green for a professional zombie vibe */
    }
    .stButton>button {
        color: #fff;
        background-color: #558b2f; /* Olive green for "official" */
        border: 1px solid #33691e;
    }
    /* Target all labels */
    label {
        color: #ddd !important; /* Tomato red, change as needed */
    }
    .stTextInput>div>div>input {
        background-color: #333;
        color: #ddd;
    }
    .stTextArea>div>div>textarea {
        background-color: #333;
        color: #ddd;
    }
    .st-form label {
        color: #ddd; /* Readable form label text */
    }
    .zombie-caption {
        color: #ddd;  /* Aqua */
        font-size: 14px;
        text-align: left;
        margin-top: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load images

# --- Homepage ---
st.title("Laura's Zombie Services Inc. - Your Premier Post-Apocalyptic Solutions Provider")
st.markdown("**(We're not saying it's the end of the world, but it's definitely... inconvenient.)**")

st.header("☣️ Home - Navigating the Undead Landscape")
st.markdown(
    """
    Welcome to the official website of Laura's Zombie Services Inc.! In these trying times, you need a reliable partner to help you navigate the... *challenges*... presented by the recent surge in the re-animated population. 

    We offer a comprehensive range of services designed to keep you, your loved ones, and your valuable (non-brain) assets safe and secure. Browse our offerings below to see how we can assist you in this new reality.
    """
)
st.image("img/zombie_services.png", width=400)
#st.markdown('<div class="zombie-caption">Just another satisfied (and unbitten) client.</div>', unsafe_allow_html=True)

# --- About Us ---
st.header("🏢 About Laura's Zombie Services Inc.")
st.markdown(
    """
    Founded by the visionary (and remarkably resourceful) Laura, our company was established with a single mission: to provide practical and effective solutions in a world overrun by the undead. 

    We understand the unique needs of the post-apocalyptic survivor, from secure relocation to expert zombie wrangling. Our team comprises seasoned professionals (and a few surprisingly agile interns) dedicated to ensuring your safety and peace of mind.

    **Our Core Values:**
    * **Efficiency:** Getting the job done, even if it involves headshots.
    * **Discretion:** We understand the need for confidentiality in these sensitive times.
    * **Resourcefulness:** Making the most of what we've got (duct tape is our best friend).
    * **(Mostly) Ethical Practices:** We strive to handle all situations with the utmost care... for the living, at least.
    """
)
st.image("img/zombie2.png", width=400)

# --- Services ---
st.header("🛠️ Our Comprehensive Range of Services")
st.markdown(
    """
    We offer a variety of services to meet your post-apocalyptic needs:
    """
)

st.subheader("Secure Relocation Services")
st.write("Need to move to a safer zone? Our experienced drivers (with reinforced vehicles) can get you and your supplies to your destination, avoiding the heavily... *populated*... areas.")

st.subheader("Zombie Mitigation & Containment")
st.write("Dealing with a persistent undead problem? Our trained teams can assess the situation and implement effective mitigation strategies, from secure fencing to... more permanent solutions.")

st.subheader("Supply Procurement & Delivery")
st.write("Low on essential supplies? We can source and deliver non-perishable goods, medical equipment, and (if you're lucky) even that hard-to-find can of beans.")

st.subheader("Survivor Support & Training")
st.write("New to the apocalypse? Our survivor support program offers essential training in self-defense, scavenging, and basic first aid (for non-bite related injuries).")

st.image("img/zombie1.png", width=400)

# --- Contact Us ---
st.header("📞 Contact Laura's Zombie Services Inc.")
st.markdown(
    """
    Ready to take the first step towards a (slightly) safer future? Contact us today for a consultation and a free quote (terms and conditions apply, may vary based on zombie density in your area).
    """
)

contact_form = st.form("contact_form")
with contact_form:
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    enquiry = st.text_area("Your Enquiry:")
    submitted = st.form_submit_button("Send Enquiry")
    if submitted:
        st.success(f"Your enquiry has been received, {name}. We will respond as soon as it's safe to do so (and we haven't run out of coffee). In the meantime browse our pictures and stay vigilant.")

st.markdown("---")
st.markdown("**(Please note: Laura's Zombie Services Inc. is not responsible for any pre-existing zombie infections or sudden cravings for brains. We recommend maintaining a safe distance and double-checking all doors and windows.)**")