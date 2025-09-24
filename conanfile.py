from conan import ConanFile
from conan.tools.files import copy
import os
import subprocess
import sys
import re

class projectNameConan(ConanFile):
    name = "projectName"
    version = "1.0.0"
    user = "kai"
    channel = "stable"
    # Optional metadata
    license = "ZK_License"
    author = "Kai.Zhang zhangkaid6@gmail.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Expand a topic json file to a lecture json file through llm"
    topics = ("json", "processor", "llm", "python", "script", "automation")
    generators = "cmake","json"
    # Binary configuration
    settings = "os", "arch"
    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "*.py", "requirements.txt"
    # Required dependencies
    tools_requires = "cmake/[>=3.15]","json"
    requires = "python_venv/[~1.0.0]@kai/stable"
    python_version = "3.11.0b4"
    python_requires = "python_venv/[~1.0.0]@kai/stable"
    python_requires_extend = "python_venv.python_venv_generator"
    def __init__(self, *args, **kwargs):
        super(projectNameConan, self).__init__(*args, **kwargs)
    def generate(self):
        pass
    def build(self):

        pass
    # def package(self):
    #     copy(self, "src/*", self.build_folder, self.package_folder)
    #     copy(self, "*", os.path.join(self.build_folder,"venv_lib"), os.path.join(self.package_folder,"deps"))

    # def package_info(self):
    #     self.user_info.VENV_PYTHON_LIB = os.path.join(self.package_folder, "deps")
    #     self.user_info.VENV_LIST = self.python_version_list
    #     print(f"Available python venv list from {self.name}/{self.version}: {self.user_info.VENV_LIST}")
    def package(self):
        copy(self, "*", os.path.join(self.build_folder,".venv"), os.path.join(self.package_folder,"deps",".venv"))
        print(f"Python {self.python_version} .venv packaged")    
    def package_info(self):
        # 设置环境变量
        self.env_info.PYTHON_EXE = os.path.join(self.package_folder,"deps",".venv","Scripts","python.exe") if os.name == "nt" else os.path.join(self.package_folder,"deps",".venv","bin","python")
        self.env_info.VENV_PYTHON = os.path.join(self.package_folder,"deps",".venv")
