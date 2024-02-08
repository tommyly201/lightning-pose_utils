from setuptools import setup, find_packages  # Preferred over distutils 

setup(
    name='lightningpose_utils',  # Update package name
    version='0.1.0',  # Start with an initial version
    description='Utilities to streamline Lightning Pose workflows',  
    author='Tommy Ly',  # Update author info
    author_email='tommyly201@gmail.com', 
    url='https://github.com/tommyly201/lightningpose_utils',  # Your repo URL
    install_requires=[
        'lightning-pose',  # Your main dependency
        # Add others like 'numpy', 'opencv-python' when needed
    ],
    packages=find_packages(),  # Automatically detects your package structure
)
