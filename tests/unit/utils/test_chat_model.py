from src.utilities.chat_model import create_chat_model


def test_chat_model_creation():
    chat_model = create_chat_model()
    assert chat_model is not None
    assert chat_model.temperature == 0.5
