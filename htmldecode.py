import sublime, sublime_plugin

# Created by pberezvay
# 2013.09.18

class htmldecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		regions = view.sel()
		if len(regions) > 1 or not regions[0].empty():
			for region in view.sel():
				if not region.empty():
					s = view.substr(region)
					s = s.replace('&lt;','<').replace('&gt;','>').replace('&quot;','"')
					view.replace(edit, region,s)
		else:
			alltextreg = sublime.Region(0, view.size())
			s = view.substr(alltextreg)
			s =	s.replace('&lt;','<').replace('&gt;','>').replace('&quot;','"')
			view.replace(edit, alltextreg, s)

class htmlencodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		regions = view.sel()
		if len(regions) > 1 or not regions[0].empty():
			for region in view.sel():
				if not region.empty():
					s = view.substr(region)
					s =	s.replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace('\r','').replace('\n','').replace('\t','')
					view.replace(edit, region,s)
		else:
			alltextreg = sublime.Region(0, view.size())
			s = view.substr(alltextreg)
			s =	s.replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace('\r','').replace('\n','').replace('\t','')
			view.replace(edit, alltextreg, s)
