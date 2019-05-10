from setuptools import setup

setup(
    name="extract_frames",
    version="1.0",
    py_modules=["extract_frames"],
    install_requires=[
        "Click",
        "xmltodict"
    ],
    entry_points="""
        [console_scripts]
        extract-frames=extract_frames:extract_frames
    """,
)
