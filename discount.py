def calculate_discount(past_total, current_order):
    """
    Tính toán tỷ lệ giảm giá dựa trên lịch sử mua hàng và đơn hàng hiện tại.
    past_total: Tổng giá trị các đơn hàng trước đây trong năm
    current_order: Giá trị của đơn hàng mới đang thực hiện
    """
    # Tính tổng tích lũy sau khi cộng dồn đơn hàng hiện tại
    total_accumulated = past_total + current_order
    
    if total_accumulated >= 50000000:
        return 0.1  # Giảm giá 10%
    else:
        return 0.0  # Không giảm giá
    # Cập nhật để lấy ảnh minh chứng git status

    