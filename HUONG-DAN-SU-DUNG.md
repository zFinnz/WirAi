# Hướng dẫn sử dụng bộ kỹ năng

Mỗi file skill là một bản hướng dẫn hoàn chỉnh cho AI. Bạn chỉ cần dán nguyên file vào công cụ AI mình đang dùng. Dưới đây là cách làm với từng công cụ và vài mẹo để kết quả tốt hơn.

---

## 1. Chọn đúng skill

1. Mở [README.md](README.md), tìm nhóm phòng ban của bạn.
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

Dòng nào không biết hoặc không liên quan thì ghi `không áp dụng`. Không xóa dòng, không để nguyên chữ `[ĐIỀN]`.

**Lưu ý bảo mật:** không điền số liệu tài chính nhạy cảm, thông tin khách hàng cụ thể, mật khẩu hay tài liệu mật vào công cụ AI công cộng. Dùng số làm tròn hoặc số giả định khi cần.

---

## 3. Tạo skill trên từng công cụ

### ChatGPT

1. Đăng nhập ChatGPT, vào mục tạo skill (tùy phiên bản, mục này nằm ở thanh bên trái hoặc trong phần cài đặt tài khoản; tên gọi có thể là "Skills" hoặc "Tạo skill").
2. Chọn tạo mới, đặt tên theo mã và tên skill, ví dụ `MKT-01 Kế hoạch marketing`.
3. Mở file skill, chọn toàn bộ nội dung (Ctrl+A hoặc Cmd+A), sao chép và dán vào ô hướng dẫn.
4. Lưu lại. Từ lần sau chỉ cần chọn skill đó rồi nêu yêu cầu.

Nếu phiên bản ChatGPT của bạn không có mục tạo skill, cách thay thế: mở cuộc trò chuyện mới, dán toàn bộ file làm tin nhắn đầu tiên, rồi xuống dòng và viết yêu cầu của bạn.

### Claude

1. Vào claude.ai, tạo một **Project** mới, đặt tên theo mã skill.
2. Vào phần hướng dẫn của Project (Project instructions), dán toàn bộ nội dung file.
3. Mọi cuộc trò chuyện trong Project đó sẽ dùng skill này.

Cách thay thế: dán file vào tin nhắn đầu tiên giống ChatGPT.

### Gemini

1. Vào Gemini, chọn tạo **Gem** mới.
2. Đặt tên theo mã skill, dán toàn bộ nội dung file vào phần hướng dẫn.
3. Lưu và dùng Gem đó khi cần.

---

## 4. Cách nêu yêu cầu để kết quả tốt

Skill sẽ hỏi bạn tối đa 4 câu trước khi làm. Bạn có thể trả lời trước ngay trong yêu cầu đầu tiên để tiết kiệm một lượt. Ví dụ với skill kế hoạch marketing:

> Lập kế hoạch marketing quý 4 cho dòng đèn LED. Mục tiêu doanh thu 2 tỷ, ngân sách marketing 150 triệu, kênh đang chạy là Shopee và Facebook, giai đoạn tăng trưởng.

Sau khi hỏi xong, skill sẽ **tóm tắt cách hiểu và đề xuất cách làm trong vài dòng rồi chờ bạn xác nhận** mới làm bản đầy đủ. Đây là lúc sửa hướng nếu AI hiểu sai, đỡ phải làm lại cả bản dài. Nếu bạn đã chắc, nói "làm luôn" để bỏ qua bước này.

Mẹo:

- **Dán biểu mẫu công ty đang dùng** nếu có (mẫu báo cáo, bảng theo dõi, cấu trúc văn bản). Skill sẽ làm theo đúng mẫu đó thay vì cấu trúc mặc định.
- **Chỗ ghi `[cần bổ sung: ...]`** trong kết quả là dữ liệu AI không có và không bịa. Bạn điền số thật vào hoặc cung cấp thêm rồi yêu cầu cập nhật.
- **Đưa số liệu thật** nếu được phép chia sẻ. Có số, AI tính được; không có số, AI chỉ nói chung chung.
- **Nói rõ người đọc kết quả** là ai: giám đốc, trưởng phòng hay nhân viên mới. Skill sẽ điều chỉnh độ dài và ngôn ngữ.
- **Yêu cầu sửa theo phần.** Kết quả nào có nhiều phần, hãy nói "sửa lại phần 3, giữ nguyên các phần khác" thay vì làm lại từ đầu.
- **Kiểm tra lại số liệu** AI đưa ra. Mọi con số chuẩn so sánh trong skill là mức tham khảo thị trường Việt Nam, không phải số của công ty bạn.

---

## 5. Khi kết quả chưa tốt

| Hiện tượng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| AI trả lời chung chung | Phần bối cảnh để trống hoặc yêu cầu thiếu số | Điền bối cảnh, bổ sung mục tiêu và số liệu |
| AI bỏ qua các bước hỏi | Dán thiếu file hoặc công cụ cắt bớt nội dung dài | Kiểm tra đã dán đủ đến phần 5 chưa |
| Kết quả không đúng cấu trúc | AI bị yêu cầu khác đè lên | Nhắc "làm đúng theo phần 4 Cấu trúc kết quả" |
| Dùng thuật ngữ tiếng Anh nhiều | Đặc thù công cụ | Nhắc "viết tiếng Việt, thuật ngữ kèm tiếng Anh trong ngoặc" |
| Số liệu lạ, không có nguồn | AI tự bịa | Yêu cầu "ghi rõ số nào là giả định" |

---

## 6. Đóng góp skill mới

Phòng ban nào có quy trình riêng muốn đóng gói thành skill, viết theo đúng mẫu của các skill hiện có (mở một skill cùng nhóm để tham khảo bố cục) hoặc xem hướng dẫn tạo skill trên ChatGPT trong trang `index.html`. Skill mới cần:

- Đúng bố cục 6 phần như mọi skill khác.
- Dài 150 đến 250 dòng.
- Có phần bối cảnh công ty với các dòng `[ĐIỀN]`.
- Không tham chiếu file khác, không yêu cầu công cụ bên ngoài.
- Đặt tên file theo mã phòng ban và số thứ tự kế tiếp.

Gửi file cho người quản lý bộ skill để rà soát trước khi đưa vào thư mục chung.
