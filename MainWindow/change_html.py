#!/usr/bin/env python3
#-*-coding:utf-8-*-
import re

def change_html(self):
	"""when any edit box is changed, change the content shown in result_webView."""
	current_html_code = self.html_textedit.text()
	current_css_code = self.css_textedit.toPlainText()
	current_js_code = self.js_textedit.toPlainText()
	style_and_js_part = '<style>\n' + current_css_code + '</style>\n' + \
								'<script type="text/javascript">\n' + \
								current_js_code + '\n</script>'
	html_with_head = re.match(r"(.*?)<//head>(.*)",current_html_code)
	if html_with_head:
		total_html = html_with_head[0] +  style_and_js_part	+ html_with_head[1]
	else:
		total_html = "<head>" + style_and_js_part + "</head>\n" + current_html_code
	# debug only
	#print(total_html)
	
	self.result_webView.setHtml(total_html)
