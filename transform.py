#!/anaconda3/bin/python
import re
import os


class toc:
    def __init__(self, raw):
        self._raw = raw
        self.title = self.title_format()
        self.link = self.link_format()
        self.depth = self.depth_format()
        self.markdown = ''
        if self.depth <= 2:
            self.para = ''
        self.file = ''

    def title_format(self):
        return re.findall('#+\s(.+)', self._raw)[0]

    def link_format(self):
        link = self.title.lower().replace(' ', '-')
        link = re.sub('[^\w-]', '', link)
        return link

    def depth_format(self):
        return len(self._raw.split(' ')[0])

    def markdown_format(self):
        mark_form = '	' * (self.depth-1) + '* [' + self.title + ']'
        mark_link = '(' + self.file + '#' + self.link + ')\n'
        return mark_form + mark_link


try:
    filename = [filename for filename in os.listdir(os.getcwd()) if filename.endswith(
        '.md') and filename not in ['SUMMARY.md', 'README.md']][0]
except:
    print('Markdown file not fund.')
    exit(0)

data = list()
data_c = list()
with open(filename) as handle:
    raw = handle.readlines()
    for i in raw:
        if re.match('(^#{1,2}\s.+)', i):
            data.append(toc(i.strip('\n')))
        if re.match('(^#+\s.+)', i):
            data_c.append(toc(i.strip('\n')))
        data[-1].para += i

for i in data:
    for j in data_c:
        if i.link == j.link:
            j.para = i.para

root = ''
summary = ''
file = ''
for item in data_c:
    if item.depth == 1:
        path = item.link
        if not os.path.exists(path):
            os.mkdir(path)
        root = path
        with open(path + '/README.md', 'w') as handle:
            handle.write(item.para)
        file = path + '/README.md'
        item.file = file
    elif item.depth == 2:
        path = root
        with open(path + '/' + item.link + '.md', 'w') as handle:
            handle.write(item.para)
        file = path + '/' + item.link + '.md'
        item.file = file
    else:
        item.file = file
    item.markdown = item.markdown_format()
    summary += item.markdown

with open('SUMMARY.md', 'w') as handle:
    handle.write(summary)