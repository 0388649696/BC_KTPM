import time
from playwright.sync_api import Page, expect
from dsl_library.domain_maps import DOMAINS_ELEMENTS

def dsl_execute(page: Page, domain: str, keyword: str, action_type: str, value: str = None) -> None:
    """
    Hàm thực thi đa hình điều phối toàn bộ hành vi tương tác giao diện.
    """
    # 1. Truy xuất định danh kỹ thuật từ Bản đồ giao diện
    try:
        selector = DOMAINS_ELEMENTS[domain][keyword]
    except KeyError:
        raise ValueError(f"[Lỗi Kiến trúc] Từ khóa '{keyword}' chưa được định nghĩa tại miền '{domain}'")

    element = page.locator(selector)
    
    # 2. Xử lý hành vi và áp dụng thuật toán đợi đồng bộ (Explicit Waits)
    try:
        if action_type == "input":
            element.wait_for(state="visible", timeout=5000)
            element.fill("")
            element.type(value, delay=30)
            
        elif action_type == "click":
            element.wait_for(state="attached", timeout=5000)
            element.scroll_into_view_if_needed()
            element.click()
            
        elif action_type == "verify_text":
            expect(element).to_be_visible(timeout=5000)
            expect(element).to_contain_text(value)
            
    except Exception as e:
        # 3. Tự động chụp ảnh màn hình lưu vết khi xảy ra sự cố chập chờn (Flakiness)
        timestamp = int(time.time())
        screenshot_path = f"test_outputs/screenshots/Loi_{domain}_{keyword}_{timestamp}.png"
        page.screenshot(path=screenshot_path)
        raise AssertionError(f"[Lỗi Thực thi] Thất bại thao tác '{action_type}' trên '{keyword}'. Minh chứng: {screenshot_path}\nChi tiết: {str(e)}")