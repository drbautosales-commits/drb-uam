# -*- coding: utf-8 -*-
import base64
import os
import re

# 이미지 폴더 경로
image_folder = r"X:\이영근\Cursor\uam\aircraft\images"
html_file = r"X:\이영근\Cursor\uam\aircraft\uam-aircraft-research.html"
output_file = r"X:\이영근\Cursor\uam\aircraft\uam-aircraft-research-standalone.html"

# 이미지 파일들의 MIME 타입 매핑
mime_types = {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.avif': 'image/avif',
    '.svg': 'image/svg+xml'
}

def get_base64_image(image_path):
    """이미지 파일을 Base64로 변환"""
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        ext = os.path.splitext(image_path)[1].lower()
        mime_type = mime_types.get(ext, 'image/jpeg')
        
        base64_data = base64.b64encode(image_data).decode('utf-8')
        return f"data:{mime_type};base64,{base64_data}"
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return None

def convert_html_to_standalone():
    """HTML 파일의 이미지 경로를 Base64 데이터 URI로 변환"""
    
    # HTML 파일 읽기
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # images/ 폴더의 이미지 파일 목록
    image_files = os.listdir(image_folder)
    
    # 각 이미지 파일에 대해 Base64 변환 및 치환
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        
        if os.path.isfile(img_path):
            base64_data = get_base64_image(img_path)
            
            if base64_data:
                # HTML에서 이미지 경로를 찾아 Base64로 치환
                # src="images/파일명" 패턴
                old_pattern = f'images/{img_file}'
                html_content = html_content.replace(old_pattern, base64_data)
                
                # src='images/파일명' 패턴도 처리
                old_pattern_single = f"images/{img_file}"
                html_content = html_content.replace(old_pattern_single, base64_data)
                
                print(f"✅ Converted: {img_file}")
    
    # Standalone HTML 파일 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 파일 크기 계산
    file_size = os.path.getsize(output_file) / (1024 * 1024)  # MB
    
    print(f"\n🎉 Standalone HTML 파일이 생성되었습니다!")
    print(f"📄 파일: {output_file}")
    print(f"📦 크기: {file_size:.2f} MB")
    print(f"\n이 파일 하나만 공유하면 모든 이미지가 포함됩니다!")

if __name__ == "__main__":
    convert_html_to_standalone()


