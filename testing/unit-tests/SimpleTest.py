

import re
import typing

from jk_testing2 import *

import jk_regexhelper






@TestGroup(testCaseOrder=EnumTestCaseOrder.AS_DEFINED)
class SimpleTest:

	def __init__(self) -> None:
		pass
	#

	@InitializeTests()
	def init(self, ctx:TestContext):
		pass
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	@TestCase()
	def testCase_compileToRegExStrList_single(self, ctx:TestContext):
		Assert.isEqual(		jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegExStrList("*.foo"),		[ ".*\\.foo", ]		)
	#

	@TestCase()
	def testCase_compileToRegExStrList_multiple(self, ctx:TestContext):
		Assert.isEqual(		jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegExStrList("*.foo|*.bar"),		[ ".*\\.foo", ".*\\.bar", ]		)
		Assert.isEqual(		jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegExStrList([ "*.foo", "*.bar" ]),		[ ".*\\.foo", ".*\\.bar", ]		)
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	@TestCase()
	def testCase_compileToRegExStr_single(self, ctx:TestContext):
		Assert.isEqual(		jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegExStr("*.foo"),		"(.*\\.foo)"		)
	#

	@TestCase()
	def testCase_compileToRegExStr_multiple(self, ctx:TestContext):
		Assert.isEqual(		jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegExStr("*.foo|*.bar"),		"(.*\\.foo)|(.*\\.bar)"		)
		Assert.isEqual(		jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegExStr([ "*.foo", "*.bar" ]),		"(.*\\.foo)|(.*\\.bar)"		)
	#

	# --------------------------------------------------------------------------------------------------------------------------------


	@TestCase()
	def testCase_compileToRegEx_multiple(self, ctx:TestContext):
		regex = jk_regexhelper.FileNamePatternToRegExCompiler.compileToRegEx([ "*.foo", "*.bar" ])

		m = regex.match("abc.def")
		Assert.isNone(m)

		m = regex.match("abc.foo")
		Assert.isNotNone(m)

		m = regex.match("abc.bar")
		Assert.isNotNone(m)
	#

	# --------------------------------------------------------------------------------------------------------------------------------

#


