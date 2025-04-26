from setuptools import setup, find_packages

setup(
    name='psupbin',  # Tên thư viện của bạn
    version='1.0.0',  # Phiên bản đầu tiên
    description='Binary operations: OR, AND, XOR, NOT for binary',
    author='phannoiershit',  # Tên tác giả
    author_email='buiphan022109@gmail.',  # Email tác giả
    url='https://github.com/phannoiershit/psupbin',  # URL GitHub project
    packages=find_packages(),  # Tự động tìm các package con
    install_requires=[],  # Danh sách thư viện phụ thuộc (nếu có)
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3',
)
