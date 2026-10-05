# Hướng dẫn tạo, chỉnh sửa và sử dụng Skill trong ChatGPT

> Tài liệu thực hành: skill là gì, cách tạo skill, cách đóng gói một file trong thư viện thành skill, cấu trúc `SKILL.md`, cách dùng, cách sửa và công thức thiết kế. Cách làm theo bài [Skill](#skill) của khóa học. Tên menu tra ngày 05/10/2026.

## Mục lục

1. [Skill trong ChatGPT là gì?](#1-skill-trong-chatgpt-là-gì)
2. [Cách tạo một Skill](#2-cách-tạo-một-skill)
   - [2a. Đóng gói một file trong thư viện thành skill](#2a-đóng-gói-một-file-trong-thư-viện-thành-skill)
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

Skill là bộ hướng dẫn để ChatGPT làm một việc lặp lại: khi nào dùng, cần thông tin gì, làm theo bước nào và trả kết quả ra sao. Mỗi skill có tên, mô tả và file chính `SKILL.md`. ChatGPT chỉ đọc tên và dòng mô tả của mọi skill để quyết định dùng skill nào. Khớp thì nó mới mở toàn bộ `SKILL.md` ra làm theo.

**Phân biệt với thư viện này:** 119 file theo mã `MKT-01`, `SAL-01`... là bản hướng dẫn để bạn đọc, điền và dán vào chat. Chúng không tự trở thành skill cài sẵn chỉ vì có chữ "skill" trong tên. Các file này không có khối `name` / `description` ở đầu, nên ChatGPT không biết khi nào gọi.

Muốn ChatGPT tự gọi một file trong thư viện, làm theo mục 2a "Đóng gói một file trong thư viện thành skill", ngay sau mục 2.

## 2. Cách tạo một Skill

Chỉ cần dùng ngay một file trong thư viện thì làm theo [Hướng dẫn sử dụng](HUONG-DAN-SU-DUNG.md): điền bối cảnh, dán vào chat mới, nêu việc cần làm. Không cần tạo skill.

### Làm tay trước, đóng gói sau

Đừng viết skill từ tờ giấy trắng. Làm việc đó bằng tay 3–5 lượt chat trước. Mỗi lần bạn phải nhắc thêm một chỉ dẫn, chỉ dẫn đó là một mục trong skill. Ví dụ: lượt 3 bạn phải nhắc "bóc mọi con số, mốc thời gian, cam kết", thì skill có mục "Số liệu, ngày tháng, hạn chót".

### Ba cách tạo skill

| Cách | Làm thế nào | Hợp khi |
|---|---|---|
| **Create with chat** | Ngay trong chat vừa làm tay, bảo ChatGPT "đóng gói cách làm vừa rồi thành skill". ChatGPT hỏi thêm vài câu rồi đề nghị cài skill. | Người mới; vừa làm tay xong một việc |
| **Create with editor** | Thanh bên → Plugins → tab Skills → Create → Create with editor. Dán nội dung `SKILL.md`. | Đã có sẵn `SKILL.md`, ví dụ đóng gói một file trong thư viện (mục 2a) |
| **Upload from your computer** | Nạp thư mục skill có sẵn trên máy. Skill được quét bảo mật xong mới dùng được. | Nhận skill từ đồng nghiệp hoặc từ thư viện skill mẫu |

Câu lệnh mẫu cho Create with chat, gõ ngay sau khi làm tay xong:

```text
Kết quả ổn rồi. Hãy đóng gói cách làm vừa rồi thành một skill tên tom-tat-tai-lieu,
để lần sau tôi chỉ cần nói "Tóm tắt tài liệu này" là bạn tự dùng skill.
Bước 1 của skill: kiểm tra đủ đầu vào, thiếu thì hỏi lại 1 lần, tối đa 3 câu.
Chỗ tài liệu không có thì ghi "Tài liệu không đề cập", không suy đoán.
```

Đường dẫn tra ngày 05/10/2026, tên menu có thể đổi. Tài khoản không thấy tab Skills thì tạo skill trong plugin bằng `@plugin-creator` (xem trang [Plugin](#plugin/plugin-cach-tao-khong-can-code)).

### Năm bước từ việc lặp lại đến skill

1. Chọn **một việc** lặp lại hằng tuần, ví dụ "viết email nhắc thanh toán". Một skill một việc.
2. Làm tay 3–5 lượt. Ghi lại câu nào bạn phải nhắc thêm.
3. Đóng gói bằng một trong ba cách trên. Soát `SKILL.md` đủ khối `name` / `description` và 6 phần (mục 4, mục 8).
4. Chạy trên 3 việc thật. Sai thì sửa skill, không sửa tay kết quả (mục 6).
5. Làm phép thử cuối: mở phiên mới, không gọi tên skill, giao một yêu cầu skill chưa từng làm. Skill tự được gọi và làm đúng thì đạt.

---

## 2a. Đóng gói một file trong thư viện thành skill

Mọi file trong thư viện có cùng một khung:

- Dòng 1: `# MÃ · Tên`.
- Ba dòng: `> **Dùng khi:**`, `> **Kết quả:**`, `> **Không dùng khi:**`.
- Sáu mục: `## 0. Bối cảnh công ty`, `## 1. Vai trò của bạn`, `## 2. Thu thập thông tin`, `## 3. Nguyên tắc làm việc`, `## 4. Cấu trúc kết quả`, `## 5. Danh sách kiểm tra chất lượng`.

Khung này chuyển thành `SKILL.md` qua 6 bước dưới đây. Ví dụ dùng file `VP-02-tom-tat-tai-lieu.md`.

Trước khi bắt đầu:

- **Không sửa file gốc.** Tạo một file `SKILL.md` mới. File gốc vẫn là bản dán vào chat. Thêm khối `name` / `description` vào file gốc sẽ làm trang web hiện lặp tiêu đề, và nút "Sao chép" dán cả khối này vào chat.
- **Một skill một việc.** File có nhiều đầu ra (ví dụ SAL-01, OPS-03) thì tách mỗi đầu ra thành một skill.
- **Dùng thử trước.** Dán file vào chat, chạy 2–3 việc thật. Câu nào phải nhắc thêm thì ghi lại để đưa vào skill.

### Bước 1. Đặt tên

Tên viết thường, không dấu, nối bằng gạch ngang. Lấy từ tên file, bỏ mã:

```text
VP-02-tom-tat-tai-lieu.md  →  tom-tat-tai-lieu
```

Tạo thư mục cùng tên, trong đó có file `SKILL.md`. Dùng Create with editor thì chỉ cần nội dung `SKILL.md`. Thư mục cần khi nạp bằng Upload from your computer.

### Bước 2. Viết khối `name` / `description`

Dòng đầu `SKILL.md` là khối nằm giữa hai dòng `---`. Ví dụ cho VP-02:

```markdown
---
name: tom-tat-tai-lieu
description: Tóm tắt văn bản dài (hợp đồng, công văn, báo cáo, biên bản, chuỗi email, tài liệu kỹ thuật) thành 5 dòng cho người quản lý, ý chính, số liệu và mốc, điểm rủi ro kèm vị trí, việc cần làm. Dùng khi người dùng nói "tóm tắt tài liệu này", "hợp đồng này có gì cần lưu ý", "công văn này yêu cầu gì, hạn khi nào". Không dùng khi cần rà từng điều khoản để đàm phán (PL-01), làm biên bản từ bản ghi cuộc họp (OPS-03), phân tích nhiều đánh giá của khách (CS-04), rút kết luận từ bảng số (OPS-09).
---
```

Cách ghép `description`:

- **Câu đầu:** skill làm gì. Rút từ dòng `> **Dùng khi:**`, còn 1–2 câu, giữ các loại tình huống.
- **"Dùng khi người dùng nói …":** 2–3 câu người dùng hay gõ. ChatGPT dựa vào phần này để chọn skill.
- **"Không dùng khi …":** chép từ dòng `> **Không dùng khi:**`.
- Viết cả `description` trên một dòng.
- Mã PL-01, OPS-03… là file trong thư viện. File nào cũng đã đóng gói thì thay mã bằng tên skill, ví dụ PL-01 thành `ra-soat-hop-dong`.

### Bước 3. Dán phần thân

Dưới khối `---`, viết tiêu đề là tên việc (dòng 1 của file, bỏ mã). Thêm mục `## Khi nào dùng` viết từ 3 dòng meta. Rồi dán nguyên phần thân từ `## 0.` đến hết file.

```markdown
# Tóm tắt tài liệu, hợp đồng, công văn

## Khi nào dùng
- Hợp đồng mua bán, đại lý, dịch vụ cần nắm điểm rủi ro trước khi trình ký.
- Công văn cơ quan nhà nước cần biết yêu cầu gì, hạn trả lời khi nào.
- Báo cáo, biên bản, chuỗi email dài cần ý chính và việc phải làm trước khi họp.
Không dùng: rà từng điều khoản để đàm phán (PL-01); biên bản từ bản ghi cuộc họp (OPS-03);
phân tích nhiều đánh giá của khách (CS-04); rút kết luận từ bảng số (OPS-09).

## 0. Bối cảnh công ty (điền một lần)
(dán tiếp mục 0 đến mục 5 của file gốc)
```

Dòng `> **Từ ngữ:**` của file gốc (nếu có) chép vào ngay dưới tiêu đề, để giữ nghĩa các chữ viết tắt.

**Mục 0 phải điền xong trước khi cài.** Trong skill không còn chữ `[ĐIỀN]`.

- Skill dùng trong chat thuộc Project của phòng: luật đã có ở Project instructions (từ cấm, chính sách giá) thì ghi `theo Project`.
- Skill gộp vào plugin có file tham chiếu chứa các luật đó: ghi `theo Project` hoặc tên file tham chiếu.
- Còn lại: điền đủ cho phòng.
- Không điền giá vốn, giá thành, công thức, lương, mật khẩu. Skill sẽ được chia sẻ cho người khác.
- Không chép số liệu demo của khóa học (trần chiết khấu, hạn công nợ) vào skill.

### Bước 4. Đối chiếu với 6 phần của chuẩn

| Phần của chuẩn | Lấy từ file thư viện | Việc cần làm khi đóng gói |
|---|---|---|
| Tên | Tên file bỏ mã | Xong ở bước 1 |
| Mô tả | `> **Dùng khi:**` và `> **Không dùng khi:**` | Xong ở bước 2 |
| Khi nào dùng | 3 dòng meta | Xong ở bước 3. Soát lại: ít nhất 3 tình huống và 1 dòng "Không dùng" |
| Đầu vào | `## 2. Thu thập thông tin` | Ghi sau mỗi câu hỏi: "(bắt buộc)" hoặc "(có thì tốt)" |
| Các bước | Câu đầu mục 2, `## 3. Nguyên tắc làm việc`, `## 5. Danh sách kiểm tra chất lượng` | Bước 1 là kiểm đầu vào: câu "Bước đầu tiên: kiểm tra đủ thông tin…" ở đầu mục 2. Bước cuối là tự rà theo danh sách ở mục 5 |
| Đầu ra | `## 4. Cấu trúc kết quả` | Giữ cấu trúc. Chưa có ví dụ đã điền số liệu thì thêm 1 ví dụ |

Với VP-02:

- **Đầu vào:** câu 1 (tài liệu) và câu 2 (mục đích, người đọc) là bắt buộc. Câu 3 (điểm cần soi) và câu 4 (độ dài, mẫu) là có thì tốt.
- **Đầu ra:** mục 4 đã có ví dụ hợp đồng mua đèn LED. Giữ nguyên.

Bốn mục để người khác dùng được (mục 8.7) đã có sẵn trong file thư viện:

- Vai trò: mục 1.
- Ranh giới không được vượt: dòng "Điều cấm hoặc giới hạn" ở mục 0 và mục 3.
- Xử lý khi thiếu dữ liệu: đoạn "Khi đủ thông tin…" ở mục 2 và đoạn "Chống bịa và người duyệt cuối" ở mục 3.
- Tiêu chuẩn đầu ra bằng số: soát mục 4. Chỗ nào còn tả bằng tính từ thì đổi sang số.

### Bước 5. Chạy thử

Cài skill bằng Create with editor hoặc Upload from your computer. Chạy trên 3 việc thật: một yêu cầu bình thường, một yêu cầu thiếu thông tin, một tài liệu có chỗ mâu thuẫn. Ghi lại chỗ phải sửa tay.

**Phép thử cuối:** mở phiên mới, **không gọi tên skill**, giao một yêu cầu skill chưa từng làm. Với VP-02, đính kèm một tài liệu chưa dùng lúc chạy thử và gõ đúng 1 câu:

```text
Tóm tắt tài liệu này.
```

Đạt khi skill tự được gọi và ra đủ các mục. Hỏi thêm một câu tài liệu không có, ví dụ "Giá bán lẻ bao nhiêu?". Đạt khi trả lời "Tài liệu không đề cập", không ra con số.

### Bước 6. Ghi lần sửa

Sai thì sửa skill, không sửa tay kết quả. Mỗi lần sửa, ghi một dòng ở cuối `SKILL.md`:

```text
Sửa lần 1: thêm câu "Tài liệu không đề cập" cho câu hỏi về nội dung tài liệu không có.
Sửa lần 2: thêm điểm soi câu công dụng vượt ranh giới pháp lý trong catalogue.
```

Skill đã qua phép thử thì chia sẻ cho đồng nghiệp, hoặc gộp vào plugin của phòng (mục 7).

---

## 3. Cấu trúc của một Skill

Một skill là một thư mục, ví dụ:

```text
tom-tat-tai-lieu/
│
├── SKILL.md
├── references/
│   └── ...
└── scripts/
    └── ...
```

Trong đó:

- **`SKILL.md`**: file hướng dẫn chính, bắt buộc. Đầu file có khối `name` / `description` nằm giữa hai dòng `---`.
- **`references/`**: tùy chọn, chứa file tham chiếu mà skill cần đọc, ví dụ mẫu báo cáo, định nghĩa chỉ số.
- **`scripts/`**: tùy chọn, chứa script hoặc code phục vụ cách làm.

Một skill đơn giản chỉ cần `SKILL.md`.

---

## 4. Ví dụ file SKILL.md

Ví dụ skill viết email công việc, viết đủ 6 phần. File gần nhất trong thư viện là VP-01.

```markdown
---
name: viet-email-cong-viec
description: Viết và sửa email công việc tiếng Việt. Dùng khi cần email báo giá, nhắc việc, xin duyệt, trả lời đối tác. Không dùng cho tin Zalo gửi khách lẻ (dùng CS-02) và hợp đồng (dùng PL-01).
---

# Viết email công việc

## Khi nào dùng
- Viết mới email báo giá, nhắc việc, xin duyệt gửi cấp trên.
- Trả lời email của đối tác, nhà cung cấp, đại lý.
- Sửa email người dùng đã viết: rút ngắn, đổi xưng hô, thêm hạn trả lời.
Không dùng: tin Zalo gửi khách lẻ (dùng CS-02); hợp đồng (dùng PL-01);
chuỗi email chào hàng gửi hàng loạt (dùng SAL-04).

## Đầu vào
| Thông tin | Mức |
|---|---|
| Người nhận và quan hệ với người gửi (lãnh đạo, đồng nghiệp, đối tác) | Bắt buộc |
| Mục đích email và việc muốn người nhận làm | Bắt buộc |
| Số tiền, ngày, tên riêng phải có trong email | Bắt buộc nếu email nhắc đến |
| Hạn người nhận cần trả lời | Có thì tốt, thiếu ghi [CẦN ĐIỀN] |
| Email cũ cần trả lời; mẫu email của công ty | Có thì tốt |

## Các bước
1. Kiểm tra đủ đầu vào. Thiếu mục bắt buộc thì hỏi lại 1 lần, tối đa 3 câu.
   Không bịa số tiền, ngày, tên.
2. Chọn xưng hô theo người nhận: lãnh đạo gọi "anh/chị", xưng "em";
   đối tác gọi "Quý công ty", xưng "chúng tôi".
3. Viết tiêu đề dưới 15 chữ, nêu việc và hạn.
4. Câu đầu nói mục đích. Mỗi ý một gạch đầu dòng, tối đa 5 gạch.
5. Đúng một lời đề nghị người nhận làm gì, kèm hạn.
6. Giữ nguyên số, ngày, tên người dùng đưa. Chỗ chưa có ghi [CẦN ĐIỀN: ...].
7. Tự rà 6 điểm: thân email dưới 120 chữ; câu dưới 20 chữ; không emoji;
   xưng hô đúng bước 2; có hạn trả lời; không có số nào ngoài đầu vào.
8. Kết thúc bằng dòng: "Đây là bản nháp. Người duyệt kiểm lại số liệu, tên riêng
   và từ ngữ trước khi gửi."

## Đầu ra
Tiêu đề, thân email, chữ ký. Sau đó 1 dòng ghi chú cho người gửi: số nào lấy từ
đầu vào ([DATA THẬT]), chỗ nào còn [CẦN ĐIỀN]. Cuối cùng là dòng bản nháp.

Ví dụ mẫu (xin duyệt chi phí, số liệu giả định):

Tiêu đề: Xin duyệt 18.400.000 đ in tờ rơi trước 17h ngày 10/10

Kính gửi anh Tuấn,

Em xin anh duyệt chi phí in 2.000 tờ rơi cho hội chợ ngày 25/10.
- Em đã lấy 3 báo giá. Chọn nhà in B: 18.400.000 đ, giao sau 7 ngày.
- Nhà in A rẻ hơn 1.200.000 đ nhưng giao sau 12 ngày, không kịp hội chợ.
- Ngân sách hội chợ còn 42.000.000 đ, đủ cho khoản này.

Anh duyệt giúp em trước 17h ngày 10/10 để kịp đặt in. Bảng so sánh 3 báo giá em gửi kèm.

Trân trọng,
Lan, phòng Marketing, [CẦN ĐIỀN: số điện thoại]

Ghi chú cho người gửi: 3 báo giá và số ngân sách lấy từ thông tin bạn đưa [DATA THẬT];
còn thiếu số điện thoại.
Đây là bản nháp. Người duyệt kiểm lại số liệu, tên riêng và từ ngữ trước khi gửi.
```

### Vai trò của `name` và `description`

```text
name: viet-email-cong-viec
description: Viết và sửa email công việc tiếng Việt. Dùng khi cần email báo giá, nhắc việc, xin duyệt, trả lời đối tác. Không dùng cho tin Zalo gửi khách lẻ (dùng CS-02) và hợp đồng (dùng PL-01).
```

ChatGPT dùng skill theo 4 bước:

1. Bạn gõ yêu cầu, ví dụ "Viết email xin sếp duyệt chi phí in tờ rơi".
2. ChatGPT **chỉ đọc tên và dòng `description`** của mọi skill đang có.
3. Thấy skill nào khớp, ChatGPT mới mở toàn bộ `SKILL.md` của skill đó.
4. ChatGPT làm đúng từng bước, kể cả bước hỏi lại khi thiếu thông tin.

Dòng `description` mơ hồ thì skill viết hay cỡ nào cũng không được gọi. Phần thân `SKILL.md` chứa các bước, quy tắc và đầu ra.

---

## 5. Cách sử dụng Skill

Sau khi skill đã cài, có hai cách dùng.

### Cách 1: Để ChatGPT tự chọn skill

Bạn đưa yêu cầu bình thường, ví dụ:

```text
Viết giúp tôi email xin khách hàng dời cuộc họp sang thứ Sáu.
```

Nếu dòng `description` của skill `viet-email-cong-viec` khớp yêu cầu, ChatGPT tự mở skill và làm theo các bước.

### Cách 2: Chủ động gọi skill

Gõ `@` rồi chọn skill trước khi đưa yêu cầu.

Cách này hữu ích khi:

- Có nhiều skill làm việc gần giống nhau.
- Bạn muốn chắc chắn một cách làm cụ thể được áp dụng.
- Bạn đang chạy thử các bước của một skill mới.
- Bạn muốn so sánh kết quả có và không có skill.

Phép thử cuối của skill thì ngược lại: **không gọi tên skill**. Skill phải tự được gọi.

---

## 6. Cách chỉnh sửa Skill

Mở `SKILL.md` của skill và sửa trực tiếp. Hoặc mô tả thay đổi bằng lời trong chat, rồi đọc lại bản đã sửa trước khi dùng.

**Sai thì sửa skill, không sửa tay kết quả.** Sửa tay thì lần sau lại sai y như cũ. Mỗi lần sửa, ghi một dòng "Sửa lần N: …" ở cuối file.

Quy tắc sửa phải tả bằng hành vi, không tả bằng tính từ:

| Tả bằng tính từ (chưa dùng được) | Tả bằng hành vi (dùng được) |
|---|---|
| Gửi lãnh đạo thì trang trọng hơn | Gửi lãnh đạo: mở bằng "Kính gửi anh/chị", xưng "em", câu dưới 20 chữ |
| Gửi đồng nghiệp thì thân thiện hơn | Gửi đồng nghiệp: xưng "mình", thân email tối đa 80 chữ |
| Lời kêu gọi phải rõ ràng | Đúng một lời đề nghị người nhận làm gì, kèm hạn |

Ví dụ câu lệnh sửa:

```text
Sửa skill viet-email-cong-viec của tôi.

Thay quy tắc xưng hô ở bước 2 bằng:
- Gửi lãnh đạo: mở bằng "Kính gửi anh/chị", xưng "em", câu dưới 20 chữ.
- Gửi đồng nghiệp: xưng "mình", thân email tối đa 80 chữ.
- Không dùng emoji trừ khi tôi yêu cầu.

Thêm vào bước tự rà: có đúng một lời đề nghị người nhận làm gì, kèm hạn.
Ghi cuối file: "Sửa lần 1: xưng hô và độ dài theo người nhận."
Cho tôi xem bản đã sửa trước khi lưu.
```

Vòng cải tiến một skill:

```text
Chạy skill trên 3 việc thật
   ↓
Ghi lại chỗ phải sửa tay
   ↓
Sửa vào skill, không sửa tay kết quả
   ↓
Ghi "Sửa lần N" ở cuối file
   ↓
Chạy lại, làm phép thử phiên mới
```

Không cần viết skill đúng ngay lần đầu. Chạy trên việc thật mới lộ ra quy tắc còn thiếu.

---

## 7. Phân biệt Skill và Plugin

> **Skill dạy ChatGPT làm đúng. Plugin cho ChatGPT với tới dữ liệu thật.**

Ví dụ skill phân tích báo cáo:

```text
Đếm số dòng, các cột của file
→ đối chiếu tổng với file gốc
→ so với kỳ trước
→ tìm biến động lớn
→ viết nguyên nhân dạng "nghi do …, cần kiểm chứng bằng …"
→ báo cáo 1 trang cho người quản lý
```

Skill chỉ làm việc trên thứ bạn dán hoặc tải vào chat. Muốn ChatGPT tự đọc file trên Drive hay soạn thư trong Gmail thì cần plugin.

Plugin tự tạo của phòng gồm 3 thành phần: **Skill + file tham chiếu + App**.

| Thành phần | Trong plugin là | Ví dụ "Plugin báo cáo bán hàng tuần" |
|---|---|---|
| **Skill** | Quy trình | `bao-cao-ban-hang` (SAL-12 đã đóng gói), `tom-tat-tai-lieu` (VP-02 đã đóng gói) |
| **File tham chiếu** | Tài liệu nguồn sự thật | Mẫu báo cáo tuần, định nghĩa chỉ số, playbook |
| **App** | Chìa khóa | Google Drive để đọc file đơn hàng; Gmail ở mức Always ask để soạn nháp thư gửi lãnh đạo |

```text
Plugin: Báo cáo bán hàng tuần
├── Skills
│   ├── bao-cao-ban-hang
│   └── tom-tat-tai-lieu
├── File tham chiếu
│   ├── mau-bao-cao-tuan.md
│   ├── dinh-nghia-chi-so.md
│   └── playbook.md
└── Apps
    ├── Google Drive
    └── Gmail (mức Always ask)
```

Có thể ghi nhớ ngắn gọn:

- **Skill** dạy ChatGPT **cách làm**.
- **App** (trước 12/2025 gọi là Connector) cho ChatGPT **dữ liệu và hành động**: đọc file trên Drive, soạn thư trong Gmail.
- **Plugin** gói Skill + file tham chiếu + App thành bộ công cụ của phòng. Người khác cài vào là làm được.

Skill chưa chuẩn thì plugin chỉ nhân bản cái sai nhanh hơn. Đóng gói và chạy thử skill trước, gộp vào plugin sau. Cách tạo plugin, mức quyền và cách chia sẻ: xem trang [Plugin](#plugin).

---

## 8. Công thức thiết kế Skill hiệu quả

Một `SKILL.md` có khối `name` / `description` ở đầu (bắt buộc) và 6 phần. Viết đủ 6 phần là có bản đầu tiên.

| Phần | Trả lời câu hỏi | Tiêu chuẩn |
|---|---|---|
| 1. Tên | Skill gọi là gì? | Viết thường, không dấu, nối gạch ngang. Đặt ở dòng `name` |
| 2. Mô tả | Skill làm gì? | Một câu, đặt đầu dòng `description`. Tiếp theo là "Dùng khi …" và "Không dùng …" |
| 3. Khi nào dùng | Gặp tình huống nào thì dùng? | Ít nhất 3 tình huống, và khi nào không dùng |
| 4. Đầu vào | Cần thông tin gì? | Tách 2 mức: bắt buộc và có thì tốt |
| 5. Các bước | Làm theo thứ tự nào? | Bước 1 kiểm đủ đầu vào, thiếu thì hỏi lại 1 lần, tối đa 3 câu. Bước cuối tự rà |
| 6. Đầu ra | Kết quả trông thế nào? | Cấu trúc cố định, kèm 1 ví dụ đã điền số liệu |

Ví dụ ở các mục dưới dùng skill `phan-tich-bao-cao-kinh-doanh` (bản đầy đủ ở mục 9).

### 8.1 Tên

| Chưa dùng được | Dùng được |
|---|---|
| `Phân tích báo cáo`, `business-report-analyzer`, `skill-1` | `phan-tich-bao-cao-kinh-doanh` |

### 8.2 Mô tả và dòng `description`

ChatGPT chỉ đọc tên và `description` để quyết định gọi skill. Viết "Dùng khi …", liệt kê tình huống và câu người dùng hay nói, ghi cả lúc không dùng.

| Chưa dùng được | Dùng được |
|---|---|
| `description: Phân tích báo cáo.` | `description: Phân tích file doanh thu, đơn hàng (Excel, CSV, PDF) thành báo cáo 1 trang cho lãnh đạo. Dùng khi người dùng tải file lên và nói "phân tích giúp", "viết báo cáo tháng", "tháng này tăng giảm thế nào". Không dùng cho báo cáo tài chính quản trị và báo cáo marketing.` |
| Quá chung: skill bị gọi nhầm hoặc không bao giờ được gọi | Nêu việc, tình huống, câu người dùng hay nói, và lúc không dùng |

### 8.3 Khi nào dùng

```text
KHI NÀO DÙNG:
- Tải file doanh thu hoặc đơn hàng tháng lên, cần báo cáo cho lãnh đạo.
- So kết quả kỳ này với kỳ trước hoặc với mục tiêu.
- Tìm sản phẩm, kênh tăng hoặc giảm bất thường.
Không dùng: báo cáo tài chính quản trị; báo cáo marketing; chỉ cần làm sạch bảng tính.
```

### 8.4 Đầu vào

| Thông tin | Mức |
|---|---|
| File báo cáo | Bắt buộc |
| Kỳ dữ liệu (tháng, quý) | Bắt buộc |
| Người đọc báo cáo | Bắt buộc |
| Mục tiêu kỳ này; số kỳ trước | Có thì tốt, thiếu ghi `[CẦN ĐIỀN]` |
| Mẫu báo cáo của công ty | Có thì tốt |

Thiếu mục bắt buộc thì hỏi lại. Thiếu mục có thì tốt thì ghi `[CẦN ĐIỀN: ...]` tại chỗ đó và làm tiếp.

### 8.5 Các bước

Bước 1 luôn là kiểm đủ đầu vào. Bước cuối luôn là tự rà. Ở giữa, mỗi bước là một hành động kiểm được: "phân tích kỹ" chưa dùng được; "so từng sản phẩm với kỳ trước, nêu 3 sản phẩm giảm nhiều nhất" dùng được.

Quy tắc chống bịa đặt ngay trong các bước:

```text
CÁC BƯỚC:
1. Kiểm tra đủ đầu vào. Thiếu mục bắt buộc thì hỏi lại 1 lần, tối đa 3 câu.
...
QUY TẮC (áp dụng ở mọi bước):
- Không bịa số liệu. Số lấy từ file ghi [DATA THẬT].
- Số tự suy ra hoặc dùng giả định ghi [SUY LUẬN].
- Thiếu dữ liệu thì ghi [CẦN ĐIỀN: cần gì] tại chỗ đó, vẫn trả phần làm được.
- Không kết luận nguyên nhân khi dữ liệu không chứng minh được.
  Viết dạng "nghi do …, cần kiểm chứng bằng …".
...
Bước cuối. Tự rà: tổng khớp file gốc; không có chiều phân tích ngoài các cột của file;
mọi số quan trọng đã gắn nhãn. Kết thúc bằng: "Đây là bản nháp. Người duyệt kiểm lại
số liệu, tên riêng và từ ngữ trước khi gửi."
```

### 8.6 Đầu ra

Ghi rõ kết quả cần giao. Chỉ xuất phần người dùng yêu cầu. Người dùng đưa mẫu công ty thì dùng mẫu đó trước.

```text
ĐẦU RA (1 trang, đọc trong 2 phút):
1. Tóm tắt kết luận: 3 dòng, có số.
2. Chỉ số chính: bảng theo sản phẩm và theo kênh, có % tổng.
3. Điểm đang tốt: 1 điểm, có số.
4. Vấn đề cần xử lý: 1–2 điểm, có số.
5. Nguyên nhân nghi ngờ và cách kiểm chứng.
6. Việc nên làm tiếp: 2–3 đề xuất.
7. Số liệu người ký cần kiểm lại trước khi trình.

Ví dụ đã điền: "Từ 01/07 đến 25/07 đạt 147.300.000 đ trên 40 đơn [DATA THẬT].
Kênh đại lý sỉ 7 đơn, chiếm 72,4% doanh thu [DATA THẬT]. Nghi do phụ thuộc vài đại lý
lớn, cần kiểm chứng bằng danh sách khách của 7 đơn sỉ [SUY LUẬN]."
```

Ví dụ đã điền giúp định dạng giữ nguyên giữa các lần chạy. Thiếu ví dụ thì mỗi lần ra một kiểu.

### 8.7 Bốn mục để người khác dùng được

Muốn đồng nghiệp cầm skill lên chạy mà không cần hỏi lại, skill phải có thêm 4 mục:

| Mục | Ví dụ cho `phan-tich-bao-cao-kinh-doanh` | Ở file thư viện nằm tại |
|---|---|---|
| **Vai trò** | "Đọc số như kế toán quản trị: đếm và đối chiếu trước, nhận định sau" | `## 1. Vai trò của bạn` |
| **Tiêu chuẩn đầu ra bằng số** | "Báo cáo 1 trang, đọc trong 2 phút; 1 điểm sáng, 1 điểm cần chú ý; 2–3 đề xuất, mỗi đề xuất đủ 4 thứ" | `## 4. Cấu trúc kết quả` |
| **Ranh giới không được vượt** | "Không tách theo cột file không có. Không quy trách nhiệm cho cá nhân. Không tự quyết ngân sách, ghi 'cần người phụ trách duyệt'" | Dòng "Điều cấm hoặc giới hạn" ở mục 0; `## 3. Nguyên tắc làm việc` |
| **Xử lý khi thiếu dữ liệu** | "Ghi `[CẦN ĐIỀN: cần gì]` tại chỗ đó, ghi rõ cần bổ sung gì, vẫn trả phần đã làm được" | Đoạn "Khi đủ thông tin…" ở mục 2 |

---

## 9. Ví dụ Skill phân tích báo cáo kinh doanh

Câu lệnh tạo skill bằng Create with chat. Dán sau khi đã làm tay vài lượt với file báo cáo của bạn:

```text
Hãy tạo cho tôi skill tên phan-tich-bao-cao-kinh-doanh.

MÔ TẢ: Phân tích file doanh thu, đơn hàng (Excel, CSV, PDF) thành báo cáo 1 trang cho lãnh đạo.
Dùng khi tôi tải file lên và nói "phân tích giúp", "viết báo cáo tháng".
Không dùng cho báo cáo tài chính quản trị và báo cáo marketing.

KHI NÀO DÙNG:
- Tải file doanh thu hoặc đơn hàng tháng lên, cần báo cáo cho lãnh đạo.
- So kết quả kỳ này với kỳ trước hoặc với mục tiêu.
- Tìm sản phẩm, kênh tăng hoặc giảm bất thường.

ĐẦU VÀO:
- Bắt buộc: file báo cáo; kỳ dữ liệu; người đọc báo cáo.
- Có thì tốt: mục tiêu kỳ này; số kỳ trước; mẫu báo cáo của công ty. Thiếu thì ghi [CẦN ĐIỀN].

CÁC BƯỚC:
1. Kiểm tra đủ đầu vào. Thiếu mục bắt buộc thì hỏi lại 1 lần, tối đa 3 câu.
2. Đếm trước: báo file có bao nhiêu dòng, những cột nào, từ ngày nào đến ngày nào.
   Chưa đếm xong thì chưa phân tích.
3. Chỉ phân tích theo cột file có. File không có cột nhân viên thì không tách theo nhân viên.
4. Đối chiếu tổng: tổng tự tính phải khớp file gốc. Lệch thì liệt kê dòng lệch trước.
5. So với kỳ trước hoặc mục tiêu. Nêu sản phẩm, kênh tăng giảm nhiều nhất, kèm số.
6. Nguyên nhân viết dạng "nghi do …, cần kiểm chứng bằng …". Không quy trách nhiệm cho cá nhân.
7. Gắn nhãn: số lấy từ file ghi [DATA THẬT]; tự suy ra ghi [SUY LUẬN]; chưa có ghi [CẦN ĐIỀN].
8. Tự rà: tổng khớp file; không có chiều phân tích ngoài cột của file; mỗi đề xuất đủ
   việc cần làm, người chịu trách nhiệm, hạn, nguồn lực hoặc chi phí.
   Kết thúc bằng: "Đây là bản nháp. Người duyệt kiểm lại số liệu, tên riêng và từ ngữ trước khi gửi."

ĐẦU RA (1 trang, đọc trong 2 phút):
1. Tóm tắt kết luận
2. Chỉ số chính
3. Điểm đang tốt
4. Vấn đề cần xử lý
5. Nguyên nhân nghi ngờ và cách kiểm chứng
6. Việc nên làm tiếp
7. Số liệu người ký cần kiểm lại trước khi trình
Ví dụ dòng đã điền: "Kênh đại lý sỉ 7 đơn, chiếm 72,4% doanh thu. Nghi do phụ thuộc
vài đại lý lớn, cần kiểm chứng bằng danh sách khách của 7 đơn sỉ."
```

Chạy thử với file [don-hang-demo.xlsx](du-lieu-demo/don-hang-demo.xlsx). Đạt khi:

- Báo 40 dòng đơn hàng, tổng 147.300.000 đ trước khi phân tích.
- Không có bảng theo nhân viên, vì file không có cột này.
- Có mục "Số liệu người ký cần kiểm lại trước khi trình".

### Vì sao cấu trúc này hữu ích?

Nó tách rõ:

- Dòng mô tả để ChatGPT biết khi nào gọi skill.
- Đầu vào bắt buộc và đầu vào có thì tốt.
- Bốn quy tắc số liệu: đếm trước; chỉ theo cột file có; đối chiếu tổng; nguyên nhân là suy đoán, có cách kiểm chứng.
- Cấu trúc đầu ra, có ví dụ đã điền.
- Nhãn chống bịa và bước tự rà.

Nhờ vậy skill dễ đọc, dễ sửa và dễ chạy thử.

### Nên tạo Skill nhỏ hay Skill lớn?

Một skill một việc. Đừng gộp mọi quy trình của công ty vào một skill như:

```text
tat-ca-viec-cong-ty
```

Hãy tách thành:

```text
bao-cao-doanh-so
viet-email-cong-viec
ghi-chu-hop
phan-tich-phan-hoi-khach
bao-cao-tuan
```

Các skill nối thành chuỗi: đầu ra của skill trước là đầu vào của skill sau. Ví dụ bảng đầu việc của `ghi-chu-hop` là đầu vào cho `viet-email-cong-viec` soạn email nhắc việc. Còn mục `[CẦN ĐIỀN]` thì chưa chạy sang skill sau.

---

## 10. Quy trình tổng thể

Vòng đời của một skill:

```text
Việc lặp lại hằng tuần
   ↓
Làm tay 3–5 lượt, ghi câu phải nhắc thêm
   ↓
Đóng gói: Create with chat / Create with editor / Upload from your computer
   ↓
SKILL.md: khối name, description và 6 phần
   ↓
Chạy trên 3 việc thật
   ↓
Sai thì sửa skill, ghi "Sửa lần N"
   ↓
Phép thử cuối: phiên mới, không gọi tên skill, yêu cầu chưa từng làm
   ↓
Dùng hằng ngày; cần app thì gộp vào plugin của phòng
```

Một quy trình thực tế:

1. Chọn một việc bạn làm hằng tuần.
2. Làm tay 3–5 lượt, ghi lại câu phải nhắc thêm.
3. Viết bản đầu tiên của `SKILL.md` đủ 6 phần (mục 8), hoặc đóng gói một file trong thư viện (mục 2a).
4. Chạy trên 3 việc thật: một việc bình thường, một việc thiếu dữ liệu, một việc dữ liệu mâu thuẫn.
5. Ghi chỗ phải sửa tay. Sửa vào skill, ghi "Sửa lần N".
6. Chạy lại đến khi qua phép thử cuối.
7. Chia sẻ cho đồng nghiệp, hoặc gộp vào plugin của phòng.

### Danh sách kiểm tra trước khi hoàn thành skill

- [ ] Tên viết thường, không dấu, nối gạch ngang.
- [ ] Đầu file có khối `name` / `description` nằm giữa hai dòng `---`.
- [ ] `description` có việc skill làm, "Dùng khi …" kèm câu người dùng hay nói, và "Không dùng …".
- [ ] Khi nào dùng có ít nhất 3 tình huống và ít nhất 1 trường hợp không dùng.
- [ ] Đầu vào tách 2 mức: bắt buộc và có thì tốt.
- [ ] Bước 1 kiểm đủ đầu vào; thiếu thì hỏi lại 1 lần, tối đa 3 câu.
- [ ] Tiêu chuẩn đầu ra viết bằng số hoặc hành vi, không bằng tính từ.
- [ ] Có ranh giới không được vượt.
- [ ] Có nhãn chống bịa: `[DATA THẬT]`, `[SUY LUẬN]`, `[CẦN ĐIỀN]`.
- [ ] Bước cuối tự rà, kết thúc bằng câu "Đây là bản nháp …".
- [ ] Đầu ra có 1 ví dụ đã điền số liệu.
- [ ] Đã chạy với việc bình thường, việc thiếu dữ liệu và việc dữ liệu mâu thuẫn.
- [ ] Qua phép thử cuối: phiên mới, không gọi tên skill, yêu cầu chưa từng làm.
- [ ] Mỗi lần sửa có một dòng "Sửa lần N" ở cuối file.

---

## 11. Tài liệu tham khảo

Nguồn chính thức (tra ngày 05/10/2026):

- [learn.chatgpt.com – Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI Help – Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [OpenAI Developers – Skills concepts](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI Developers – Build skills](https://developers.openai.com/plugins/build/skills)

Bài học tương ứng trên trang này: [Skill](#skill) và [Plugin](#plugin).

> **Lưu ý:** Tính năng, tên menu và loại tài khoản được hỗ trợ có thể thay đổi. Trước khi triển khai, kiểm tra tài liệu OpenAI mới nhất.

---

## Mẫu khung SKILL.md để tái sử dụng

Sao chép mẫu dưới đây để bắt đầu skill mới. Thay các chỗ trong ngoặc vuông.

```markdown
---
name: ten-viec-viet-thuong-khong-dau
description: Làm gì, trong một câu. Dùng khi [tình huống], khi người dùng nói "[câu hay gõ]". Không dùng khi [trường hợp] (dùng [skill khác]).
---

# [Tên việc]

Vai trò: [ví dụ "đọc số như kế toán quản trị: đếm và đối chiếu trước, nhận định sau"]

## Khi nào dùng
- [Tình huống 1]
- [Tình huống 2]
- [Tình huống 3]
Không dùng: [trường hợp] (dùng [skill khác]).

## Đầu vào
| Thông tin | Mức |
|---|---|
| [Thông tin 1] | Bắt buộc |
| [Thông tin 2] | Bắt buộc |
| [Thông tin 3] | Có thì tốt, thiếu ghi [CẦN ĐIỀN] |

## Các bước
1. Kiểm tra đủ đầu vào. Thiếu mục bắt buộc thì hỏi lại 1 lần, tối đa 3 câu.
   Không bịa số liệu, tên, ngày.
2. [Bước làm việc, viết bằng hành động kiểm được]
3. [Bước làm việc]
4. Ranh giới: [điều không được tự quyết]. Gặp thì ghi "cần xác nhận với người phụ trách".
5. Gắn nhãn: lấy từ tài liệu ghi [DATA THẬT]; tự suy ra ghi [SUY LUẬN];
   chưa có ghi [CẦN ĐIỀN: cần gì], vẫn trả phần làm được.
6. Tự rà: [3–6 điểm kiểm được, ví dụ "dưới 150 chữ", "không có số nào ngoài đầu vào"].
   Kết thúc bằng: "Đây là bản nháp. Người duyệt kiểm lại số liệu, tên riêng và từ ngữ
   trước khi gửi."

## Đầu ra
[Cấu trúc cố định: các mục, độ dài bằng số]

Ví dụ mẫu (đã điền số liệu):
[Một kết quả đạt, có số thật hoặc số giả định ghi rõ]

Sửa lần 1: [ngày], [sửa gì, vì sao]
```

Mẫu này dùng được cho nhiều loại việc: nghiên cứu thị trường, viết nội dung, phân tích bảng tính, viết email, làm báo cáo, phân tích tài chính.
