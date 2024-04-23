# Streamlit 的使用方式
## 目的 
* 由於公司的活動需要建立一個數據Dashboard，因此才找到這個套件，打算用它來建立一個Dashboard

## 安裝 & 執行
* 安裝
```
pip install streamlit
```
* 執行，並指定Port Number
```
streamlit run <python file path> --server.port xxxx
```
* 停止執行，Control/Command + C

## 創建程式
### Import 用到的套件
```
import time
import streamlit as st

```