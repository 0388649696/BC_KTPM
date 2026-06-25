import pytest
import os
import shutil
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session", autouse=True)
def system_environment_setup():
    """
    Fixture cấp phiên làm việc (Session Scope).
    Tự động khởi tạo cấu trúc thư mục lưu trữ minh chứng kiểm thử (Artifacts)
    và dọn dẹp dữ liệu của các phiên chạy trước.
    """
    print("\n[System] Khởi tạo môi trường kiểm thử tự động...")
    if os.path.exists("test_outputs"):
        shutil.rmtree("test_outputs")
    os.makedirs("test_outputs/screenshots", exist_ok=True)
    
    yield # Bàn giao quyền điều khiển cho các kịch bản kiểm thử
    
    print("\n[System] Hoàn tất phiên kiểm thử. Đã lưu minh chứng tại /test_outputs")

@pytest.fixture(scope="function")
def isolated_page(playwright: Playwright):
    """
    Fixture cấp kịch bản (Function Scope).
    Cấp phát một ngữ cảnh trình duyệt (Browser Context) hoàn toàn độc lập 
    cho mỗi ca kiểm thử nhằm ngăn chặn xung đột trạng thái (State Leakage).
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={'width': 1280, 'height': 720},
        user_agent="Vnmu/DSL-Automation-Framework v1.0"
    )
    page = context.new_page()
    
    yield page
    
    context.close()
    browser.close()