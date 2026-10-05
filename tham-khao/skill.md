# Skill

> **Là gì:** tờ quy trình chuẩn cho một loại việc lặp lại. Viết một lần, ChatGPT tự gọi ra mỗi khi gặp đúng loại việc đó.
> **Tra mục này khi:** thấy mình gõ lại cùng một bộ chỉ dẫn mỗi tuần, cần tạo hoặc sửa skill, hoặc skill không được gọi và chạy sai.

## Tóm tắt nhanh

- Skill là tờ quy trình chuẩn dán trên tường, nhưng viết cho ChatGPT. Ai làm việc đó cũng ra kết quả giống nhau, không sót bước.
- ChatGPT chỉ đọc **tên và dòng `description`** để quyết định có dùng skill hay không. Dòng mô tả mơ hồ thì skill không bao giờ được gọi.
- Làm tay vài lượt trước, đóng gói sau. Mỗi lần phải nhắc thêm chính là một mục trong skill.
- Sai thì sửa skill, không sửa tay kết quả.
- Một skill một việc. Nhiều việc thì nối skill thành chuỗi.

## Instructions, Prompt và Skill khác nhau thế nào

| | Instructions | Prompt | Skill |
|---|---|---|---|
| Ví như | Nội quy | Phiếu giao việc hôm nay | Tờ quy trình chuẩn cho 1 việc |
| Áp dụng | Mọi việc | 1 lần | Mỗi lần gặp đúng loại việc đó |
| Độ dài | Ngắn, chỉ điều luôn đúng | Vừa đủ cho việc này | Chi tiết, không sợ dài |
| Ai gọi | Tự áp dụng | Mình gõ | ChatGPT tự chọn, hoặc mình gọi bằng `@` |

## Skill hoạt động thế nào

1. Bạn gõ yêu cầu, ví dụ "Tóm tắt tài liệu này".
2. ChatGPT **chỉ đọc tên và dòng `description`** của mọi skill đang có.
3. Thấy skill nào khớp, ChatGPT mới mở toàn bộ file `SKILL.md` của skill đó ra.
4. ChatGPT làm đúng từng bước trong skill, kể cả bước hỏi lại khi thiếu thông tin.

> **Ghi nhớ:** Bước 2 là chỗ mấu chốt. ChatGPT không đọc hết mọi skill, nó chỉ đọc dòng mô tả. Dòng mô tả mơ hồ thì skill viết hay cỡ nào cũng không được gọi ra.

## Cấu trúc một skill

Một skill là một thư mục chứa file `SKILL.md`. Đầu file **bắt buộc** có khối `name` / `description` nằm giữa hai dòng `---`. Phần thân gồm 6 phần:

1. **Tên skill:** viết thường, không dấu, nối bằng gạch ngang. Ví dụ `viet-bai-tpcn`.
2. **Mô tả:** một câu.
3. **Khi nào dùng:** ít nhất 3 tình huống, và khi nào **không** dùng.
4. **Đầu vào:** ghi rõ mục bắt buộc và mục "có thì tốt".
5. **Các bước:** bước 1 luôn là kiểm tra đủ đầu vào; bước cuối luôn là tự rà lại.
6. **Đầu ra:** kèm một ví dụ mẫu đã điền số liệu.

## Ba cách tạo skill trong ChatGPT

- **Create with chat:** ngay trong cuộc chat, bảo ChatGPT "đóng gói cách làm vừa rồi thành skill". ChatGPT hỏi thêm vài câu rồi đề nghị cài skill. Cách này hợp với người mới.
- **Create with editor:** thanh bên → Plugins → tab Skills → Create → Create with editor. Tự viết hoặc dán nội dung `SKILL.md`. Muốn dùng một bản trong [Skill template](#skill-template): điền phần bối cảnh, rồi thêm khối `name` / `description` ở đầu như [mẫu SKILL.md](#skill/skill-mot-skill-md-hoan-chinh) trước khi dán. Bản template không có khối này thì ChatGPT không biết khi nào gọi skill.
- **Upload from your computer:** nạp skill có sẵn trên máy. Skill tải lên được quét bảo mật xong mới dùng được.
- **Tài khoản không thấy tab Skills:** tạo skill bên trong plugin bằng `@plugin-creator` (xem [Plugin](#plugin/plugin-cach-tao-khong-can-code)). Khái niệm và cấu trúc `SKILL.md` giữ nguyên.

Hướng dẫn từng bước có trong [Hướng dẫn tạo skill trên ChatGPT](#tao-skill-chatgpt).

## Làm tay trước, đóng gói sau

Đừng ngồi nghĩ ra skill từ tờ giấy trắng. Hãy làm việc đó bằng tay vài lượt. Thấy mình phải dặn đi dặn lại chỉ dẫn nào thì đóng gói đúng chỉ dẫn đó lại.

Ví dụ với skill tóm tắt tài liệu, năm lượt chat biến thành năm mục của skill:

| Lượt chat làm tay | Câu phải hỏi thêm | Thành mục nào trong skill |
|---|---|---|
| Lượt 1 | "Tóm tắt giúp tôi tài liệu này", kết quả chung chung | Lý do cần skill |
| Lượt 2 | "Liệt kê theo từng phần của tài liệu" | **Ý CHÍNH CHI TIẾT** |
| Lượt 3 | "Bóc mọi con số, mốc thời gian, cam kết" | **SỐ LIỆU, NGÀY THÁNG, HẠN CHÓT** |
| Lượt 4 | "Có câu nào vượt ranh giới pháp lý, mâu thuẫn không?" | **ĐIỂM CẦN LƯU Ý / RỦI RO** |
| Lượt 5 | "Chỗ nào bạn tự đoán? Rút 3–5 ý gửi sếp" | **QUY TẮC** chống bịa và **TÓM TẮT NHANH** |

## Cải tiến skill: chạy, soi, sửa

- Chạy skill trên 3 việc thật. Ghi lại chỗ nào phải sửa tay.
- **Sai thì sửa skill, không sửa tay kết quả.** Sửa tay thì lần sau lại sai y như cũ.
- Mỗi lần sửa, ghi một dòng cuối file, ví dụ "Sửa lần 1: thêm bước soát từ cấm theo tầng pháp lý".

## Một skill một việc, nối thành chuỗi

Mỗi công đoạn một tờ quy trình, không gộp nhiều công đoạn vào 1 tờ.

```text
Marketing:  customer-insight  →  content-engine
Sale:       cham-diem-lead  →  soan-tiep-can-sale  →  xu-ly-tu-choi-sale
```

- Đầu ra của skill trước là đầu vào của skill sau. Ví dụ `customer-insight` rút insight từ review khách, rồi bảng insight đó là đầu vào cho `content-engine` viết nội dung.
- Còn mục `[CẦN ĐIỀN]` thì không chạy sang skill sau.

#### Tìm các skill mẫu này ở đâu

Tên skill trên trang này lấy từ thư viện skill mẫu của Wir. Trong [Skill template](#skill-template), bản gần nhất để làm điểm khởi đầu là:

| Skill mẫu | Việc | Skill template gần nhất |
|---|---|---|
| `tom-tat-tai-lieu` | Tóm tắt tài liệu dài | [VP-02](#skill/VP-02) |
| `ghi-chu-hop` | Biên bản họp và đầu việc | [OPS-03](#skill/OPS-03) |
| `kho-faq-noi-bo` | Hỏi đáp nội bộ | [OPS-07](#skill/OPS-07), [CS-03](#skill/CS-03) |
| `lam-sach-va-bao-cao` | Làm sạch bảng tính, lập báo cáo | [VP-04](#skill/VP-04) |
| `customer-insight` | Rút insight từ phản hồi khách | [CS-04](#skill/CS-04), [MKT-02](#skill/MKT-02) |
| `content-engine` | Lịch nội dung và bài đăng | [MKT-07](#skill/MKT-07), [MKT-08](#skill/MKT-08) |
| `viet-bai-tpcn` | Bài mạng xã hội cho sản phẩm TPCN | [MKT-08](#skill/MKT-08) |
| `cham-diem-lead` | Chấm điểm khách tiềm năng | [SAL-02](#skill/SAL-02) |
| `soan-tiep-can-sale` | Tin tiếp cận khách | [SAL-04](#skill/SAL-04) |
| `xu-ly-tu-choi-sale` | Xử lý từ chối | [SAL-06](#skill/SAL-06) |

Skill template là bản dán vào chat, viết cho doanh nghiệp nói chung. Khi đóng gói thành skill, bổ sung theo [cấu trúc một skill](#skill/skill-cau-truc-mot-skill): ranh giới sản phẩm của phòng, bước kiểm đầu vào, ví dụ đầu ra đã điền số liệu.

#### Tách những chỗ dễ chồng chéo

- Bài mạng xã hội là nội dung đăng công khai cho nhiều người. Tin trả lời khách là trao đổi 1-1, có báo giá và ranh giới chính sách.
- Karima là thiết bị tiêm, không đi chung skill viết bài TPCN.

## Để người khác dùng được

Muốn đồng nghiệp cầm skill lên chạy mà không cần hỏi lại, skill phải có thêm 4 mục:

| Mục | Ví dụ |
|---|---|
| **Vai trò** | "Viết như dược sĩ tư vấn ở quầy: giải thích thành phần trước, mời mua sau" |
| **Tiêu chuẩn đầu ra bằng số** | "Bài Facebook dưới 250 chữ, câu dưới 20 chữ, tối đa 2 emoji, đúng 1 lời mời hành động" |
| **Ranh giới không được vượt** | "Không tự quyết chiết khấu ngoài bảng. Khách hỏi thì ghi 'cần xác nhận với người phụ trách'" |
| **Xử lý khi thiếu dữ liệu** | "Ghi 'chưa đủ dữ liệu' tại chỗ đó, ghi rõ cần bổ sung gì, vẫn trả về phần đã làm được" |

### Phép thử cuối

1. Mở phiên mới.
2. **Không gọi tên skill.**
3. Giao một yêu cầu skill chưa từng làm, ví dụ "viết nội dung cho gian hàng Wir ở hội chợ".

Skill tự được gọi và làm đúng thì đạt.

Sau đó thêm một bẫy chống bịa: trong cùng phiên, hỏi một chi tiết mà tài liệu không có. Ví dụ sau khi tóm tắt hồ sơ Elasten:

```text title="Bẫy chống bịa"
Một hộp Elasten có bao nhiêu ống, giá bán lẻ bao nhiêu?
```

Đạt khi ChatGPT trả lời "Tài liệu không đề cập" cho cả hai ý, không đưa ra con số.

## Mẫu dùng ngay

### Dòng description: chưa đạt và đạt

| Chưa đạt | Đạt |
|---|---|
| `description: Viết nội dung cho công ty.` | `description: Viết bài mạng xã hội cho sản phẩm TPCN của Wir (Elasten, CH Alpha Plus, Lactobact Intima). Dùng khi cần bài Facebook, Zalo OA, kịch bản video ngắn. Không dùng cho Karima (thiết bị tiêm) và tin trả lời khách.` |
| Quá chung: skill bị gọi nhầm hoặc không bao giờ được gọi | Nêu rõ dùng khi nào, liệt kê tình huống, ghi cả lúc không dùng |

### Một SKILL.md hoàn chỉnh

```markdown title="SKILL.md · viet-bai-tpcn"
---
name: viet-bai-tpcn
description: Viết bài mạng xã hội cho sản phẩm TPCN của Wir (Elasten, CH Alpha Plus, Lactobact Intima). Dùng khi cần bài Facebook, Zalo OA, kịch bản video ngắn. Không dùng cho Karima (thiết bị tiêm) và tin trả lời khách.
---

# Viết bài sản phẩm TPCN

## Khi nào dùng
- Bài Facebook giới thiệu Elasten, CH Alpha Plus hoặc Lactobact Intima.
- Tin Zalo OA, bài "ngày bằng chứng" dùng số liệu lâm sàng có nguồn.
- Kịch bản video ngắn 30–60 giây.
Không dùng: Karima (thiết bị tiêm, chỉ thông tin cho nhân viên y tế); tin trả lời từng khách
(dùng soan-tiep-can-sale); sản phẩm mỹ phẩm như DEO Cream, M.Asam, Vagisan (ranh giới khác).

## Đầu vào
| Thông tin | Bắt buộc |
|---|---|
| Sản phẩm; kênh (Facebook / Zalo OA / video) | Bắt buộc |
| Mục tiêu bài (giới thiệu, ngày bằng chứng, nhắc mua lại) | Bắt buộc |
| Hồ sơ sản phẩm (file tham chiếu) | Bắt buộc |
| Khách mục tiêu; ưu đãi đang chạy | Có thì tốt, thiếu ghi [CẦN ĐIỀN] |

## Các bước
1. Kiểm tra đủ đầu vào. Thiếu mục bắt buộc thì hỏi lại 1 lần, tối đa 3 câu. Không bịa giá, khuyến mãi.
2. Xác định tầng pháp lý trong hồ sơ. Sản phẩm không phải TPCN thì dừng, báo dùng skill khác.
3. Chọn 1 nỗi lo cụ thể của khách làm câu mở bài.
4. Viết thân bài bằng từ được phép: "hỗ trợ", "góp phần", "bổ sung", "cải thiện".
5. Số liệu: chỉ dùng số trong hồ sơ, giữ nguyên, kèm nguồn. Không làm tròn, không thêm chỉ số.
6. Một lời mời hành động. Giá, khuyến mãi chưa có trong hồ sơ thì ghi [CẦN ĐIỀN].
7. Thêm câu bắt buộc: "Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."
8. Tự rà 6 điểm: không từ cấm (chữa, điều trị, khỏi, đặc trị, hết hẳn, thay thế thuốc);
   không "số 1", "tốt nhất" thiếu nguồn; số liệu khớp hồ sơ; không nói "tốt cho thai kỳ";
   có câu bắt buộc; đúng độ dài của kênh.
9. Kết thúc bằng: "Đây là bản nháp. Người duyệt kiểm lại số liệu và từ ngữ trước khi đăng."

## Đầu ra
Facebook dưới 250 chữ, câu dưới 20 chữ, tối đa 2 emoji. Zalo OA dưới 150 chữ.
Video: kịch bản 3 cảnh, có lời thoại.
Ví dụ mẫu (Elasten, Facebook): "Da bạn khô và kém đàn hồi? Sau 12 tuần, nghiên cứu lâm sàng
ghi nhận độ ẩm da tăng 28%… Thực phẩm này không phải là thuốc và không có tác dụng thay thế
thuốc chữa bệnh."
```

### Câu lệnh đóng gói cách làm thành skill

Dùng với cách Create with chat, sau khi đã làm tay vài lượt và kết quả đã ổn.

```text title="Đóng gói thành skill · tom-tat-tai-lieu"
Kết quả ổn rồi. Hãy đóng gói cách làm vừa rồi thành một skill tên tom-tat-tai-lieu, để lần sau
tôi chỉ cần nói "Tóm tắt tài liệu này" là bạn tự dùng skill.
Khi tôi đưa tài liệu, làm theo các bước:
1. Đọc toàn bộ tài liệu.
2. Xuất đúng cấu trúc:
   - TÓM TẮT NHANH: 3-5 gạch đầu dòng ý chính nhất.
   - Ý CHÍNH CHI TIẾT: theo từng mục/phần của tài liệu.
   - SỐ LIỆU, NGÀY THÁNG, HẠN CHÓT: mọi con số, mốc thời gian, cam kết.
   - ĐIỂM CẦN LƯU Ý / RỦI RO: câu vượt ranh giới pháp lý theo tầng sản phẩm,
     chỗ mâu thuẫn, chỗ mập mờ.
   - QUY TẮC: chỉ dùng thông tin trong tài liệu; không có thì ghi "Tài liệu không đề cập",
     không suy đoán; trích nguyên văn trong ngoặc kép khi cần bằng chứng.
```

## Lỗi hay gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| `description` mơ hồ | Gõ yêu cầu đúng loại việc mà skill không được gọi | Viết "Dùng khi…", liệt kê tình huống cụ thể và câu người dùng hay nói |
| Skill ôm nhiều việc | Kết quả lúc đúng lúc sai, các bước lẫn vào nhau | Tách thành nhiều skill nhỏ, nối thành chuỗi |
| Thiếu bước kiểm đầu vào | Thiếu thông tin vẫn viết, tự bịa giá và khuyến mãi | Bước 1 luôn là: thiếu thì hỏi lại |
| Không có ví dụ mẫu | Định dạng mỗi lần một kiểu | Thêm 1 ví dụ đầu ra đã điền số liệu |
| Sửa tay kết quả thay vì sửa skill | Lần nào cũng phải sửa cùng một chỗ | Sửa ngược vào skill, ghi "Sửa lần N" |
| Skill chỉ chạy đúng trên một ví dụ | Đổi tài liệu khác là hỏng | Làm phép thử: phiên mới, yêu cầu mới, không gọi tên skill |

## Nguồn chính thức

Tính năng ChatGPT thay đổi nhanh. Khi màn hình khác với trang này, đối chiếu lại với nguồn chính thức dưới đây.

- [Skills in ChatGPT – OpenAI Help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Build skills – learn.chatgpt.com](https://learn.chatgpt.com/docs/build-skills)
- [Build skills – OpenAI Developers](https://developers.openai.com/plugins/build/skills)

## Liên quan

- [Skill template](#skill-template): thư viện bản hướng dẫn viết sẵn theo phòng ban, dùng làm điểm khởi đầu cho skill của bạn.
- [Hướng dẫn tạo skill trên ChatGPT](#tao-skill-chatgpt): thao tác tạo, sửa và gọi skill.
- [Plugin](#plugin): nối ChatGPT với Gmail, Drive và đóng gói nhiều skill thành bộ công cụ của phòng.
- [Prompt](#prompt): công thức 4 phần, dùng khi việc chưa lặp lại đủ để đóng gói.
- [Instructions](#instructions): luật chung của phòng, skill không cần nhắc lại.
