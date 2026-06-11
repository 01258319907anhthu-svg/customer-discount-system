import pytest
from discount import calculate_discount

# --- 2 Test cases ban đầu theo tài liệu hướng dẫn ---
def test_vip_customer():
    # Đã mua 60M (đạt VIP trước đó) -> Đơn hàng mới (ví dụ 2M) chắc chắn được giảm 10%
    assert calculate_discount(60000000, 2000000) == 0.1

def test_normal_customer():
    # Đã mua 30M, đơn mới 2M -> Tổng mới 32M (< 50M) -> Không giảm giá
    assert calculate_discount(30000000, 2000000) == 0.0

# --- 3 Test cases kiểm thử nghiệp vụ do bộ phận kinh doanh yêu cầu ---
def test_tc01():
    # TC01: Trước: 60M, Hiện tại: 2M -> Tổng 62M >= 50M -> Giảm 10%
    assert calculate_discount(60000000, 2000000) == 0.1

def test_tc02():
    # TC02: Trước: 30M, Hiện tại: 2M -> Tổng 32M < 50M -> Không giảm
    assert calculate_discount(30000000, 2000000) == 0.0

def test_tc03():
    # TC03: Trước: 49M, Hiện tại: 2M -> Tổng mới 51M >= 50M -> Phải được giảm 10%
    assert calculate_discount(49000000, 2000000) == 0.1