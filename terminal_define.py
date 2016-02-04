#!/usr/bin/env python
import webbrowser
url='http://www.merriam-webster.com/dictionary/'
word=raw_input('Enter Word to be Define: ? ')
webbrowser.open_new_tab(url+word)
