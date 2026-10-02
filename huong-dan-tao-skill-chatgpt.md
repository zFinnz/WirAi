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

Trong ChatGPT, **Skill** có thể hiểu là một workflow hoặc bộ hướng dẫn có thể tái sử dụng. Bạn mô tả cho ChatGPT cách thực hiện một loại công việc, các bước cần tuân theo, định dạng đầu ra, ví dụ, tài liệu tham chiếu và khi cần có thể kèm script/code.

Sau khi Skill được cài đặt, ChatGPT có thể nhận biết khi nào Skill phù hợp với yêu cầu hoặc bạn có thể chủ động gọi Skill khi muốn sử dụng workflow đó.

> **Lưu ý về khả dụng:** Tính năng Skills có thể phụ thuộc vào loại tài khoản, workspace và cấu hình sản phẩm hiện tại. Nếu bạn không thấy mục Skills/Kỹ năng trong giao diện ChatGPT, tài khoản hoặc workspace của bạn có thể chưa được cấp tính năng này.

---

## 2. Cách tạo một Skill

Khi giao diện tài khoản của bạn hỗ trợ Skills, cách phổ biến là vào khu vực quản lý **Plugins/Tiện ích → Skills/Kỹ năng → Create/Tạo** rồi chọn phương thức tạo phù hợp.

Bạn có thể mô tả Skill bằng ngôn ngữ tự nhiên. Ví dụ:

```text
Hãy tạo cho tôi một skill tên professional-email-vn.

Skill này dùng khi tôi yêu cầu viết hoặc chỉnh sửa email công việc bằng tiếng Việt.

Yêu cầu:
- Văn phong chuyên nghiệp, tự nhiên.
- Không quá dài.
- Không dùng từ ngữ sáo rỗng.
- Nếu thiếu người nhận hoặc mục đích email thì hỏi lại.
- Luôn đưa ra subject phù hợp.
- Kiểm tra lỗi chính tả trước khi trả kết quả.
```

ChatGPT hoặc công cụ tạo Skill có thể giúp chuyển yêu cầu trên thành cấu trúc Skill hoàn chỉnh.

Ngoài cách tạo bằng hội thoại, tùy giao diện được cung cấp, bạn có thể có các lựa chọn như:

- Tạo bằng editor để tự kiểm soát nội dung Skill.
- Upload Skill đã chuẩn bị sẵn trên máy.
- Chỉnh sửa Skill đã tạo trước đó.

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
- **`scripts/`**: tùy chọn, chứa script hoặc code phục vụ workflow.

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

Output:

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

Phần thân của `SKILL.md` chứa hướng dẫn chi tiết về workflow, quy tắc và đầu ra mong muốn.

---

## 5. Cách sử dụng Skill

Sau khi Skill đã được cài đặt, có hai cách sử dụng chính.

### Cách 1: Để ChatGPT tự chọn Skill

Bạn đưa yêu cầu bình thường, ví dụ:

```text
Viết giúp tôi email xin khách hàng dời cuộc họp sang thứ Sáu.
```

Nếu Skill `professional-email-vn` được mô tả phù hợp, ChatGPT có thể nhận biết rằng workflow của Skill nên được sử dụng.

### Cách 2: Chủ động gọi Skill

Nếu giao diện ChatGPT của bạn hỗ trợ việc chọn hoặc mention Skill, bạn có thể chủ động chọn Skill trước khi đưa yêu cầu.

Cách này hữu ích khi:

- Có nhiều Skill có chức năng gần giống nhau.
- Bạn muốn chắc chắn một workflow cụ thể được áp dụng.
- Bạn đang kiểm thử Skill mới.
- Bạn muốn so sánh kết quả có và không sử dụng Skill.

---

## 6. Cách chỉnh sửa Skill

Bạn có thể mở khu vực quản lý Skills và chọn Skill do mình tạo để chỉnh sửa.

Ngoài chỉnh sửa trực tiếp bằng editor, bạn có thể mô tả thay đổi mong muốn bằng ngôn ngữ tự nhiên.

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
Sửa instructions
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
→ tạo executive summary
```

Trong khi đó, **Plugin** có thể cung cấp phạm vi rộng hơn, chẳng hạn kết hợp workflow với các công cụ, dữ liệu hoặc hành động từ hệ thống bên ngoài.

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
- **Plugin** có thể đóng gói workflow và khả năng kết nối/công cụ thành một trải nghiệm rộng hơn.

---

## 8. Công thức thiết kế Skill hiệu quả

Khi xây dựng Skill, nên trả lời rõ sáu câu hỏi sau:

```text
1. WHEN
Khi nào skill này được sử dụng?

2. INPUT
Skill cần thông tin gì?

3. PROCESS
ChatGPT phải làm những bước nào?

4. RULES
Có những điều gì bắt buộc / bị cấm?

5. OUTPUT
Kết quả phải có cấu trúc như thế nào?

6. QUALITY CHECK
Trước khi trả lời phải kiểm tra những gì?
```

### 8.1. WHEN — Khi nào sử dụng Skill?

Mô tả rõ các tình huống mà Skill nên được kích hoạt.

Ví dụ:

```text
Sử dụng skill này khi người dùng yêu cầu phân tích báo cáo doanh thu,
KPI, báo cáo kinh doanh hoặc dữ liệu performance.
```

### 8.2. INPUT — Skill cần dữ liệu gì?

Liệt kê những thông tin Skill cần để thực hiện công việc.

Ví dụ:

```text
INPUT:
- File báo cáo
- Khoảng thời gian
- KPI cần phân tích
- Mục tiêu kinh doanh
```

Nếu một input là bắt buộc nhưng chưa có, Skill nên biết khi nào cần hỏi người dùng thay vì tự suy đoán.

### 8.3. PROCESS — Quy trình xử lý

Đây là phần quan trọng nhất của workflow.

Ví dụ:

```text
PROCESS:
1. Đọc dữ liệu.
2. Xác định KPI.
3. So sánh với kỳ trước.
4. Phát hiện bất thường.
5. Tìm các yếu tố có thể giải thích từ dữ liệu.
6. Tổng hợp insight.
```

Các bước nên đủ cụ thể để tạo kết quả ổn định, nhưng không nên chi tiết đến mức khiến Skill không thể xử lý những trường hợp hơi khác dự kiến.

### 8.4. RULES — Các quy tắc

Ví dụ:

```text
RULES:
- Không bịa số liệu.
- Không kết luận nguyên nhân nếu dữ liệu không chứng minh được.
- Phân biệt fact và hypothesis.
- Nếu thiếu dữ liệu phải nói rõ.
```

### 8.5. OUTPUT — Định dạng kết quả

Một Skill tốt nên quy định rõ output.

Ví dụ:

```text
OUTPUT:

## Executive Summary

## Key Metrics

## Positive Signals

## Problems

## Possible Causes

## Recommended Next Steps
```

Điều này giúp kết quả giữa nhiều lần chạy nhất quán hơn.

### 8.6. QUALITY CHECK — Kiểm tra chất lượng

Skill nên có bước tự kiểm tra trước khi hoàn thành.

Ví dụ:

```text
QUALITY CHECK:
- Kiểm tra lại số liệu.
- Kiểm tra các phép so sánh.
- Kiểm tra kết luận có được dữ liệu hỗ trợ hay không.
- Kiểm tra xem fact và hypothesis đã được phân biệt chưa.
- Kiểm tra output có đúng cấu trúc yêu cầu không.
```

---

## 9. Ví dụ Skill phân tích báo cáo kinh doanh

Bạn có thể bắt đầu bằng prompt tạo Skill như sau:

```text
Hãy tạo cho tôi skill "business-report-analyzer".

WHEN:
Sử dụng khi tôi upload báo cáo kinh doanh,
Excel, CSV hoặc PDF và yêu cầu phân tích.

INPUT:
- Báo cáo
- Khoảng thời gian
- KPI nếu người dùng cung cấp

PROCESS:
1. Xác định KPI chính.
2. So sánh với kỳ trước.
3. Tìm tăng trưởng và suy giảm.
4. Phát hiện bất thường.
5. Tìm nguyên nhân có thể giải thích từ dữ liệu.
6. Đưa ra các vấn đề cần điều tra thêm.

OUTPUT:
Executive Summary

Key Metrics

Positive Signals

Problems

Possible Causes

Recommended Next Steps

RULES:
- Không bịa số liệu.
- Phân biệt fact và hypothesis.
- Mọi kết luận phải dựa trên dữ liệu.
- Nếu thiếu dữ liệu phải nói rõ.

QUALITY CHECK:
Kiểm tra lại tất cả số liệu trước khi trả kết quả.
```

### Vì sao cấu trúc này hữu ích?

Nó tách rõ:

- Trigger của Skill.
- Dữ liệu đầu vào.
- Quy trình phân tích.
- Cấu trúc đầu ra.
- Quy tắc chống hallucination.
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

Mỗi Skill trở thành một building block có thể tái sử dụng.

---

## 10. Quy trình tổng thể

Có thể hình dung vòng đời của một Skill như sau:

```text
Ý tưởng
   ↓
Mô tả công việc
   ↓
Create Skill
   ↓
SKILL.md
   ↓
Test
   ↓
Sửa instructions
   ↓
Install
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
2. Xác định rõ WHEN, INPUT, PROCESS, RULES, OUTPUT và QUALITY CHECK.
3. Viết phiên bản đầu tiên của `SKILL.md`.
4. Test với nhiều tình huống thực tế.
5. Ghi lại những lỗi hoặc kết quả không mong muốn.
6. Bổ sung/chỉnh sửa instructions.
7. Test lại.
8. Khi Skill đã ổn định, sử dụng nó như một workflow tái sử dụng.

### Checklist nhanh trước khi hoàn thành Skill

- [ ] Tên Skill có rõ ràng không?
- [ ] Description có mô tả đúng lúc cần sử dụng Skill không?
- [ ] Input cần thiết đã được xác định chưa?
- [ ] Quy trình có thứ tự rõ ràng không?
- [ ] Có quy định những điều ChatGPT không được tự suy đoán không?
- [ ] Output có format cụ thể không?
- [ ] Có bước quality check không?
- [ ] Đã test với trường hợp bình thường chưa?
- [ ] Đã test với trường hợp thiếu dữ liệu chưa?
- [ ] Đã test với trường hợp dữ liệu mâu thuẫn chưa?

---

## 11. Tài liệu tham khảo

Các tài liệu OpenAI liên quan đã được đề cập trong hướng dẫn ban đầu:

- Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Plugins in ChatGPT: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- OpenAI Developers — Skills concepts: https://developers.openai.com/plugins/concepts/skills
- OpenAI Developers — Build skills: https://developers.openai.com/plugins/build/skills
- OpenAI Academy — Skills: https://openai.com/academy/skills/

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

# WHEN

Sử dụng Skill này khi:
- ...
- ...

Không sử dụng khi:
- ...

# INPUT

Thông tin cần thiết:
- ...
- ...

Nếu thiếu input bắt buộc:
- Hỏi người dùng trước khi tiếp tục.

# PROCESS

1. ...
2. ...
3. ...
4. ...

# RULES

- Không tự bịa dữ liệu.
- Không suy đoán thông tin quan trọng khi chưa có bằng chứng.
- ...

# OUTPUT

## Phần 1
...

## Phần 2
...

## Phần 3
...

# QUALITY CHECK

Trước khi hoàn thành:
- Kiểm tra ...
- Kiểm tra ...
- Đảm bảo ...
```

Mẫu này có thể dùng làm điểm khởi đầu cho các Skill như nghiên cứu thị trường, viết content, phân tích Excel, viết email, review code, làm báo cáo hoặc phân tích tài chính.
