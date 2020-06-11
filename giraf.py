Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> text = """キリンは大昔から _複数名詞_ の興味の対象でした。
キリンは _複数名詞_ の中で一番背が高いですが、科学者たちはそのような
長い _体の一部_ をどうやって獲得したのか説明できません。
キリンの身長は _数値_ _単位_ 近くあり、その高さのほとんどは
脚と _体の一部_ によるものです。
"""
>>> def mad_libs(mls):
	"""
	:param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は後を２つの
	アンダースコアで挟んでください。ヒントの単語にはアンダースコアを含めないでください。
	_hint_hint_ はだめです。 _hint_ はOKです。
	"""

	
>>>  def mad_libs(mls):
	"""
	:param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は後を２つの
	アンダースコアで挟んでください。ヒントの単語にはアンダースコアを含めないでください。
	_hint_hint_ はだめです。 _hint_ はOKです。
	
SyntaxError: unexpected indent
>>> def mad_libs(mls):
	"""
	:param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は後を２つの
	アンダースコアで挟んでください。ヒントの単語にはアンダースコアを含めないでください。
	_hint_hint_ はだめです。 _hint_ はOKです。
	"""
	hints = re.findall("_.*?_", mls)
	if hint is not None:
		for word in hints:
			q = "{}を入力:".format(word)
			new = input(q)
			mls = mls.replace(word, new, 1)
		print('\n')
		mls = mls.replace("\n", "")
		print(mls)
	else:
		print("引数mlsが無効です。")

		
>>> mad_libs(text)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    mad_libs(text)
  File "<pyshell#28>", line 8, in mad_libs
    if hint is not None:
NameError: name 'hint' is not defined
>>> def mad_libs(mls):
	"""
	:param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は後を２つの
	アンダースコアで挟んでください。ヒントの単語にはアンダースコアを含めないでください。
	_hint_hint_ はだめです。 _hint_ はOKです。
	"""
	hints = re.findall("_.*?_", mls)
	if hints is not None:
		for word in hints:
			q = "{}を入力:".format(word)
			new = input(q)
			mls = mls.replace(word, new, 1)
		print('\n')
		mls = mls.replace("\n", "")
		print(mls)
	else:
		print("引数mlsが無効です。")

		
>>> mad_libs(text)
_複数名詞_を入力:人々
_複数名詞_を入力:動物
_体の一部_を入力:首
_数値_を入力:７
_単位_を入力:m
_体の一部_を入力:首


キリンは大昔から 人々 の興味の対象でした。キリンは 動物 の中で一番背が高いですが、科学者たちはそのような長い 首 をどうやって獲得したのか説明できません。キリンの身長は ７ m 近くあり、その高さのほとんどは脚と 首 によるものです。
>>> 
