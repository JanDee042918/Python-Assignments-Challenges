from setuptools import setup

#Call the setup method from setup tools.
#Provide data about the program to be distributed.
#py_modules is a list - so it can contai n multiple files.
setup(
    name="parse_ip",
    version = "1.0",
    description = "Parses and returns the ip address.",
    author = "John Matas",
    author_email = "jmatas@rrc.ca",
    py_modules = ["parse_ip"]
)