python docx

# 问题

issue

https://github.com/python-openxml/python-docx/issues/85



# 分析

### **[SebasSBM](https://github.com/SebasSBM)** commented [on Aug 16, 2014](https://github.com/python-openxml/python-docx/issues/85#issuecomment-52392327)

Thanks for your reply, scanny. I've just read it right now and started researching. The command you posted revealed an inner file structure, so I used the Ubuntu's tool for compressed files and noticed that all of them are XML files. I'm used to XML through I made apps for Android and I used some SOAP webservices, so XML is not new for me. Althrough, you have a point about it may become a steep learning curve, through the XML structure seems to be quite complex.Anyway, analyzing it I figured out some things in just less than half an hour: it seems that styles are defined in "styles.xml". There is also a file for the fonts, I just don't get why it seems there are 4 fonts in a test.docx file I created with LibreOffice in which I just used the default font and a hyperlink (which it seems it has it's own style defined), but I don't think extra fonts are relevant for now.I've taken a look to the "document.xml" file and noticed a difference between a normal paragraph and a hyperlink paragraph: this would be a normal paragraph structure:`                                    Prueba jajajjajajajaja     `On the other hand, this would be a hyperlink paragraph:`                                                                                http://www.google.com/             `In other words, it seems that the tags <w:hyperlink></w:hyperlink> contain the whole rich text structure that is supposed to be the hyperlink, with an id which would point to the actual URL stored somewhere in the XML file system, I guess. It seems quite interesting, unfortunately, I don't have much spare time lately, because I'm very busy with web developing.Anyways, if I ever have some spare time, I'd like to research how your python API reads the paragraphs, and make their .text() method able to recognize the <w:hyperlink> tag as text container. I'll keep you informed if I make any relevant progress.

👍 1

<details class="details-overlay details-reset dropdown hx_dropdown-fullscreen position-relative float-left d-inline-block reaction-popover-container reactions-menu js-reaction-popover-container" style="box-sizing: border-box; display: inline-block !important; position: relative; float: left !important;"><summary class="btn-link reaction-summary-item add-reaction-btn" aria-label="Add your reaction" aria-haspopup="menu" role="button" style="box-sizing: border-box; display: inline-block; cursor: pointer; padding: 9px 15px 7px; font-size: inherit; color: var(--color-text-link-primary); text-decoration: none; white-space: nowrap; user-select: none; background-color: initial; border: 0px; -webkit-appearance: none; opacity: 0; transition: opacity 0.1s ease-in-out 0s; float: left; line-height: 18px; list-style: none;"><svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM5 8a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zM5.32 9.636a.75.75 0 011.038.175l.007.009c.103.118.22.222.35.31.264.178.683.37 1.285.37.602 0 1.02-.192 1.285-.371.13-.088.247-.192.35-.31l.007-.008a.75.75 0 111.222.87l-.614-.431c.614.43.614.431.613.431v.001l-.001.002-.002.003-.005.007-.014.019a1.984 1.984 0 01-.184.213c-.16.166-.338.316-.53.445-.63.418-1.37.638-2.127.629-.946 0-1.652-.308-2.126-.63a3.32 3.32 0 01-.715-.657l-.014-.02-.005-.006-.002-.003v-.002h-.001l.613-.432-.614.43a.75.75 0 01.183-1.044h.001z"></path></svg></summary></details>

[![@SebasSBM](python%20docx.assets/7997164.jpg)](https://github.com/SebasSBM)

 

Author

### **[SebasSBM](https://github.com/SebasSBM)** commented [on Aug 17, 2014](https://github.com/python-openxml/python-docx/issues/85#issuecomment-52402264)

I think here's the problem: check the [class CT_P](https://github.com/python-openxml/python-docx/blob/master/docx/oxml/text.py#L32) at master/docx/oxml/text.py . If you take a look at the initial variables (lines 36 and 37) it seems this class (which I suppose it handles <w:p> objects) doesn't handle <w:hyperlink> objects at all. I think that's why text inside hyperlinks are not returned in the [text](https://github.com/python-openxml/python-docx/blob/master/docx/oxml/text.py#L231) property. I don't know much about the structure of the whole project -not yet-, but I think this is the way to go to resolve the problem.

# docx内部实现使用了大量的meta programming，搞得很难分析

比如如下callstack

```python
_add_list_getter (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\oxml\xmlchemy.py:325)
populate_class_members (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\oxml\xmlchemy.py:557)
__init__ (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\oxml\xmlchemy.py:105)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\oxml\document.py:26)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\oxml\__init__.py:75)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\opc\part.py:13)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\opc\package.py:9)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\package.py:9)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\api.py:14)
<module> (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\docx\__init__.py:3)
<module> (g:\sw\Python36\test_docx.py:1)
_run_code (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\runpy.py:86)
_run_module_code (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\runpy.py:96)
run_path (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\runpy.py:263)
_run_code (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\runpy.py:86)
_run_module_as_main (d:\Users\cutep\AppData\Local\Programs\Python\Python38-32\Lib\runpy.py:193)
```

具体就是如果class从BaseOxmlElement继承

```python
class CT_Body(BaseOxmlElement):
    """
    ``<w:body>``, the container element for the main document story in
    ``document.xml``.
    """
    p = ZeroOrMore('w:p', successors=('w:sectPr',))
    tbl = ZeroOrMore('w:tbl', successors=('w:sectPr',))
    sectPr = ZeroOrOne('w:sectPr', successors=())
```

而class BaseOxmlElement实现了

```python
BaseOxmlElement = MetaOxmlElement(
    'BaseOxmlElement', (etree.ElementBase,), dict(_OxmlElementBase.__dict__)
)
```



所以最终跑到

```python
class MetaOxmlElement(type):
    """
    Metaclass for BaseOxmlElement
    """
    def __init__(cls, clsname, bases, clsdict):
        dispatchable = (
            OneAndOnlyOne, OneOrMore, OptionalAttribute, RequiredAttribute,
            ZeroOrMore, ZeroOrOne, ZeroOrOneChoice
        )
        for key, value in clsdict.items():
            if isinstance(value, dispatchable):
                value.populate_class_members(cls, key)
```

其中clsdict内容如下

![image-20201018114652604](python%20docx.assets/image-20201018114652604.png)

也就是CT_Body中声明的变量p，。。。的如下函数被调用

```python
class ZeroOrMore(_BaseChildElement):
    """
    Defines an optional repeating child element for MetaOxmlElement.
    """
    def populate_class_members(self, element_cls, prop_name):
        """
        Add the appropriate methods to *element_cls*.
        """
        super(ZeroOrMore, self).populate_class_members(
            element_cls, prop_name
        )
        self._add_list_getter()
        self._add_creator()
        self._add_inserter()
        self._add_adder()
        self._add_public_adder()
        delattr(element_cls, prop_name)
```

而_add_list_getter代码如下，会生成相关的property,比如p_lst,...

```python
    def _add_list_getter(self):
        """
        Add a read-only ``{prop_name}_lst`` property to the element class to
        retrieve a list of child elements matching this type.
        """
        prop_name = '%s_lst' % self._prop_name
        property_ = property(self._list_getter, None, None)
        setattr(self._element_cls, prop_name, property_)
```



```python
class Paragraph(Parented):
    里面包含self._p，类型为class CT_P(BaseOxmlElement)
    
```

## 为什么`CT_P`可以 `for child in self`？

# temp solution

增加text_2属性

```python
class Paragraph(Parented):
    @property
    def text(self):
        """
        String formed by concatenating the text of each run in the paragraph.
        Tabs and line breaks in the XML are mapped to ``\\t`` and ``\\n``
        characters respectively.

        Assigning text to this property causes all existing paragraph content
        to be replaced with a single run containing the assigned text.
        A ``\\t`` character in the text is mapped to a ``<w:tab/>`` element
        and each ``\\n`` or ``\\r`` character is mapped to a line break.
        Paragraph-level formatting, such as style, is preserved. All
        run-level formatting, such as bold or italic, is removed.
        """
        text = ''
        for run in self.runs:
            text += run.text
        return text
    @property
    def text_2(self):
        """
        String formed by concatenating the text of each run in the paragraph.
        Tabs and line breaks in the XML are mapped to ``\\t`` and ``\\n``
        characters respectively.

        Assigning text to this property causes all existing paragraph content
        to be replaced with a single run containing the assigned text.
        A ``\\t`` character in the text is mapped to a ``<w:tab/>`` element
        and each ``\\n`` or ``\\r`` character is mapped to a line break.
        Paragraph-level formatting, such as style, is preserved. All
        run-level formatting, such as bold or italic, is removed.
        """
        text = self._p.text_2
        return text
    

class CT_P(BaseOxmlElement):
    """
    ``<w:p>`` element, containing the properties and text for a paragraph.
    """
    pPr = ZeroOrOne('w:pPr')
    r = ZeroOrMore('w:r')
    hyperlink = ZeroOrMore('w:hyperlink')

    @property
    def text_2(self):
        """
        A string representing the textual content of this run, with content
        child elements like ``<w:tab/>`` translated to their Python
        equivalent.
        """
        text = ''
        for child in self:
            if child.tag == qn('w:t'):
                t_text = child.text
                text += t_text if t_text is not None else ''
            elif child.tag == qn('w:hyperlink'):
                for c in child:
                    t_text = c.text
                    text += t_text if t_text is not None else ''
            elif child.tag == qn('w:r'):
                t_text = child.text
                text += t_text if t_text is not None else ''
            elif child.tag == qn('w:tab'):
                text += '\t'
            elif child.tag in (qn('w:br'), qn('w:cr')):
                text += '\n'
        return text    
```

