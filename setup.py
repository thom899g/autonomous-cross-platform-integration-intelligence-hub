from setuptools import setup, find_packages

setup(
    name="APILink",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pika',
        'prometheus-client',
        'stable-baselines3',
        'docstring-generator',
    ],
)