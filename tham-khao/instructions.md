# Instructions

> **Là gì:** phần khai báo một lần để ChatGPT biết bạn là ai và luật chung của phòng, không phải dặn lại ở mỗi cuộc chat.
> **Tra mục này khi:** mới bắt đầu dùng ChatGPT cho công việc, lập Project cho phòng, hoặc thấy ChatGPT "quên" luật và viết sai giọng.

## Tóm tắt nhanh

- Mỗi lần mở chat mới, ChatGPT không biết bạn là ai, làm ở đâu, bán sản phẩm gì. Instructions là cách nói **một lần** để ChatGPT nhớ.
- Chỉ ghi điều đúng cho **mọi** việc. Quy trình chi tiết của một việc đặt vào Skill. Số liệu dùng một lần đặt vào Prompt.
- Tả bằng hành vi đếm được, không tả bằng tính từ.
- Luôn có ba nguyên tắc chống bịa.

## Ba nơi đặt Instructions trong ChatGPT

| Nơi | Áp dụng cho | Ví như | Nên đặt gì vào | Cách mở |
|---|---|---|---|---|
| **Custom Instructions** | Mọi cuộc chat của tài khoản | Danh thiếp của chính mình | Chức danh, cách xưng hô, văn phong, quy tắc chung | Settings → Personalization → Custom instructions |
| **Project instructions** | Chỉ các chat nằm trong Project đó | Hồ sơ nhập môn của phòng | Đơn vị, sản phẩm, thuật ngữ, luật riêng, kèm file tham chiếu | Thanh bên → New project. Instructions: ••• → Project settings. Files: thêm vào phần nguồn (sources) của Project |
| **Memory** | ChatGPT tự ghi lại qua các cuộc chat | Sổ giao ca | Thói quen nhỏ, ví dụ "thích báo cáo dạng bảng" | Settings → Personalization → Memory → Manage (hoặc Saved memories) |

#### Chi tiết cần biết

- **Trong Project, Project instructions ghi đè Custom Instructions.** Vì vậy luật nghiệp vụ của phòng phải đặt trong Project.
- **Project có chế độ memory riêng (project-only memory),** chỉ nhớ trong phạm vi Project. Hợp với từng phòng ban hoặc từng nhóm khách. ChatGPT Work không chạy trong Project đang bật chế độ này.

#### Cách dùng gợi ý

- Custom Instructions dùng cho phần "tôi là ai".
- Mỗi mảng việc lớn tạo 1 Project riêng, ví dụ "Wir – Marketing", "Wir – Kinh doanh sỉ".
- Memory cho ChatGPT tự học thêm, nhưng phải mở ra kiểm tra định kỳ, ghi sai thì xóa.

> **Lưu ý:** Tên và vị trí menu có thể đổi theo phiên bản ChatGPT.

## Thông tin nào đặt ở đâu

Instructions giống bảng nội quy dán ở cửa phòng: chỉ ghi điều đúng cho mọi việc. Nhét quy trình chi tiết vào đây thì bảng nội quy dài ba trang và không ai đọc.

| Thông tin | Đặt ở | Vì sao |
|---|---|---|
| "Tôi là nhân viên Sale của Wir Group, phụ trách khách sỉ" | Instructions | Đúng cho mọi việc |
| "TPCN không dùng từ 'điều trị'; không bịa số" | Instructions | Luật chung của phòng |
| Các bước viết lịch nội dung 14 ngày | Skill | Chỉ đúng cho 1 việc |
| Số liệu đơn hàng tháng này | Prompt | Chỉ dùng 1 lần |
| Hộp thư, file trên Drive | Plugin | Dữ liệu nằm ngoài ChatGPT |
| "Tôi thích bảng hơn đoạn văn" | Memory | Thói quen nhỏ, ChatGPT tự nhớ |

## Cách viết: tả bằng hành vi, không tả bằng tính từ

"Chuyên nghiệp" với mỗi người một kiểu, với ChatGPT lại là kiểu khác. Muốn ChatGPT viết đúng giọng thì phải tả bằng thứ đếm được, nhìn thấy được.

| Tính từ (chưa dùng được) | Hành vi (dùng được) |
|---|---|
| Viết chuyên nghiệp | Câu dưới 20 chữ. Không emoji. Xưng "Wir Group", gọi đối tác là "Quý đối tác". |
| Thân thiện, gần gũi | Gọi khách là "anh/chị", xưng "em". Mở bài bằng một tình huống da cụ thể. |
| Ngắn gọn | Tin nhắn dưới 150 chữ. Tối đa 5 gạch đầu dòng. |
| Cẩn thận số liệu | Không tự bịa số. Thiếu thì ghi `[CẦN ĐIỀN]`. |

> **Mẹo:** **Phép thử đổi tên.** Thay "Wir Group" bằng tên đối thủ. Nếu câu vẫn đúng thì câu đó quá chung chung, phải viết lại.

## Ba nguyên tắc chống bịa

Đặt ba nguyên tắc này vào mọi bản Instructions.

1. **Chỉ dùng dữ liệu được cấp.** Không tự chế số liệu, tên người, ngày tháng, điều khoản.
2. **Gắn nhãn nguồn.** Thông tin lấy từ tài liệu ghi `[DATA THẬT]`. Thông tin tự suy ra ghi `[SUY LUẬN]`. Chưa có dữ liệu thì ghi "chưa đủ dữ liệu" hoặc `[CẦN ĐIỀN]`.
3. **Người duyệt cuối.** Mọi thứ ChatGPT viết là bản nháp. Người ký và người bấm gửi chịu trách nhiệm.

> **Ghi nhớ:** "Chưa đủ dữ liệu" tốt hơn một con số nghe hợp lý. Con số bịa mà trơn tru mới là thứ nguy hiểm nhất, vì không ai nghi ngờ nó.

## Bảo mật

> **Cảnh báo:** Năm loại tuyệt đối không dán vào ChatGPT:
> - Giá vốn, giá thành, công thức.
> - Hợp đồng có điều khoản bảo mật.
> - Thông tin cá nhân nhân viên (lương, CCCD).
> - Mật khẩu, tài khoản.
> - Tài liệu đóng dấu MẬT.

### Tắt huấn luyện

Vào Settings → Data controls, tắt *Improve the model for everyone*. Làm một lần cho mỗi tài khoản.

### Temporary Chat

Dùng khi xử lý nội dung nhạy cảm.

- Chat tạm không vào lịch sử (trừ khi bấm **Save**), không dùng để huấn luyện, không tạo Memory mới.
- Khi mở chat tạm, chọn **Unpersonalized** thì chat không đọc Memory, Custom Instructions và plugin. Chọn **Personalized** thì vẫn đọc.
- OpenAI vẫn giữ bản sao tối đa 30 ngày vì lý do an toàn.

### Làm sạch trước khi dán

- Thay tên thật bằng tên chung, ví dụ "khách hàng A", "HĐ số X".
- **Không ghi thông tin nhạy cảm vào Instructions hoặc Memory.** Hai chỗ này đi theo mọi cuộc chat.

## Mẫu dùng ngay

Thay phần trong ngoặc vuông bằng thông tin của bạn trước khi dán.

### Custom Instructions cá nhân

Dán vào Settings → Personalization → Custom instructions.

```text title="Custom Instructions cá nhân"
Thông tin về tôi:
- Chức danh: [Nhân viên Sale phụ trách khách sỉ], Wir Group, nhà phân phối dược mỹ phẩm
  và thực phẩm bảo vệ sức khỏe.
- Khách tôi phụ trách: spa, nhà thuốc, đại lý, cửa hàng mỹ phẩm.
- Tôi báo cáo cho [Trưởng phòng Kinh doanh].
- Việc tôi hay nhờ: soạn tin Zalo và email cho khách, tóm tắt tài liệu sản phẩm,
  báo cáo doanh số, biên bản họp.

Cách trả lời tôi:
1. Luôn trả lời tiếng Việt có dấu. Câu ngắn, đoạn ngắn, gạch đầu dòng khi liệt kê.
2. Không bịa số liệu, tên người, ngày tháng, điều khoản. Thiếu thì ghi [CẦN ĐIỀN].
3. Việc phức tạp thì hỏi lại tôi tối đa 3 câu trước khi làm, mỗi câu kèm sẵn phương án để tôi chọn.
4. Không dùng emoji trong văn bản công việc.
5. Cuối mỗi văn bản quan trọng, nhắc đúng một dòng: "Kiểm tra lại số liệu và tên riêng trước khi gửi."
```

### Project instructions cho phòng Marketing

Tạo Project "Wir – Marketing". Dán mẫu vào phần Instructions, rồi tải file dữ liệu sản phẩm và hồ sơ sản phẩm vào phần Files.

```text title="Project instructions · Marketing"
## 1. Tôi là ai
Nhân viên Marketing, Wir Group. Wir phân phối dược mỹ phẩm và thực phẩm bảo vệ sức khỏe (TPCN).
Việc chính: bài Facebook, tin Zalo OA, kịch bản video ngắn cho sản phẩm Wir.

## 2. Sản phẩm và tầng pháp lý
Xem file du-lieu-san-pham-wir.md. Chỉ dùng công dụng và số liệu ghi trong file.
- TPCN: Elasten, CH Alpha Plus, Warnke, Lactobact Intima.
- Mỹ phẩm: DEO Cream, M.Asam, Vagisan.
- Thiết bị tiêm: Karima (Karisma). Chỉ bác sĩ tại cơ sở được cấp phép. Không viết nội dung
  cho người dùng tự dùng.

## 3. Từ ngữ theo tầng
- TPCN được nói: "hỗ trợ", "góp phần", "bổ sung", "cải thiện".
- TPCN cấm: "chữa", "điều trị", "khỏi", "đặc trị", "hết hẳn", "thay thế thuốc".
- Mọi nội dung về TPCN kèm câu: "Thực phẩm này không phải là thuốc và không có tác dụng
  thay thế thuốc chữa bệnh."
- Cấm "số 1", "tốt nhất" khi chưa gắn nguồn (tên nguồn và năm).
- Thai kỳ: không nói "tốt cho thai kỳ". Elasten chỉ được nói "không gây rủi ro" theo giám định.
  Warnke chống chỉ định phụ nữ có thai và cho con bú.

## 4. Giọng văn
Gọi khách "anh/chị", xưng "em". Câu dưới 20 chữ, một ý một câu.
Mở bài bằng một tình huống cụ thể của khách. Tối đa 2 emoji mỗi bài.

## 5. Chưa có dữ liệu (gặp thì ghi [CẦN ĐIỀN])
Giá bán lẻ hiện hành, chương trình khuyến mãi đang chạy, quy cách đóng gói, liệu trình khuyến nghị.

## 6. Ba nguyên tắc chống bịa
Chỉ dùng dữ liệu tôi cấp; gắn nhãn [DATA THẬT]/[SUY LUẬN]/[CẦN ĐIỀN];
mọi đầu ra là nháp, tôi là người duyệt cuối. Nội dung về thai kỳ, vùng kín để người duyệt trước khi đăng.
```

### Project instructions cho phòng Kinh doanh (khách sỉ)

Tạo Project "Wir – Kinh doanh sỉ". Dán mẫu vào Instructions, tải file dữ liệu sản phẩm và chính sách giá sỉ vào Files.

```text title="Project instructions · Kinh doanh sỉ"
## 1. Tôi là ai
Nhân viên Sale, Phòng Kinh doanh Wir Group, phụ trách khách sỉ: spa, nhà thuốc, đại lý, cửa hàng.

## 2. Luật báo giá
- Chỉ báo chiết khấu theo bảng 4 mức trong file chính sách giá sỉ. Trần chiết khấu 20%.
- Chưa có giá bán lẻ nền thì ghi [CẦN ĐIỀN], không tự tính ra số tiền cuối.
- Khách đòi điều chưa có chính sách (độc quyền khu vực, chiết khấu trên 20%, công nợ quá 15 ngày,
  ký gửi, giá riêng từng SKU): chỉ nói đúng 1 câu "Mức này vượt chính sách sỉ hiện hành,
  em cần xin ý kiến quản lý trước khi xác nhận với anh/chị." Không báo số, không hứa.
- Karima là thiết bị tiêm, không nằm trong chính sách sỉ: chuyển quản lý.

## 3. Ranh giới sản phẩm
Dùng bộ từ cấm theo tầng pháp lý trong file du-lieu-san-pham-wir.md.
Khách hỏi thai kỳ: Elasten chỉ nói "không gây rủi ro" theo giám định; Warnke chống chỉ định;
sản phẩm khác chưa có tài liệu thì chuyển người phụ trách.

## 4. Giọng văn
Gọi khách "anh/chị", xưng "em". Tin nhắn dưới 150 chữ, không emoji.
Tin Zalo gồm lời chào, nội dung, chữ ký.

## 5. Ba nguyên tắc chống bịa
Chỉ dùng dữ liệu tôi cấp; gắn nhãn [DATA THẬT]/[SUY LUẬN]/[CẦN ĐIỀN];
mọi tin gửi khách là nháp, tôi tự gửi.
```

## Ví dụ: trước và sau khi có Instructions

Cùng một câu lệnh: *"Viết bài Facebook bán Elasten."*

| Không có Instructions | Có Project instructions phòng Marketing |
|---|---|
| "Elasten — collagen SỐ 1, điều trị nếp nhăn, trẻ ra chỉ sau 7 ngày!!!" | "Da bạn khô và kém đàn hồi? Sau 12 tuần, nghiên cứu lâm sàng ghi nhận độ ẩm da tăng 28%… Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh." |
| Dùng từ cấm "điều trị" cho TPCN. "Số 1" không có nguồn. Tự bịa kết quả "7 ngày" | Số liệu có nguồn: +28% độ ẩm sau 12 tuần. Có câu bắt buộc của TPCN. Giá chưa có thì ghi `[CẦN ĐIỀN]` |

Số +28% độ ẩm da sau 12 tuần là `[DATA THẬT]` trích từ tài liệu sản phẩm Wir.

> **Ghi nhớ:** Không phải ChatGPT giỏi lên. Lần này nó đã đọc hồ sơ nhập môn.

## Kiểm tra Instructions đã có hiệu lực

Làm bốn phép thử sau mỗi khi viết mới hoặc sửa Instructions.

1. **Phép thử chống bịa.** Trong Project, hỏi 3 con số mà hồ sơ không có.

   ```text title="Câu hỏi thử chống bịa"
   Giá bán lẻ Elasten hiện nay là bao nhiêu? Tháng này đang có chương trình khuyến mãi gì?
   ```

   Đạt khi cả 3 lần ChatGPT đều trả lời "chưa đủ dữ liệu" hoặc hỏi xin thêm. Nếu nó đưa ra một con số, thêm dòng luật còn thiếu vào Instructions.
2. **Kiểm tra trong chat mới.** Mở một chat mới trong cùng Project rồi hỏi lại luật.

   ```text title="Câu hỏi kiểm tra trí nhớ"
   Elasten thuộc tầng pháp lý nào? Khi viết bài thì những từ nào bị cấm?
   ```

   Đạt khi ChatGPT dùng đúng thuật ngữ và tuân thủ luật mà không cần nhắc lại.
3. **Kiểm tra bảo mật.** Xác nhận đã tắt *Improve the model for everyone*, và Instructions lẫn Memory không chứa thông tin nhạy cảm.
4. **Kiểm tra Memory.** Dặn ChatGPT nhớ một thói quen nhỏ.

   ```text title="Câu thử Memory"
   Hãy nhớ: tôi thích mọi báo cáo trình bày dạng bảng.
   ```

   Vào Settings → Personalization → Memory → Manage (hoặc Saved memories), tìm dòng vừa được ghi, rồi xóa thử. Nếu tài khoản chỉ hiện bản tóm tắt Memory, không có danh sách từng dòng, thì gõ "Hãy quên điều tôi vừa dặn". Đạt khi bạn xem được và xóa được điều ChatGPT đã nhớ.

## Lỗi hay gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Nhồi quy trình chi tiết vào Instructions | Instructions dài vài trang, ChatGPT làm sót bước | Chỉ giữ thứ luôn đúng. Quy trình chi tiết tách ra Skill |
| Tả giọng văn bằng tính từ | Kết quả "chuyên nghiệp" mỗi lần một kiểu | Đổi sang số và hành vi: độ dài câu, cách xưng hô, có hay không có emoji |
| Quên ghi luật chống bịa | Hỏi số không có, ChatGPT vẫn trả ra một con số | Thêm dòng "Không bịa số. Thiếu ghi [CẦN ĐIỀN]" |
| Thiếu bộ từ cấm theo tầng pháp lý | Bài TPCN vẫn có "điều trị", "khỏi hẳn"; thiếu câu bắt buộc | Thêm mục từ cấm và câu bắt buộc vào Project instructions, tải file dữ liệu sản phẩm vào Files |
| Chat ngoài Project | Hỏi lại thấy ChatGPT "quên hết" | Kiểm tra tên Project ở đầu khung chat |
| Custom Instructions và Project instructions mâu thuẫn | Trong Project, ChatGPT bỏ qua luật cá nhân | Custom Instructions chỉ để phần cá nhân. Luật nghiệp vụ để trong Project. Luật cá nhân nào cần áp dụng trong Project thì chép vào Project instructions |
| Ghi thông tin nhạy cảm vào Instructions hoặc Memory | Lương, số điện thoại khách nằm trong Instructions | Xóa ngay. Dùng tên chung như "khách hàng A" |

## Nguồn chính thức

Tính năng ChatGPT thay đổi nhanh. Khi màn hình khác với trang này, đối chiếu lại với nguồn chính thức dưới đây.

- [Custom instructions – OpenAI Help](https://help.openai.com/en/articles/8096356)
- [Memory – OpenAI Help](https://help.openai.com/en/articles/8590148)
- [Temporary Chat – OpenAI Help](https://help.openai.com/en/articles/8914046)
- [Projects – OpenAI Help](https://help.openai.com/en/articles/10169521)
- [ChatGPT Release Notes – OpenAI Help](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

## Liên quan

- [Prompt](#prompt): giao từng việc cụ thể. Phần nào đã có trong Instructions thì prompt không cần nhắc lại.
- [Skill](#skill): nơi đặt quy trình chi tiết của một việc lặp lại.
