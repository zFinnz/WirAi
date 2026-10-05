# Dữ liệu demo để tập

Bộ dữ liệu **DEMO** của Wir Group để tập các mẫu prompt trên trang Prompt và Plugin. Đây không phải số liệu kinh doanh thật. Review, tin nhắn và ghi chú lead là giọng khách mô phỏng.

File Excel mở bằng Excel hoặc Google Sheets. File Word mở bằng Word hoặc Google Docs. Có thể tải thẳng các file này lên ChatGPT.

| Tài liệu | File | Nội dung | Tập với |
|---|---|---|---|
| Đơn hàng tháng 7 | `don-hang-demo.xlsx` (Excel) | 40 dòng đơn hàng, 6 cột: Ngày, Kênh, Sản phẩm, Số lượng, Đơn giá, Thành tiền | Prompt: phân tích file số liệu. Plugin: đọc và ghi file trên Drive |
| Review và tin nhắn khách | `review-va-tin-nhan-khach.docx` (Word) | 20 review (R01–R20) và 10 tin nhắn hỏi trước khi mua (M01–M10) về Elasten, Lactobact Intima | Prompt: rút insight từ phản hồi khách |
| Danh sách 12 lead | `danh-sach-lead.xlsx` (Excel) | 12 lead ngành làm đẹp và bán sỉ | Prompt: chấm điểm lead và soạn tin tiếp cận |
| Ghi chú trao đổi lead | `ghi-chu-trao-doi-lead.docx` (Word) | Ghi chú trao đổi với 5 lead (L01, L04, L05, L08, L11) | Prompt: soạn tin tiếp cận. Plugin: phép thử trước khi bàn giao |
| Chính sách giá sỉ | `chinh-sach-gia-si-demo.docx` (Word) | Bảng chiết khấu sỉ 4 mức, điều chưa có chính sách, câu xin ý kiến quản lý | Prompt: trả lời khách hỏi giá sỉ, chấm điểm lead |
| Bản ghi họp Phòng Kinh doanh | `transcript-hop-demo.docx` (Word) | Cuộc họp kế hoạch tháng 8, có chỗ chưa rõ ai làm | Prompt: biên bản họp và bảng đầu việc |
| Đáp án | `dap-an.docx` (Word) | Số đối chiếu và các bẫy cài sẵn trong từng file | Tự chấm sau khi làm |

## Cách dùng

1. Tải file cần dùng. Tải thẳng file lên ChatGPT, hoặc mở file rồi sao chép nội dung dán vào chat. Sau đó chạy mẫu prompt tương ứng.
2. Làm xong mới mở file Đáp án để đối chiếu. Không dán đáp án vào ChatGPT cùng dữ liệu.
3. Mỗi file có **lỗ hổng cố ý**: ô để trống, lead thiếu thông tin, khách đòi điều vượt chính sách, review lệch khen. Đạt là khi ChatGPT ghi `[CẦN ĐIỀN]`, chuyển quản lý, hoặc trả lời "chưa đủ dữ liệu", thay vì tự điền cho đủ.

## Lưu ý

- Đây là dữ liệu tập. Không trộn dữ liệu khách thật vào khi tập trên ChatGPT.
- Hồ sơ sản phẩm (Elasten, Lactobact Intima) và file dữ liệu sản phẩm Wir không kèm ở đây vì chứa tài liệu nội bộ. Mẫu Project instructions trên trang Instructions vẫn dùng được: thay tên file bằng tài liệu sản phẩm của phòng bạn.
- Hai file Excel có thêm trang tính "Đọc trước" ghi chú về dữ liệu. Dữ liệu nằm ở trang tính đầu tiên.
- Sửa dữ liệu thì mở thẳng file Word, Excel ra sửa. Thêm file mới vào thư mục này rồi chạy `python3 _build/build-index.py` để trang web nhận file.
