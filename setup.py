from setuptools import setup, find_packages

setup(
    name='data_cook',  # Tên thư viện
    version='0.1.0',    # Phiên bản
    author='Cookiescooker', # Tên tác giả
    author_email='vanhaminhquan2406@gmail.com',  # Email
    description='An data handle library',  # Mô tả ngắn
    long_description=open('README.md').read(),  # Mô tả dài (đọc từ README.md)
    long_description_content_type='text/markdown',  # Định dạng của mô tả dài
    url='https://github.com/AutoCookies/data_py',  # URL repository
    packages=find_packages(),  # Tự động tìm các package
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'opencv-python',
        'scikit-image'
    ],  # Các dependencies (ví dụ: ['numpy', 'pandas'])
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Phiên bản Python yêu cầu
)