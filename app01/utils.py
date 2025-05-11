

_MODEL = None

def get_credentials(debug=False):
    try:
        import os
        from dotenv import load_dotenv
        from google.oauth2 import service_account

        load_dotenv()
        service_account_file = os.getenv("GOOGLE_KEY_PATH")

        if service_account_file and os.path.exists(service_account_file):
            credentials = service_account.Credentials.from_service_account_file(
                service_account_file,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
            return credentials
        else:
            if debug:
                print("⚠️ 找不到金鑰檔案或未設定 GOOGLE_KEY_PATH")
            return None

    except Exception as e:
        if debug:
            print(f"⚠️ 無法初始化憑證：{e}")
        return None


def _ensure_initialized(debug=False):
    global _MODEL
    if _MODEL is None:
        try:
            import vertexai
            from vertexai.preview.language_models import ChatModel

            credentials = get_credentials(debug=debug)
            if not credentials:
                raise Exception("⚠️ 憑證為 None，無法初始化 Vertex AI")

            vertexai.init(
                project="my-project-111707006",
                location="us-central1",
                credentials=credentials
            )
            _MODEL = ChatModel.from_pretrained("chat-bison")

        except Exception as e:
            if debug:
                print(f"⚠️ VertexAI 初始化失敗：{e}")
            return None

    return _MODEL


def ask_gemini(prompt: str) -> str:
    model = _ensure_initialized()
    if model is None:
        return "⚠️ 無法回應，模型尚未初始化"
    try:
        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini 回應失敗：{e}"


def translate_text(text: str) -> str:
    return ask_gemini(f"請將以下內容翻譯成英文：\n{text}")

def summarize_text(text: str) -> str:
    return ask_gemini(f"請為以下筆記產生一段摘要：\n{text}")

def rewrite_text(text: str) -> str:
    return ask_gemini(f"請將下列內容改寫成更專業、簡潔的語氣：\n{text}")
