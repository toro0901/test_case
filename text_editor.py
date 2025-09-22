class TextEditor:
    #文字列を大文字にして返すメソッド
    def to_upper(self, text):
        return text.upper()

    #文字列を逆順にして返すメソッド
    def reverse_text(self, text):
        return text[::-1]
        
    
editor = TextEditor()

print(editor.to_upper("python"))
print(editor.reverse_text("python"))