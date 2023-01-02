---
title:  "Subset sum problem"
mathjax: true
layout: post
categories: DLB
---

Bài toán tổng con (SSP) là một dạng bài toán ra quyết định (decision making).

Input: Cho các tập hợp con của tập các số nguyên $$S$$ và một tổng mục tiêu (target-sum) $$T$$

Output: Liệu có tồn tại bất kỳ tập hợp con nào có tổng chính xác bằng $$T$$ hay không?

Phân loại bài toán: NP-hard

Ràng buộc thêm vào để trở thành bài toán NP-complete
- Tập hợp đầu vào gồm các số dương
- Tập hợp đầu vào gồm các số dương và âm với tổng mục tiêu $$T = 0$$
- Tập hợp đầu vào gồm các số dương và tổng mục tiêu bằng một nửa tổng tất cả đầu vào, bài toán phân hoạch !

Bên cạnh đó, có thể xem xét bài toán này dưới góc nhìn tối ưu hóa (optimisation problem): Tìm một tập con mà tổng của nó gần bằng $$T$$

## Computational hardness

*Computational hardness: Trong lý thuyết phân tích độ phức tạp, một giả định Computational hardness là một giả thuyết mà một bài toán cụ thể không thể giải một cách hiệu quả (hiệu quả ở đây là tính toán được trong thời gian đa thức - polynomial time).

Xem chi tiết trong [Computational Hardness and One-wayness - Cryptography/Computer Science 687/Cornell University/ Spring 2008](https://www.cs.cornell.edu/courses/cs687/2008sp/chap2.pdf)

Độ phức tạp thời gian thực thi của SSP phụ thuộc vào hai tham số
- $$n$$ - tức số lượng đầu vào nguyên. Nếu $$n$$ là một số cố định tương đối nhỏ, thì phương pháp tìm kiếm đầy đủ (exhaustive search) có thể là một giải pháp thực tế
- $$L$$ độ chính xác của bài toán, có thể hiểu là số lượng vị trí nhị phân mà cần để làm trạng thái cho bài toán. Nếu mà $$L$$ là một số cố định tương đối nhỏ, chiến lược quy hoạch động (dynamic programming) có thể được dùng để giải bài toán này một cách chính xác.

Tuy nhiên, nếu cả $$n$$ và $$L$$ ngày càng lớn, SSP là NP-hard. Độ phức tạp tốt nhất cho các thuật toán tốt nhất là exponential của số nhỏ hơn trong hai tham số $$n$$ và $$L$$

## Exponential time algorithms

### Thuật toán ngây thơ inclusion–exclusion

Thuật toán: Duyệt tất cả tập hợp con của $$n$$ số và, với mỗi chúng, kiểm tra nếu tổng của tập con này có bằng với $$T$$ hay không?

Độ phức tạp thời gian thực thi: $$O(2^n \cdot n)$$

Cài đặt thuật toán bằng tìm kiếm theo chiều sâu (depth-first search) trên một cây nhị phân: mỗi cấp trong cây tương ứng với một số đầu vào; nhánh bên trái tương ứng với số loại từ khỏi tập hợp (excluding number), và nhánh bên phải tương ứng với số thêm vào tập hợp (including number). Độ phức tạp bộ nhớ $$O(n)$$

```py
def inclusion_exclusion_ssp(inp_set, target):
    if len(inp_set) == 0:
        return target == 0
    else:
        first_element = inp_set[0]
        rest = inp_set[1:]
        return inclusion_exclusion_ssp(rest, target) or inclusion_exclusion_ssp(rest, target - first_element)
```