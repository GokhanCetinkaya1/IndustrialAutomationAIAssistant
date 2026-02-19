import streamlit as st
from anthropic import Anthropic
from openai import OpenAI
from google import genai
import os
from dotenv import load_dotenv
from prompts.plc_prompts import get_plc_system_prompt
from prompts.robot_prompts import get_robot_system_prompt
from prompts.nc_prompts import get_nc_system_prompt
from utils.code_formatter import format_code_output

# .env dosyasından API key'i yükle
load_dotenv()

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="INDUSTRIAL AUTOMATION AI ASSISTANT",
    page_icon="🤖",
    layout="wide"
)

# Session state başlatma
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_platform' not in st.session_state:
    st.session_state.current_platform = "PLC"
if 'current_language' not in st.session_state:
    st.session_state.current_language = "ST"

# Başlık ve açıklama
st.title("🏭 INDUSTRIAL AUTOMATION AI ASSISTANT")
st.markdown("*AI-Assisted Code Generator for PLC and Robot Programming by Gökhan ÇETİNKAYA*")

# Sidebar - Ayarlar
with st.sidebar:

    #st.markdown("## for ICS/OT ")
    st.markdown("<h2 style='font-size: 24px; font-weight: bold; color: #1f77b4;'>for ICS/OT</h2>", unsafe_allow_html=True)
    st.divider()

    st.header("⚙️ Settings")
    
    # AI Provider Seçimi
    ai_provider = st.radio(
        "AI Provider:",
        ["Google Gemini", "DeepSeek", "Anthropic Claude", "OpenAI GPT"],
    )
    
    # API Key girişi
    if ai_provider == "Google Gemini":
        default_key = os.getenv("GOOGLE_API_KEY", "")
        api_key = st.text_input(
            "Google Gemini API Key",
            value=default_key,
            type="password",
            help="ÜCRETSIZ! https://aistudio.google.com/app/apikey adresinden alın"
        )
    elif ai_provider == "DeepSeek":
        default_key = os.getenv("DEEPSEEK_API_KEY", "")
        api_key = st.text_input(
            "DeepSeek API Key",
            value=default_key,
            type="password",
            help="API key'inizi https://platform.deepseek.com adresinden alabilirsiniz"
        )
    elif ai_provider == "Anthropic Claude":
        default_key = os.getenv("ANTHROPIC_API_KEY", "")
        api_key = st.text_input(
            "Anthropic API Key",
            value=default_key,
            type="password",
            help="API key'inizi https://console.anthropic.com adresinden alabilirsiniz"
        )
    else:  # OpenAI
        default_key = os.getenv("OPENAI_API_KEY", "")
        api_key = st.text_input(
            "OpenAI API Key",
            value=default_key,
            type="password",
            help="API key'inizi https://platform.openai.com adresinden alabilirsiniz"
        )
    
    st.divider()
    
    # Platform seçimi
    platform = st.radio(
        "Choose Platform:",
        ["PLC", "Robot", "NC"],
        key="platform_selector"
    )
    st.session_state.current_platform = platform
    
    # Dil/Marka seçimi
    if platform == "PLC":
        language = st.selectbox(
            "PLC Language:",
            ["ST (Structured Text)", "SCL (Structured Control Language)", "STL (Statement List)"]
        )
        st.session_state.current_language = language.split(" ")[0]
    elif platform == "Robot":
        language = st.selectbox(
            "Robot Brands:",
            ["Fanuc TP", "ABB RAPID", "KUKA KRL", "Yaskawa INFORM"]
        )
        st.session_state.current_language = language.split(" ")[0]
    else:  # NC
        language = st.selectbox(
            "NC Type:",
            ["Siemens 840D-SL", "Fanuc 0i/30i", "Mitsubishi M70/M80"]
        )
        st.session_state.current_language = language.split(" ")[0]
    
    st.divider()
    
    # Örnekler
    st.header("📝 Sample Questions")
    if platform == "PLC":
        st.markdown("""
        - 3 tankı sırayla dolduran program
        - Sıcaklık kontrol sistemi oluştur
        - PID kontrol bloğu yaz
        """)
    elif platform == "Robot":
        st.markdown("""
        - Palet dizilimi programı
        - Kaynak noktaları arası hareket
        - Dairesel hareket trajectoire
        """)
    else:  # NC 
        st.markdown("""
        - 840D SL Alarm 25030 hatası nasıl çözülür?
        - Eksen sürücü arızası için kontrol noktaları
        - Encoder hatası troubleshooting
        """)
    
    st.divider()
    
    # Sohbeti temizle
    if st.button("🗑️ Sohbeti Temizle", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Ana chat alanı
st.header(f"💬 {st.session_state.current_platform} - {st.session_state.current_language}")

# Önceki mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı girişi
if prompt := st.chat_input("Ne yapmak istiyorsunuz? Detaylı açıklayın..."):
    
    # API key kontrolü
    if not api_key:
        st.error("⚠️ Lütfen sidebar'dan API key giriniz!")
        st.stop()
    
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI yanıtı
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # System prompt seç
            if st.session_state.current_platform == "PLC":
                system_prompt = get_plc_system_prompt(st.session_state.current_language)
            elif st.session_state.current_platform == "Robot":
                system_prompt = get_robot_system_prompt(st.session_state.current_language)
            else:  # NC 
                system_prompt = get_nc_system_prompt(st.session_state.current_language)
            
            # Konuşma geçmişini hazırla
            conversation_history = []
            for msg in st.session_state.messages:
                conversation_history.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            # AI Provider'a göre API çağrısı
            if ai_provider == "Google Gemini":
                # Google Gemini API
                try:
                    # Client oluştur
                    client = genai.Client(api_key=api_key)
                    
                    # Chat oluştur
                    chat = client.chats.create(model="gemini-3-flash-preview")
                    
                    # System promptu ve konuşma geçmişini birleştir
                    full_prompt = f"{system_prompt}\n\n"
                    
                    # Konuşma geçmişini ekle
                    for msg in conversation_history:
                        if msg["role"] == "user":
                            full_prompt += f"Kullanıcı: {msg['content']}\n\n"
                        else:
                            full_prompt += f"Asistan: {msg['content']}\n\n"
                    
                    # Mesaj gönder ve yanıt al
                    response = chat.send_message(full_prompt)
                    
                    # Yanıtı ekrana yaz (streaming yok, direk tüm yanıt gelir)
                    full_response = response.text
                    message_placeholder.markdown(full_response)
                            
                except Exception as e:
                    error_msg = str(e)
                    if "404" in error_msg or "not found" in error_msg.lower():
                        st.error(f"""
                                 
**Hata detayı:** {error_msg}
                        """)
                        full_response = "Gemini şu anda kullanılamıyor. Lütfen DeepSeek veya OpenAI seçin."
                    else:
                        st.error(f"Gemini Hatası: {str(e)}")
                        full_response = f"Hata oluştu: {str(e)}"
            
            elif ai_provider == "DeepSeek":
                # DeepSeek API (OpenAI uyumlu)
                client = OpenAI(
                    api_key=api_key,
                    base_url="https://api.deepseek.com"
                )
                
                # System promptu mesajlara ekle
                messages = [{"role": "system", "content": system_prompt}] + conversation_history
                
                # Streaming API çağrısı
                stream = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages,
                    stream=True,
                    max_tokens=4000
                )
                
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        text = chunk.choices[0].delta.content
                        full_response += text
                        message_placeholder.markdown(full_response + "▌")
                
            elif ai_provider == "Anthropic Claude":
                # Anthropic Claude API
                client = Anthropic(api_key=api_key)
                
                with client.messages.stream(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4000,
                    system=system_prompt,
                    messages=conversation_history
                ) as stream:
                    for text in stream.text_stream:
                        full_response += text
                        message_placeholder.markdown(full_response + "▌")
            
            else:  # OpenAI GPT
                # OpenAI API
                client = OpenAI(api_key=api_key)
                
                # System promptu mesajlara ekle
                messages = [{"role": "system", "content": system_prompt}] + conversation_history
                
                # Streaming API çağrısı
                stream = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    stream=True,
                    max_tokens=4000
                )
                
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        text = chunk.choices[0].delta.content
                        full_response += text
                        message_placeholder.markdown(full_response + "▌")
            
            # Son halini göster
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"❌ Hata: {str(e)}")
            full_response = f"Bir hata oluştu: {str(e)}"
    
    # Yanıtı kaydet
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Alt bilgi
st.divider()
st.caption("🔒 Bu uygulama AI API Key kullanır. API key'iniz güvenli bir şekilde saklanır ve paylaşılmaz.")
