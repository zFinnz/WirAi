# Hướng dẫn sử dụng bộ kỹ năng

Mỗi file là một bản hướng dẫn công việc để bạn sao chép vào công cụ AI. Bạn không cần biết lập trình hay cài thêm tính năng. Điền phần bối cảnh, dán file, rồi nói rõ mình cần kết quả gì.

---

## 1. Chọn đúng skill

1. Tìm nhóm phòng ban của bạn.
2. Đọc cột **Dùng khi**. Chọn skill khớp với việc bạn đang cần làm, không chọn theo tên.
3. Nếu việc của bạn cần 2 skill (ví dụ viết mô tả công việc rồi sàng lọc hồ sơ), tạo 2 skill riêng và dùng lần lượt. Kết quả của skill trước dán vào làm đầu vào cho skill sau.
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

**Lưu ý bảo mật:** không điền số liệu tài chính nhạy cảm, thông tin khách hàng cụ thể, mật khẩu hay tài liệu mật vào công cụ AI công cộng. Dùng số làm tròn hoặc số giả định khi cần.

---

## 3. Dùng trên từng công cụ

### ChatGPT

1. Mở một cuộc trò chuyện mới.
2. Mở file đã điền bối cảnh, sao chép toàn bộ nội dung và dán vào tin nhắn đầu tiên.
3. Cuối tin nhắn, thêm yêu cầu cụ thể, ví dụ: "Chỉ viết một email nhắc thanh toán, giọng lịch sự, tối đa 120 từ".

Nếu nơi làm việc của bạn có chức năng lưu hướng dẫn dùng lại, bạn có thể lưu nội dung ở đó theo quy định của nơi làm việc. Các file trong thư viện này chưa phải gói Skill cài đặt sẵn để ChatGPT tự nhận diện.

### Claude

Mở cuộc trò chuyện mới, dán nội dung file đã điền bối cảnh và thêm yêu cầu cụ thể. Nếu tài khoản của bạn có nơi lưu hướng dẫn dùng lại, có thể lưu ở đó để khỏi dán mỗi lần.

### Gemini

Mở cuộc trò chuyện mới, dán nội dung file đã điền bối cảnh và thêm yêu cầu cụ thể. Nếu tài khoản của bạn có nơi lưu hướng dẫn dùng lại, có thể lưu ở đó để khỏi dán mỗi lần.

---

## 4. Cách nêu yêu cầu để kết quả tốt

Skill chỉ hỏi thêm khi thiếu thông tin quan trọng, tối đa 4 câu mỗi lượt. Bạn có thể cung cấp bối cảnh ngay trong yêu cầu đầu tiên để có kết quả sát hơn. Ví dụ với skill kế hoạch marketing:

> Lập kế hoạch marketing quý 4 cho dòng đèn LED. Mục tiêu doanh thu 2 tỷ, ngân sách marketing 150 triệu, kênh đang chạy là Shopee và Facebook, giai đoạn tăng trưởng.

Khi đã đủ thông tin, skill sẽ làm ngay. Nếu kết quả chưa đúng hướng, bạn có thể nêu điểm cần chỉnh và yêu cầu sửa phần đó.

Mẹo:

- **Dán biểu mẫu công ty đang dùng** nếu có (mẫu báo cáo, bảng theo dõi, cấu trúc văn bản). Skill sẽ làm theo đúng mẫu đó thay vì cấu trúc mặc định.
- **Chỉ rõ phần cần làm.** Ví dụ "chỉ viết tin nhắn đầu tiên" hoặc "chỉ sửa bảng ngân sách"; bạn không phải nhận toàn bộ các mục của skill.
- **Sửa các quy tắc trong file nếu cần.** Phần 0 là bối cảnh công ty; phần 2 là thông tin AI cần hỏi; phần 3 là cách làm; phần 4 là mẫu kết quả; phần 5 là danh sách tự kiểm tra. Dòng **Từ ngữ** giải thích chữ viết tắt và thuật ngữ hay gặp.
- **Chỗ ghi `[cần bổ sung: ...]`** trong kết quả là dữ liệu AI không có và không bịa. Bạn điền số thật vào hoặc cung cấp thêm rồi yêu cầu cập nhật.
- **Đưa số liệu thật** nếu được phép chia sẻ. Có số, AI tính được; không có số, AI chỉ nói chung chung.
- **Nói rõ người đọc kết quả** là ai: giám đốc, trưởng phòng hay nhân viên mới. Skill sẽ điều chỉnh độ dài và ngôn ngữ.
- **Yêu cầu sửa theo phần.** Kết quả nào có nhiều phần, hãy nói "sửa lại phần 3, giữ nguyên các phần khác" thay vì làm lại từ đầu.
- **Kiểm tra lại số liệu** AI đưa ra. Mức tham khảo trong skill chỉ là gợi ý; cần xem nguồn, thời điểm và mức phù hợp với công ty trước khi dùng.

---

## 5. Khi kết quả chưa tốt

| Hiện tượng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| AI trả lời chung chung | Phần bối cảnh để trống hoặc yêu cầu thiếu số | Điền bối cảnh, bổ sung mục tiêu và số liệu |
| AI hỏi lại thông tin đã có | Chưa dùng hết bối cảnh bạn cung cấp | Nhắc AI dùng dữ liệu trong yêu cầu và làm ngay nếu đã đủ |
| Kết quả không đúng ý | Yêu cầu đầu ra chưa đủ cụ thể | Nêu rõ phần cần làm, người đọc và mẫu công ty nếu có; chỉ yêu cầu theo phần 4 khi bạn muốn bản đầy đủ |
| Dùng thuật ngữ tiếng Anh nhiều | Đặc thù công cụ | Nhắc "viết tiếng Việt, thuật ngữ kèm tiếng Anh trong ngoặc" |
| Số liệu lạ, không có nguồn | AI tự bịa | Yêu cầu "ghi rõ số nào là giả định" |

---

## 6. Đóng góp skill mới

Phòng ban nào có quy trình riêng muốn đóng gói thành skill, viết theo đúng mẫu của các skill hiện có (mở một skill cùng nhóm để tham khảo bố cục) hoặc xem hướng dẫn tạo skill trên ChatGPT trong trang `index.html`. Skill mới cần:

- Đúng bố cục 6 phần như mọi skill khác.
- Viết đủ các bước cần thiết nhưng bỏ phần lặp, phần không giúp AI làm đúng việc; 150 đến 250 dòng chỉ là khoảng tham khảo của thư viện này.
- Có phần bối cảnh công ty với các dòng `[ĐIỀN]`.
- Dùng độc lập; nếu nhắc đến skill khác, chỉ coi đó là gợi ý cho việc liên quan.
- Đặt tên file theo mã phòng ban và số thứ tự kế tiếp.

Gửi file cho người quản lý bộ skill để rà soát trước khi đưa vào thư mục chung.
