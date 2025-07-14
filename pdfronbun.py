from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
import textwrap

# ✅ MS Gothicフォント登録（Windows環境）
pdfmetrics.registerFont(TTFont('MSGothic', 'C:\\Windows\\Fonts\\msgothic.ttc'))

# 📄 出力ファイル名
pdf_filename = "sugiru_acknowledgement_fujii_final.pdf"

# 📝 藤井さんへの謝辞文（着火バージョン）
acknowledgement_text = """本研究の原点は、同僚・藤井さんが発したたった一言――「最高すぎるとは何か？」にあります。

その問いかけは、何気ない雑談の中に唐突に現れたにもかかわらず、私の中で静かに、しかし確実に火を灯しました。普段使っていたはずの表現に、こんなにも深い意味を問うことができるのか？ その瞬間から、“すぎる構文”に関する語用論的研究が始まりました。

研究を進めていくうちに、「最高すぎる」という言葉が、単なる誇張ではなく、感情の濃度や主観的リアリティを伴った言語現象であることが明らかになっていきました。そしてその出発点には、藤井さんの好奇心と鋭さが確かに存在していたのです。

心より感謝を申し上げます。
"""

# 📐 PDFレイアウト設定
doc = SimpleDocTemplate(pdf_filename, pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm,
                        topMargin=2*cm, bottomMargin=2*cm)

style = ParagraphStyle(name='Body',
                       fontName='MSGothic',
                       fontSize=10.5,
                       leading=14,
                       spaceAfter=10)

elements = []

# 段落ごとに整形
for para in acknowledgement_text.strip().split("\n\n"):
    wrapped_para = "<br/>".join(textwrap.wrap(para, width=90))
    elements.append(Paragraph(wrapped_para, style))
    elements.append(Spacer(1, 0.4*cm))

# PDF生成
doc.build(elements)
print("✅ 藤井さんへの謝辞PDF（着火バージョン）完成！ファイル:", pdf_filename)