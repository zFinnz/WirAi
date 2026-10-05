# Hướng dẫn sử dụng bộ kỹ năng

Mỗi file là một bản hướng dẫn công việc để bạn dán vào ChatGPT. Bạn không cần biết lập trình hay cài thêm tính năng. Điền phần bối cảnh, dán file, rồi nói rõ mình cần kết quả gì.

---

## 1. Chọn đúng skill

1. Tìm nhóm phòng ban của bạn.
2. Đọc cột **Dùng khi**. Chọn skill khớp với việc bạn đang cần làm, không chọn theo tên.
3. Nếu việc của bạn cần 2 skill (ví dụ viết mô tả công việc rồi sàng lọc hồ sơ), dùng lần lượt trong 2 chat: kết quả của skill trước dán vào làm đầu vào cho skill sau. Còn mục `[CẦN ĐIỀN]` thì điền xong mới chạy skill sau.
4. Không biết chọn skill nào: đọc cột **Dùng khi** của nhóm phòng ban mình, hoặc gõ việc đang cần làm vào ô tìm kiếm trong `index.html`.

---

## 2. Điền bối cảnh công ty

Mỗi file có phần **0. Bối cảnh công ty** ở đầu với các dòng `[ĐIỀN: ...]`. Hãy điền trước khi dán vào AI. Phần này giúp AI không hỏi lại những điều ai cũng biết trong công ty.

Ví dụ trước khi điền:

```
- Tên công ty và ngành: [ĐIỀN: ví dụ "Công ty ABC, phân phối thiết bị điện dân dụng"]
- Sản phẩm, dịch vụ chính: [ĐIỀN]
- Khách hàng chính: [ĐIỀN: B2C qua sàn và cửa hàng, B2B qua đại lý]
```

Sau khi điền:

```
- Tên công ty và ngành: Công ty ABC, phân phối thiết bị điện dân dụng
- Sản phẩm, dịch vụ chính: ổ cắm, công tắc, đèn LED thương hiệu riêng
- Khách hàng chính: B2C qua Shopee và 3 cửa hàng, B2B qua 40 đại lý miền Nam
```

Dòng không liên quan thì ghi `không áp dụng`; dòng chưa biết thì ghi `chưa rõ` để bổ sung sau. Không để nguyên chữ `[ĐIỀN]`.

**Lưu ý bảo mật:** không dán 5 loại: giá vốn, giá thành, công thức; hợp đồng có điều khoản bảo mật; thông tin cá nhân nhân viên (lương, CCCD); mật khẩu, tài khoản; tài liệu đóng dấu MẬT. Thay tên thật bằng "khách hàng A", "HĐ số X" trước khi dán. Nội dung nhạy cảm dùng Temporary Chat. Tắt *Improve the model for everyone* trong Settings → Data controls.

---

## 3. Dùng trên ChatGPT

### Cách 1: dùng ngay (mặc định)

1. Mở một cuộc trò chuyện mới.
2. Mở file đã điền bối cảnh, sao chép toàn bộ nội dung và dán vào tin nhắn đầu tiên.
3. Cuối tin nhắn, thêm yêu cầu cụ thể, ví dụ: "Chỉ viết một email nhắc thanh toán, xưng 'em', tối đa 120 từ, không emoji".

### Cách 2: trong Project của phòng

- Luật chung của phòng (giọng văn, từ cấm, chính sách giá, dữ liệu không được dán) đặt ở Project instructions.
- Mở chat trong Project đó rồi dán template. Ô nào ở mục 0 đã có trong Project thì ghi `theo Project`.
- Không dán cả template vào Project instructions. Instructions chỉ giữ điều đúng cho mọi việc; nhồi quy trình chi tiết vào đó là lỗi hay gặp của khóa học.

### Cách 3: để ChatGPT tự gọi

Đóng gói file thành skill theo [hướng dẫn tạo skill](huong-dan-tao-skill-chatgpt.md), mục "Đóng gói một file trong thư viện thành skill". Bản trong thư viện chưa có khối `name` / `description` nên chưa tự được gọi.

**Dùng ở Wir:** tạo Project theo mẫu 2.2 (Marketing) hoặc 2.3 (Kinh doanh sỉ) của khóa học, nạp `du-lieu-san-pham-wir.md` vào Files, rồi dán template vào chat trong Project đó. Số liệu demo của khóa học không chép vào template.

---

## 4. Cách nêu yêu cầu để kết quả tốt

Skill kiểm tra đủ thông tin trước, thiếu thông tin quan trọng thì hỏi lại 1 lần, tối đa 3 câu. Bạn có thể cung cấp bối cảnh ngay trong yêu cầu đầu tiên để có kết quả sát hơn. Ví dụ với skill kế hoạch marketing:

> Lập kế hoạch marketing quý 4 cho dòng đèn LED. Mục tiêu doanh thu 2 tỷ, ngân sách marketing 150 triệu, kênh đang chạy là Shopee và Facebook, giai đoạn tăng trưởng.

Khi đã đủ thông tin, skill sẽ làm ngay. Nếu kết quả chưa đúng hướng, bạn có thể nêu điểm cần chỉnh và yêu cầu sửa phần đó.

Mẹo:

- **Dán biểu mẫu công ty đang dùng** nếu có (mẫu báo cáo, bảng theo dõi, cấu trúc văn bản). Skill sẽ làm theo đúng mẫu đó thay vì cấu trúc mặc định.
- **Chỉ rõ phần cần làm.** Ví dụ "chỉ viết tin nhắn đầu tiên" hoặc "chỉ sửa bảng ngân sách"; bạn không phải nhận toàn bộ các mục của skill.
- **Sửa các quy tắc trong file nếu cần.** Phần 0 là bối cảnh công ty; phần 2 là thông tin AI cần hỏi; phần 3 là cách làm; phần 4 là mẫu kết quả; phần 5 là danh sách tự kiểm tra. Dòng **Từ ngữ** giải thích chữ viết tắt và thuật ngữ hay gặp.
- **Chỗ ghi `[CẦN ĐIỀN: ...]`** trong kết quả là dữ liệu AI không có và không bịa. **`[DATA THẬT]`** là số lấy từ tài liệu bạn đưa; **`[SUY LUẬN]`** là chỗ AI tự suy ra hoặc dùng số giả định của mẫu. Bạn điền số thật vào hoặc cung cấp thêm rồi yêu cầu cập nhật.
- **Đưa số liệu thật** nếu được phép chia sẻ. Có số, AI tính được; không có số, AI chỉ nói chung chung.
- **Nói rõ người đọc kết quả** là ai: giám đốc, trưởng phòng hay nhân viên mới. Skill sẽ điều chỉnh độ dài và ngôn ngữ.
- **Yêu cầu sửa theo phần.** Kết quả nào có nhiều phần, hãy nói "sửa lại phần 3, giữ nguyên các phần khác" thay vì làm lại từ đầu.
- **Kiểm tra lại số liệu** AI đưa ra. Mức tham khảo trong skill chỉ là gợi ý; cần xem nguồn, thời điểm và mức phù hợp với công ty trước khi dùng. Số tham khảo trong mẫu là giả định, AI phải ghi `[SUY LUẬN]` khi dùng.
- **Mọi kết quả là bản nháp.** Bạn là người duyệt cuối và tự bấm gửi.

---

## 5. Khi kết quả chưa tốt

| Hiện tượng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| AI trả lời chung chung | Phần bối cảnh để trống hoặc yêu cầu thiếu số | Điền bối cảnh, bổ sung mục tiêu và số liệu |
| AI hỏi lại thông tin đã có | Chưa dùng hết bối cảnh bạn cung cấp | Nhắc AI dùng dữ liệu trong yêu cầu và làm ngay nếu đã đủ |
| Kết quả không đúng ý | Yêu cầu đầu ra chưa đủ cụ thể | Nêu rõ phần cần làm, người đọc và mẫu công ty nếu có; chỉ yêu cầu theo phần 4 khi bạn muốn bản đầy đủ |
| Dùng thuật ngữ tiếng Anh nhiều | Đặc thù công cụ | Nhắc "viết tiếng Việt, thuật ngữ kèm tiếng Anh trong ngoặc" |
| Số liệu lạ, không có nguồn | AI tự bịa | Hỏi "Chỗ nào bạn tự suy đoán mà tài liệu không nói?"; rà 2–3 số với nguồn; Ctrl+F câu trích dẫn trong tài liệu gốc |

---

## 6. Đóng góp skill mới

Phòng ban nào có quy trình riêng muốn đóng gói thành skill, viết theo đúng mẫu của các skill hiện có (mở một skill cùng nhóm để tham khảo bố cục) hoặc xem hướng dẫn tạo skill trên ChatGPT trong trang `index.html`. Skill mới cần:

- Đúng bố cục 6 phần như mọi skill khác.
- Viết đủ các bước cần thiết nhưng bỏ phần lặp, phần không giúp AI làm đúng việc; 150 đến 250 dòng chỉ là khoảng tham khảo của thư viện này.
- Có phần bối cảnh công ty với các dòng `[ĐIỀN]`.
- Có đoạn "Chống bịa và người duyệt cuối" ở mục 3 và 2 dòng kiểm tra cuối như các file khác.
- Dùng độc lập; nếu nhắc đến skill khác, chỉ coi đó là gợi ý cho việc liên quan.
- Đặt tên file theo mã phòng ban và số thứ tự kế tiếp.

Gửi file cho người quản lý bộ skill để rà soát trước khi đưa vào thư mục chung.
