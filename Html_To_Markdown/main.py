import re

dictionary_tags = {
    '<pre><code>': '    ',
    '<em>': '*',
    '<strong>': '**',
    '<h1>': '\n',
    '<h2>': '\n## ',
    '<h3>': '\n### ',
    '<h4>': '\n#### ',
    '<blockquote>': '\t',
    '<a': '',
    '<img': 'img',
    '<hr />': '\n - - -',
    '<ol>': '',
    '<li>': '* ',
    '<ul>': '',
    '<p>': '',
    '<code>': '`'
}

def convert_html_to_markdown(html_string, dictionary_tags):
    result = html_string

    for tag, markdown_tag in dictionary_tags.items():
        if tag in html_string:

            if tag == '<blockquote>':
                result = treatment_blockquote(result)

            elif tag == '<ol>':
                result = treatment_order_list(result)

            elif tag == '<a':
                result = treatment_link(result)

            elif tag == '<img':
                result = treatment_image(result)

            else:
                result = result.replace(tag, f'{markdown_tag}')

# Обработка случаев, когда теги закрываются
    result = result.replace('</code></pre>', '\n')
    result = result.replace('</em>', '*')
    result = result.replace('</strong>', '**')
    result = result.replace('</h1>', '\n===\n')
    result = result.replace('</h2>', ' ##\n')
    result = result.replace('</h3>', ' ###\n')
    result = result.replace('</a>', '')
    result = result.replace('</img>', '')
    result = result.replace('</p>', '')
    result = result.replace('</h4>', ' ####\n')
    result = result.replace('</hr>', '\n')
    result = result.replace('</br>', '\n')
    result = result.replace('</ol>', '\n')
    result = result.replace('</ul>', '')
    result = result.replace('</li>', '\n')
    result = result.replace('</code>', '`')
    return result

def treatment_blockquote(html):
    while ('<blockquote>' in html):
        start_tag = "<blockquote>"
        end_tag = "</blockquote>"
        start_index = html.find(start_tag) + len(start_tag)
        end_index = html.find(end_tag)
        container = html[start_index:end_index]
        result = html[:start_index - len(start_tag)]
        container = container.replace('<p>', '<').replace('\n', '\n<')
        result += container
        result += html[end_index + len(end_tag):]
        html = result

    return result

def treatment_order_list(html):
    while '<ol>' in html:
        start_tag = "<ol>"
        end_tag = "</ol>"
        start_index = html.find(start_tag) + len(start_tag)
        end_index = html.find(end_tag)
        container = html[start_index:end_index]
        result = html[:start_index - len(start_tag)]
        container = container.replace('</li>', '\n')
        container = container.split("<li>")[1:]
        for i, item in enumerate(container, start=1):
            result += f"{i}. {item}"
        result += html[end_index + len(end_tag):]
        html = result

    return result

def treatment_link(html):

    def find_href(string):
        res = str(re.findall(r'href=\"(.*?)\"', string))
        res = res.replace('[', '').replace(']', '').replace('\'', '')
        return res

    def find_name_link(string):
        res = str(re.findall(r'>(.*?)</a>', string)).replace('\'','')
        return res

    while '<a' in html:
        start_tag = "<a"
        end_tag = "</a>"
        start_index = html.find(start_tag) + len(start_tag)
        end_index = html.find(end_tag)
        container = html[start_index:end_index+len(end_tag)]
        result = html[:start_index - len(start_tag)]
        result += find_name_link(container) + '(' + find_href(container) + ')'
        result += html[end_index + len(end_tag):]
        html = result

    return result

def treatment_image(html):

    def find_src(string):
        res = str(re.findall(r'src=\"(.*?)\"', string))
        res = res.replace('[', '').replace(']', '').replace('\'', '')
        return res

    def find_name_img(string):
        res = str(re.findall(r'alt=\"(.*?)\"', string)).replace('\'','')
        return res

    while ('<img' in html):
        start_tag = "<img"
        end_tag = "/>"
        start_index = html.find(start_tag) + len(start_tag)
        end_index = html.find(end_tag)
        container = html[start_index:end_index+len(end_tag)]
        result = html[:start_index - len(start_tag)]
        result += '!' + find_name_img(container) + '(' + find_src(container) + ')'
        result += html[end_index + len(end_tag):]
        html = result

    return result

html_string = '<p><em>Slipknot</em>.</p>'
markdown_text = convert_html_to_markdown(html_string, dictionary_tags)
#print(markdown_text)
