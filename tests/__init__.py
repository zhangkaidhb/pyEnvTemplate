"""tests 包占位：用于阻断外部 site-packages 中 tests 的误发现，且本仓库不在安装阶段运行单元测试。"""
import unittest


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    return unittest.TestSuite()


