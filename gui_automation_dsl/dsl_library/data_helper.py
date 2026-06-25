def generate_auth_payloads() -> list[dict]:
    """
    Sinh ma trận dữ liệu kiểm thử (Data Matrix) cho luồng nghiệp vụ xác thực.
    """
    return [
        {
            "id": "TC01_Valid", 
            "user": "tomsmith", 
            "pass": "SuperSecretPassword!", 
            "expected": "You logged into a secure area!"
        },
        {
            "id": "TC02_InvalidUser", 
            "user": "sai_tai_khoan", 
            "pass": "SuperSecretPassword!", 
            "expected": "Your username is invalid!"
        },
        {
            "id": "TC03_InvalidPass", 
            "user": "tomsmith", 
            "pass": "sai_mat_khau", 
            "expected": "Your password is invalid!"
        },
        {
            "id": "TC04_EmptyFields", 
            "user": "", 
            "pass": "", 
            "expected": "Your username is invalid!"
        }
    ]