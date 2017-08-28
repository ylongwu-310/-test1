# -*- coding: utf-8 -*-
"""
用于测试环境的全局配置
"""
import os
from settings import BASE_DIR


# ===============================================================================
# 数据库设置, 测试环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),                      # 数据库名 (默认与APP_ID相同)
    }
}
