import re
import sys

class MDConverter:
    def __init__(self):
        self.in_list = False
    
    def convert_headers(self, line):
        header_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            return f"<h{level}>{text}</h{level}>"
        return line

    def convert_bold(self, line):
        return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)

    def convert_italic(self, line):
        return re.sub(r'\*(.+?)\*', r'<i>\1</i>', line)

    def convert_links(self, line):
        return re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

    def convert_images(self, line):
        return re.sub(r'^!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', line)

    def handle_list_item(self, line):
        list_match = re.match(r'^\d+\.\s+(.+)$', line)
        if list_match:
            if not self.in_list:
                self.in_list = True
                return f"<ol>\n<li>{list_match.group(1)}</li>"
            return f"<li>{list_match.group(1)}</li>"
        if self.in_list:
            self.in_list = False
            return "</ol>" + line
        return line

    def convert(self, text):
        result = []
        for line in text.split('\n'):
            line = self.handle_list_item(line)
            if not line.startswith('<li>') and not line.startswith('</ol>'):
                line = self.convert_headers(line)
                line = self.convert_bold(line)
                line = self.convert_italic(line)
                line = self.convert_images(line)
                line = self.convert_links(line)
            result.append(line)
        
        if self.in_list:
            result.append("</ol>")
            self.in_list = False
            
        return '\n'.join(result)

def main():
    if len(sys.argv) != 3:
        print("Usage: python MDtoHTML.py input.md output.html")
        sys.exit(1)
        
    converter = MDConverter()
    with open(sys.argv[1], 'r') as f:
        text = f.read()
    
    html = converter.convert(text)
    
    with open(sys.argv[2], 'w') as f:
        f.write(html)

if __name__ == "__main__":
    main()
