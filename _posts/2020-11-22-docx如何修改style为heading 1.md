docx如何修改style为heading 1

https://python-docx.readthedocs.io/en/latest/user/styles-using.html



```
>>> from docx.enum.style import WD_STYLE_TYPE

>>> document = Document()
>>> styles = document.styles
s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH


paragraph = document.add_paragraph()
paragraph.style = document.styles['Heading 1']

document.styles.add_style('Citation', WD_STYLE_TYPE.PARAGRAPH)
```



Briefly, latent styles cannot be applied to a paragraph (or other object) in `python-pptx`. Only defined styles available in `document.styles` can be applied. So you either restrict yourself to styles already available in the document, or add any desired styles before attempting to use them.



