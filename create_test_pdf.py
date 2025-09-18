#!/usr/bin/env python3
"""
创建测试PDF文件
"""

import pymupdf

def create_test_pdf():
    """创建一个包含英文文本的测试PDF"""
    
    # 创建新文档
    doc = pymupdf.open()
    
    # 添加页面
    page = doc.new_page(width=595, height=842)  # A4尺寸
    
    # 添加标题
    page.insert_text((50, 50), "BabelDOC Translation Test", fontsize=20, color=(0, 0, 0))
    
    # 添加测试文本
    test_text = [
        "This is a test document for BabelDOC translation.",
        "It contains multiple paragraphs with English text.",
        "The translation should convert this to Chinese.",
        "",
        "Here are some technical terms:",
        "- Machine Learning",
        "- Artificial Intelligence", 
        "- Natural Language Processing",
        "- Computer Vision",
        "",
        "This document also contains some numbers: 123, 456, 789",
        "And some special characters: @#$%^&*()",
        "",
        "The end of the test document."
    ]
    
    y_position = 100
    for line in test_text:
        if line:  # 非空行
            page.insert_text((50, y_position), line, fontsize=12, color=(0, 0, 0))
        y_position += 20
    
    # 保存PDF
    output_path = "test_document.pdf"
    doc.save(output_path)
    doc.close()
    
    print(f"✅ 测试PDF已创建: {output_path}")
    return output_path

if __name__ == "__main__":
    create_test_pdf()
