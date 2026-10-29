#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # 确保项目根目录被添加到 PYTHONPATH
    project_path = os.path.dirname(os.path.abspath(__file__))  # 获取 manage.py 所在目录的绝对路径
    sys.path.append(project_path)  # 添加项目根目录到 PYTHONPATH

    # 设置默认的 Django 配置模块
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backdoorbench.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
