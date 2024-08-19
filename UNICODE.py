unicode_text = "Xin ch\u00E0o th\u1EBF gi\u1EDBi!"
vietnamese_text = ''.join(unicode_to_vietnamese.get(char, char) for char in unicode_text)
print(vietnamese_text)