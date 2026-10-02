# Hướng dẫn tạo, chỉnh sửa và sử dụng Skill trong ChatGPT

> Tài liệu thực hành giúp bạn hiểu Skill là gì, cách tạo Skill, cấu trúc `SKILL.md`, cách sử dụng, chỉnh sửa và các nguyên tắc thiết kế Skill hiệu quả.

## Mục lục

1. [Skill trong ChatGPT là gì?](#1-skill-trong-chatgpt-là-gì)
2. [Cách tạo một Skill](#2-cách-tạo-một-skill)
3. [Cấu trúc của một Skill](#3-cấu-trúc-của-một-skill)
4. [Ví dụ file SKILL.md](#4-ví-dụ-file-skillmd)
5. [Cách sử dụng Skill](#5-cách-sử-dụng-skill)
6. [Cách chỉnh sửa Skill](#6-cách-chỉnh-sửa-skill)
7. [Phân biệt Skill và Plugin](#7-phân-biệt-skill-và-plugin)
8. [Công thức thiết kế Skill hiệu quả](#8-công-thức-thiết-kế-skill-hiệu-quả)
9. [Ví dụ Skill phân tích báo cáo kinh doanh](#9-ví-dụ-skill-phân-tích-báo-cáo-kinh-doanh)
10. [Quy trình tổng thể](#10-quy-trình-tổng-thể)
11. [Tài liệu tham khảo](#11-tài-liệu-tham-khảo)

---

## 1. Skill trong ChatGPT là gì?

Skill là bộ hướng dẫn để AI làm một công việc lặp lại: khi nào dùng, cần thông tin gì, làm theo bước nào và trả kết quả ra sao. Skill cài đặt sẵn có tên, mô tả và file chính `SKILL.md`; hệ thống có thể cân nhắc dùng skill dựa vào tên và mô tả.

**Phân biệt với thư viện này:** 119 file theo mã `MKT-01`, `SAL-01`... là nội dung hướng dẫn để bạn đọc, sửa và dán vào cuộc trò chuyện. Chúng không tự trở thành Skill cài đặt sẵn chỉ vì có chữ “skill” trong tên. Nếu muốn AI tự chọn, cần đóng gói từng bộ hướng dẫn theo định dạng Skill của nền tảng và kiểm thử sau khi cài.

## 2. Cách tạo một Skill

Nếu chỉ muốn dùng ngay một file trong thư viện, làm theo [Hướng dẫn sử dụng](HUONG-DAN-SU-DUNG.md): điền bối cảnh, dán nội dung vào cuộc trò chuyện, rồi nêu việc cần làm. Không cần tạo Skill cài đặt sẵn.

Nếu muốn tạo Skill cài đặt sẵn:

1. Chọn **một việc cụ thể** mà người dùng thường yêu cầu, ví dụ “viết email nhắc thanh toán”.
2. Viết một câu mô tả nêu cả **việc làm** và **khi nào nên dùng**.
3. Tạo thư mục riêng có file `SKILL.md`; đầu file có `name` và `description` như ví dụ ở mục 4.
4. Trong thân file, ghi đầu vào cần có, các bước xử lý, chỗ nào cần hỏi, kết quả phải giao và điều không được tự đoán.
5. Thử với yêu cầu thông thường, yêu cầu thiếu thông tin và yêu cầu gần giống nhưng không đúng phạm vi. Sửa câu chữ nếu AI chọn sai hoặc trả lời sai.
6. Cài đặt hoặc đưa Skill vào plugin theo cách mà nền tảng và tài khoản của bạn hỗ trợ; kiểm tra hướng dẫn chính thức ở cuối tài liệu trước khi thao tác.

Vị trí menu và quyền tạo Skill phụ thuộc sản phẩm, tài khoản và cấu hình nơi làm việc. Không dựa vào một đường dẫn menu cố định.

---

## 3. Cấu trúc của một Skill

Một Skill có thể được tổ chức theo cấu trúc thư mục như sau:

```text
my-skill/
│
├── SKILL.md
├── references/
│   └── ...
└── scripts/
    └── ...
```

Trong đó:

- **`SKILL.md`**: file hướng dẫn chính của Skill và là thành phần quan trọng nhất.
- **`references/`**: tùy chọn, chứa tài liệu tham khảo mà Skill có thể cần sử dụng.
- **`scripts/`**: tùy chọn, chứa script hoặc code phục vụ cách làm.

Một Skill đơn giản có thể chỉ cần `SKILL.md`.

---

## 4. Ví dụ file SKILL.md

Ví dụ Skill viết email công việc bằng tiếng Việt:

```markdown
---
name: professional-email-vn
description: Viết và chỉnh sửa email công việc bằng tiếng Việt theo phong cách chuyên nghiệp, ngắn gọn và tự nhiên.
---

Sử dụng skill này khi người dùng muốn:
- viết email công việc;
- trả lời email;
- chỉnh sửa email;
- làm email chuyên nghiệp hơn.

Quy trình:

1. Xác định người nhận.
2. Xác định mục đích email.
3. Xác định hành động người gửi mong muốn.
4. Viết tiêu đề email.
5. Viết nội dung ngắn gọn, chuyên nghiệp.
6. Kiểm tra chính tả và ngữ pháp.
7. Loại bỏ những câu dài hoặc sáo rỗng.

Kết quả:

Subject: ...

Nội dung email:
...

Không tự bịa thông tin mà người dùng chưa cung cấp.
```

### Vai trò của `name` và `description`

Hai trường này đặc biệt quan trọng:

```yaml
name: professional-email-vn
description: Viết và chỉnh sửa email công việc bằng tiếng Việt theo phong cách chuyên nghiệp, ngắn gọn và tự nhiên.
```

`name` giúp xác định Skill, còn `description` mô tả Skill làm gì và trong trường hợp nào Skill phù hợp. Description nên đủ rõ để hệ thống có thể phân biệt Skill này với các Skill khác.

Phần thân của `SKILL.md` chứa hướng dẫn chi tiết về cách làm, quy tắc và đầu ra mong muốn.

---

## 5. Cách sử dụng Skill

Sau khi Skill đã được cài đặt, có hai cách sử dụng chính.

### Cách 1: Để ChatGPT tự chọn Skill

Bạn đưa yêu cầu bình thường, ví dụ:

```text
Viết giúp tôi email xin khách hàng dời cuộc họp sang thứ Sáu.
```

Nếu Skill `professional-email-vn` được mô tả phù hợp, ChatGPT có thể nhận biết rằng cách làm của Skill nên được sử dụng.

### Cách 2: Chủ động gọi Skill

Nếu giao diện ChatGPT của bạn hỗ trợ việc chọn hoặc mention Skill, bạn có thể chủ động chọn Skill trước khi đưa yêu cầu.

Cách này hữu ích khi:

- Có nhiều Skill có chức năng gần giống nhau.
- Bạn muốn chắc chắn một cách làm cụ thể được áp dụng.
- Bạn đang kiểm thử Skill mới.
- Bạn muốn so sánh kết quả có và không sử dụng Skill.

---

## 6. Cách chỉnh sửa Skill

Mở file `SKILL.md` hoặc nơi lưu hướng dẫn của Skill do bạn quản lý để sửa. Bạn cũng có thể mô tả thay đổi mong muốn bằng ngôn ngữ tự nhiên rồi đọc lại bản đã sửa trước khi dùng.

Ví dụ:

```text
Sửa skill professional-email-vn của tôi.

Thêm các quy tắc:
- Email mặc định dưới 200 từ.
- Nếu email gửi lãnh đạo thì trang trọng hơn.
- Nếu gửi đồng nghiệp thì thân thiện hơn.
- Không dùng emoji trừ khi tôi yêu cầu.
- Cuối cùng luôn kiểm tra xem CTA đã rõ ràng chưa.
```

Một cách phát triển Skill hiệu quả là:

```text
Tạo Skill
   ↓
Dùng thử
   ↓
Quan sát lỗi / điểm chưa tốt
   ↓
Sửa hướng dẫn
   ↓
Dùng thử lại
   ↓
Tiếp tục tối ưu
```

Không nên cố viết một Skill hoàn hảo ngay từ lần đầu. Việc kiểm thử với các tình huống thực tế thường giúp bạn phát hiện những quy tắc còn thiếu.

---

## 7. Phân biệt Skill và Plugin

Có thể hiểu đơn giản:

> **Skill = ChatGPT nên thực hiện công việc này như thế nào?**

Ví dụ Skill phân tích báo cáo:

```text
Đọc báo cáo
→ tìm KPI
→ so sánh tháng trước
→ tìm bất thường
→ đưa ra 5 insight
→ tạo bản tóm tắt cho người quản lý
```

Trong khi đó, **Plugin** có thể cung cấp phạm vi rộng hơn, chẳng hạn kết hợp cách làm với các công cụ, dữ liệu hoặc hành động từ hệ thống bên ngoài.

Ví dụ về một Plugin phục vụ Weekly Sales Review:

```text
PLUGIN: Weekly Sales Review

├── Skill
│   └── Quy trình phân tích sales
│
├── Google Sheets
│   └── lấy dữ liệu doanh số
│
├── Slack
│   └── lấy cập nhật từ sales team
│
└── Skill
    └── tạo báo cáo tuần
```

Có thể ghi nhớ ngắn gọn:

- **Skill** hướng dẫn ChatGPT **cách làm**.
- **Tool/App/Connector** cung cấp **dữ liệu hoặc hành động**.
- **Plugin** có thể đóng gói cách làm và khả năng kết nối/công cụ thành một trải nghiệm rộng hơn.

---

## 8. Công thức thiết kế Skill hiệu quả

Khi xây dựng Skill, nên trả lời rõ sáu câu hỏi sau:

```text
1. KHI NÀO DÙNG
Khi nào skill này được sử dụng?

2. THÔNG TIN CẦN
Skill cần thông tin gì?

3. CÁCH LÀM
ChatGPT phải làm những bước nào?

4. QUY TẮC
Có những điều gì bắt buộc / bị cấm?

5. KẾT QUẢ
Kết quả phải có cấu trúc như thế nào?

6. TỰ KIỂM TRA
Trước khi trả lời phải kiểm tra những gì?
```

### 8.1. KHI NÀO DÙNG — Khi nào sử dụng Skill?

Mô tả rõ các tình huống mà Skill nên được kích hoạt.

Ví dụ:

```text
Sử dụng skill này khi người dùng yêu cầu phân tích báo cáo doanh thu,
chỉ số đo kết quả, báo cáo kinh doanh hoặc dữ liệu hiệu quả công việc.
```

### 8.2. THÔNG TIN CẦN — Skill cần dữ liệu gì?

Liệt kê những thông tin Skill cần để thực hiện công việc.

Ví dụ:

```text
THÔNG TIN CẦN:
- File báo cáo
- Khoảng thời gian
- KPI cần phân tích
- Mục tiêu kinh doanh
```

Nếu một thông tin đầu vào là bắt buộc nhưng chưa có, Skill nên biết khi nào cần hỏi người dùng thay vì tự suy đoán.

### 8.3. CÁCH LÀM — Quy trình xử lý

Đây là phần quan trọng nhất của cách làm.

Ví dụ:

```text
CÁCH LÀM:
1. Đọc dữ liệu.
2. Xác định KPI.
3. So sánh với kỳ trước.
4. Phát hiện bất thường.
5. Tìm các yếu tố có thể giải thích từ dữ liệu.
6. Nêu điều đáng chú ý rút ra từ dữ liệu và bằng chứng đi kèm.
```

Các bước nên đủ cụ thể để tạo kết quả ổn định, nhưng không nên chi tiết đến mức khiến Skill không thể xử lý những trường hợp hơi khác dự kiến.

### 8.4. QUY TẮC — Các quy tắc

Ví dụ:

```text
QUY TẮC:
- Không bịa số liệu.
- Không kết luận nguyên nhân nếu dữ liệu không chứng minh được.
- Phân biệt dữ liệu đã kiểm chứng và giả định.
- Nếu thiếu dữ liệu phải nói rõ.
```

### 8.5. KẾT QUẢ — Định dạng kết quả

Ghi rõ kết quả cần giao, nhưng chỉ xuất phần người dùng yêu cầu. Nếu họ đưa mẫu công ty, dùng mẫu đó trước.

Ví dụ:

```text
KẾT QUẢ:

## Tóm tắt kết luận

## Chỉ số chính

## Điểm đang tốt

## Vấn đề cần xử lý

## Nguyên nhân có thể có

## Việc nên làm tiếp
```

Điều này giúp kết quả giữa nhiều lần chạy nhất quán hơn.

### 8.6. TỰ KIỂM TRA — Kiểm tra chất lượng

Skill nên có bước tự kiểm tra trước khi hoàn thành.

Ví dụ:

```text
TỰ KIỂM TRA:
- Kiểm tra lại số liệu.
- Kiểm tra các phép so sánh.
- Kiểm tra kết luận có được dữ liệu hỗ trợ hay không.
- Kiểm tra dữ liệu đã xác nhận và giả định có được tách rõ chưa.
- Kiểm tra kết quả có đúng yêu cầu của người dùng không.
```

---

## 9. Ví dụ Skill phân tích báo cáo kinh doanh

Bạn có thể bắt đầu bằng prompt tạo Skill như sau:

```text
Hãy tạo cho tôi skill "business-report-analyzer".

KHI NÀO DÙNG:
Sử dụng khi tôi upload báo cáo kinh doanh,
Excel, CSV hoặc PDF và yêu cầu phân tích.

THÔNG TIN CẦN:
- Báo cáo
- Khoảng thời gian
- KPI nếu người dùng cung cấp

CÁCH LÀM:
1. Xác định KPI chính.
2. So sánh với kỳ trước.
3. Tìm tăng trưởng và suy giảm.
4. Phát hiện bất thường.
5. Tìm nguyên nhân có thể giải thích từ dữ liệu.
6. Đưa ra các vấn đề cần điều tra thêm.

KẾT QUẢ:
Tóm tắt kết luận

Chỉ số chính

Điểm đang tốt

Vấn đề cần xử lý

Nguyên nhân có thể có

Việc nên làm tiếp

QUY TẮC:
- Không bịa số liệu.
- Phân biệt dữ liệu đã kiểm chứng và giả định.
- Mọi kết luận phải dựa trên dữ liệu.
- Nếu thiếu dữ liệu phải nói rõ.

TỰ KIỂM TRA:
Kiểm tra lại tất cả số liệu trước khi trả kết quả.
```

### Vì sao cấu trúc này hữu ích?

Nó tách rõ:

- Thời điểm cần dùng Skill.
- Dữ liệu đầu vào.
- Quy trình phân tích.
- Cấu trúc đầu ra.
- Quy tắc chống bịa thông tin.
- Bước kiểm tra chất lượng.

Nhờ vậy Skill dễ đọc, dễ sửa và dễ kiểm thử hơn.

### Nên tạo Skill nhỏ hay Skill lớn?

Thông thường, nên ưu tiên các Skill tập trung vào một nhiệm vụ tương đối rõ ràng thay vì nhồi toàn bộ quy trình doanh nghiệp vào một Skill khổng lồ.

Ví dụ thay vì một Skill:

```text
all-company-operations
```

bạn có thể tách thành:

```text
sales-report-analyzer
professional-email-vn
meeting-summary
customer-feedback-analyzer
weekly-business-review
```

Mỗi Skill trở thành một phần việc có thể tái sử dụng.

---

## 10. Quy trình tổng thể

Có thể hình dung vòng đời của một Skill như sau:

```text
Ý tưởng
   ↓
Mô tả công việc
   ↓
Viết Skill
   ↓
SKILL.md
   ↓
Dùng thử
   ↓
Sửa hướng dẫn
   ↓
Cài đặt nếu cần
   ↓
Dùng trong ChatGPT
   ↓
ChatGPT tự kích hoạt
hoặc bạn gọi trực tiếp
   ↓
Tiếp tục chỉnh sửa / chia sẻ
```

Một quy trình thực tế nên là:

1. Chọn một công việc bạn thực hiện thường xuyên.
2. Xác định rõ KHI NÀO DÙNG, THÔNG TIN CẦN, CÁCH LÀM, QUY TẮC, KẾT QUẢ và TỰ KIỂM TRA.
3. Viết phiên bản đầu tiên của `SKILL.md`.
4. Dùng thử với nhiều tình huống thực tế.
5. Ghi lại những lỗi hoặc kết quả không mong muốn.
6. Bổ sung/chỉnh sửa instructions.
7. Dùng thử lại.
8. Khi Skill đã ổn định, sử dụng nó như một cách làm tái sử dụng.

### Checklist nhanh trước khi hoàn thành Skill

- [ ] Tên Skill có rõ ràng không?
- [ ] Description có mô tả đúng lúc cần sử dụng Skill không?
- [ ] Input cần thiết đã được xác định chưa?
- [ ] Quy trình có thứ tự rõ ràng không?
- [ ] Có quy định những điều ChatGPT không được tự suy đoán không?
- [ ] Kết quả có định dạng cụ thể không?
- [ ] Có bước quality check không?
- [ ] Đã test với trường hợp bình thường chưa?
- [ ] Đã test với trường hợp thiếu dữ liệu chưa?
- [ ] Đã test với trường hợp dữ liệu mâu thuẫn chưa?

---

## 11. Tài liệu tham khảo

Các tài liệu OpenAI liên quan đã được đề cập trong hướng dẫn ban đầu:

- OpenAI Developers — Skills concepts: https://developers.openai.com/plugins/concepts/skills
- OpenAI Developers — Build skills: https://developers.openai.com/plugins/build/skills

> Các tính năng, vị trí menu và phạm vi tài khoản hỗ trợ có thể thay đổi theo thời gian. Khi triển khai thực tế, nên kiểm tra tài liệu OpenAI mới nhất.

---

## Mẫu khung SKILL.md để tái sử dụng

Bạn có thể copy mẫu dưới đây để bắt đầu Skill mới:

```markdown
---
name: your-skill-name
description: Mô tả ngắn gọn Skill làm gì và khi nào nên sử dụng.
---

# Mục tiêu

Mô tả mục tiêu chính của Skill.

# KHI NÀO DÙNG

Sử dụng Skill này khi:
- ...
- ...

Không sử dụng khi:
- ...

# THÔNG TIN CẦN

Thông tin cần thiết:
- ...
- ...

Nếu thiếu thông tin đầu vào bắt buộc:
- Hỏi người dùng trước khi tiếp tục.

# CÁCH LÀM

1. ...
2. ...
3. ...
4. ...

# QUY TẮC

- Không tự bịa dữ liệu.
- Không suy đoán thông tin quan trọng khi chưa có bằng chứng.
- ...

# KẾT QUẢ

## Phần 1
...

## Phần 2
...

## Phần 3
...

# TỰ KIỂM TRA

Trước khi hoàn thành:
- Kiểm tra ...
- Kiểm tra ...
- Đảm bảo ...
```

Mẫu này có thể dùng làm điểm khởi đầu cho các Skill như nghiên cứu thị trường, viết content, phân tích Excel, viết email, review code, làm báo cáo hoặc phân tích tài chính.
