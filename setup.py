from setuptools import setup, find_packages

setup(
    name='lang',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'ply',
    ],
    entry_points={                   # Opcional: para definir scripts de consola
        'console_scripts': [
            'lang = lang_op.main:main',
        ],
    },
    author='Alvaro Caballero y Yael Contreras',
    author_email='acaballero31@alumnos.uax.mx',
    description='Lenguaje interactivo para operaciones con lenguajes',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ZiftK/lang'
)
