from setuptools import setup, find_packages

setup(
    name='PDF 2 NER',
    version='0.1.0',
    author='Fer Aguirre',
    description='Web application to convert scanned PDF files to text-based data and apply Named Entity Recognition (NER) to extract entities in Spanish',
    python_requires='>=3',
    license='MIT License',
    packages=find_packages(),
)