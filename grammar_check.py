import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    matches = tool.check(text) 
    return [{"message": m.message, "sentence": m.context} for m in matches[:10]]
