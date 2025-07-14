from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
import qrcode

# ✅ フォント登録（Windows環境前提）
pdfmetrics.registerFont(TTFont('MSGothic', 'C:\\Windows\\Fonts\\msgothic.ttc'))

# 📄 出力ファイル名
pdf_filename = "fujiisenyou_qr_intro.pdf"

# 📦 QRコード生成
qr_link = "https://github.com/NiGHTS-PIKO/fujiisenyou"
qr_img = qrcode.make(qr_link)
qr_img_path = "github_qr.png"
qr_img.save(qr_img_path)

# 📘 テキスト構成
main_text = """GitHubでも公開中！
この研究に火を灯してくださった藤井さんへ感謝を込めて、  
“最高すぎる”構文に関する語用論的分析記録を共有いたします。

以下のQRコードから、専用リポジトリへアクセスできます："""

one_liner = "つまり、言葉の沼は笑いと論理の両方で掘れるということです。"

# 📐 PDFレイアウト設定
doc = SimpleDocTemplate(pdf_filename, pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm,
                        topMargin=2*cm, bottomMargin=2*cm)

styles = {
    'Main': ParagraphStyle(name='Main', fontName='MSGothic',
                           fontSize=11, leading=16, spaceAfter=14),
    'OneLiner': ParagraphStyle(name='OneLiner', fontName='MSGothic',
                               fontSize=10.5, leading=14, alignment=1, textColor='gray')
}

elements = []

# 文章挿入
elements.append(Paragraph(main_text, styles['Main']))
elements.append(Image(qr_img_path, width=5*cm, height=5*cm))
elements.append(Spacer(1, 0.5*cm))
elements.append(Paragraph(one_liner, styles['OneLiner']))

# PDF作成
doc.build(elements)
print("✅ QR付き紹介PDFが完成しました！ファイル:", pdf_filename)