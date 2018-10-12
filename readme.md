## python 代码生成器
### 1.目录说明

`Output/` 输出目录
`Tpl/`  模板目录
`generate.py` 生成器
`setting.json` 生成器配置文件

### 2.使用说明
根据setting.json里面的配置文件生成代码

    python generate.py -i setting.json 


#### 参数说明

    C:\python_project\cyd-scrapy\web\generate-scrapy>python generate.py -h
    usage: generate.py [-h] [--input [INPUT]]

    genetate setting

    optional arguments:
    -h, --help            show this help message and exit
    --input [INPUT], -i [INPUT]


### 3.配置文件说明
| 键值  |  描述 |
|---|---|
|  name |  配置文件名称 |
|  output |  代码生成目录 |
|  tpl |  指定对应的模板路径 |
|  list |  代码生成器的主要内容 |
说明:list里面的url,name等对应模板里面的${url},${name}

### 配置文件例子
```json
{
    "name": "demo",
    "output": "./Output/", 
    "tpl": "./Tpl/scrapy.tpl", 
    "list": [
        {
            "url": "http://fgw.hunan.gov.cn/xxgk_70899/tzgg/", 
            "host": "fgw.hunan.gov.cn", 
            "name": "sfzhggwyh", 
            "title": "省发展和改革委员会"
        }
    ]
}
```

