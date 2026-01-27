from app.security.security import create_acess_token, decode_token

def test_jwt_creation_and_validation():
    subject = "user_id_123"

    token = create_acess_token(subject)
    decoded = decode_token(token)

    assert decoded["sub"] == subject
    assert "exp" in decoded
    assert "iat" in decoded

