# Định nghĩa Bản đồ phần tử giao diện đặc thù cho Miền Ứng dụng (Domain Elements Map)
DOMAINS_ELEMENTS = {
    "Trang_Dang_Nhap": {
        "Nhập tài khoản": "#username",
        "Nhập mật khẩu": "#password",
        "Nút Đăng Nhập": "button[type='submit']",
        "Thông báo nhanh": "#flash"
    },
    "Trang_San_Pham": {
        "Thanh tìm kiếm": "input[name='search']",
        "Nút Tìm kiếm": "button.search-btn",
        "Kết quả đầu tiên": ".product-item:first-child",
        "Nút Thêm vào giỏ": ".add-to-cart",
        "Số lượng giỏ hàng": "#cart-count"
    }
}