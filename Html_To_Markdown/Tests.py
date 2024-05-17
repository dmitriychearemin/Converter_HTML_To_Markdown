import unittest
import unittest
import os
import sys
import main
class Test_Convert(unittest.TestCase):

    def test_empty(self):
        html = ""
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = ""
        self.assertEqual(result, expected)

    def test_on_pre_code(self):
        html = "<pre><code>Slipknot</code></pre>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "    Slipknot\n"
        self.assertEqual(result, expected)

    def test_on_italic(self):
        html = "<p><em>Slipknot</em>.</p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "*Slipknot*."
        self.assertEqual(result, expected)

    def test_on_bold(self):
        html = "<p><strong>Slipknot</strong>.</p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "**Slipknot**."
        self.assertEqual(result, expected)

    def test_on_bold_italic(self):
        html = "<p><em><strong>Slipknot</strong></em>.</p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "***Slipknot***."
        self.assertEqual(result, expected)

    def test_on_header1(self):
        html = "<h1>Slipknot</h1>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "\nSlipknot\n===\n"
        self.assertEqual(result, expected)

    def test_on_header2(self):
        html = "<h2>Slipknot</h2>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "\n## Slipknot ##\n"
        self.assertEqual(result, expected)

    def test_on_header3(self):
        html = "<h3>Slipknot</h3>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "\n### Slipknot ###\n"
        self.assertEqual(result, expected)

    def test_on_header4(self):
        html = "<h4>Slipknot</h4>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "\n#### Slipknot ####\n"
        self.assertEqual(result, expected)

    def test_on_blockquote(self):
        html = "<blockquote><p>Slipknot\nKorn</p></blockquote>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "<Slipknot\n<Korn"
        self.assertEqual(result, expected)

    def test_on_order_list(self):
        html = "<ol><li>Slipknot</li><li>Korn</li></ol>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "1. Slipknot\n2. Korn\n"
        self.assertEqual(result, expected)

    def test_on_not_order_list(self):
        html = "<ul><li>Slipknot</li><li>Korn</li></ul>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "* Slipknot\n* Korn\n"
        self.assertEqual(result, expected)

    def test_on_link(self):
        html = "<p><a href=\"http://url.com/\">example</a></p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "[example](http://url.com/)"
        self.assertEqual(result, expected)

    def test_on_image(self):
        html = "<p><img src=\"/path/img.jpg\" alt=\"img\"/></p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "![img](/path/img.jpg)"
        self.assertEqual(result, expected)

    def test_on_code(self):
        html = "<p><code>import</code></p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "`import`"
        self.assertEqual(result, expected)

    def test_on_big_html_text(self):
        html = "<p><code>impotr</code><em>italic</em>," \
               "<strong>bold</strong></p><h1>Header</h1><p><baaaaa<gaaaaa</p><p><img src=\"/path/img.jpg\" alt=\"alt " \
               "text\" title="" /></p>"
        result = main.convert_html_to_markdown(html, main.dictionary_tags)
        expected = "`impotr`*italic*,**bold**\nHeader\n===\n<baaaaa<gaaaaa![alt text](/path/img.jpg)"
        self.assertEqual(result, expected)



'''print('--------\n'+result + '--------')
print('--------\n'+expected + '--------')'''


if __name__ == "__main__":
    unittest.main()
