import pytest
from playwright.sync_api import Page
from dsl_library.actions import dsl_execute
from dsl_library.data_helper import generate_auth_payloads

@pytest.mark.gui
@pytest.mark.auth
@pytest.mark.parametrize("payload", generate_auth_payloads(), ids=lambda x: x["id"])
def test_domain_authentication_workflow(isolated_page: Page, payload: dict):
    """
    Đặc tả kịch bản kiểm thử giao diện sử dụng Ngôn ngữ đặc thù miền (DSL).
    Kịch bản này tự động nội suy và chạy đệ quy 4 lần dựa trên ma trận dữ liệu.
    """
    page = isolated_page
    
    # Thiết lập tiền đề nghiệp vụ
    page.goto("https://the-internet.herokuapp.com/login", wait_until="networkidle")
    
    # Thực thi tương tác thông qua từ khóa nghiệp vụ thuần Việt
    dsl_execute(page, domain="Trang_Dang_Nhap", keyword="Nhập tài khoản", action_type="input", value=payload["user"])
    dsl_execute(page, domain="Trang_Dang_Nhap", keyword="Nhập mật khẩu", action_type="input", value=payload["pass"])
    dsl_execute(page, domain="Trang_Dang_Nhap", keyword="Nút Đăng Nhập", action_type="click")
    
    # Xác thực kết quả đầu ra
    dsl_execute(page, domain="Trang_Dang_Nhap", keyword="Thông báo nhanh", action_type="verify_text", value=payload["expected"])