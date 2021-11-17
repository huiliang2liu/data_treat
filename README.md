# 数据简单处理

## 使用说明
   需要安装python3和pandas  
   python3 deal.py 批处理文件为脚本目录下batch.json  
   python3 deal.py ./batch.json 批处理文件为./batch.json

## 批处理文件说明

### batch对象


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| head | [head](#head)对象 | 头部处理 | 否 |
| filter | [filter](#filter)对象 | 数据过滤处理 | 否|
| statistical | [statistical](#statistical)对象 | 数据过滤处理 | 否|




<h3 id="head">head对象</h3>


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| heads | string数组 | 需要添加的头部的值 | 是 |
| file | string | 需要处理的文件地址 | 是 |
| save | string | 文件保存地址 | 是 |


<h3 id="filter">filter对象</h3>


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| file | string | 原数据文件 | 是 |
| filter | [condition](#condition)对象数组 | 过滤条件 | 是 |


<h3 id="statistical">statistical对象</h3>


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| file | string | 输出文件 | 是 |
| task | [task](#task)对象数组 | 过滤条件 | 是 |


<h3 id="task">task</h3>


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| file | string | 原数据文件 | 是 |
| name | string | 任务名称 | 是 |
| filter | [condition](#condition)对象 | 过滤条件 | 否 |
| target | [target](#target)对象数组 | 过滤条件 | 是 |


<h3 id="condition">condition对象</h3>


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| file | string | 处理完成后保存地址 | 是 |
| key | string数组 | 获取的字断 | 是 |
| equal | map | 等于过滤条件，key是过滤字断，value是过滤的值 | 否 |
| equal_list | map | 多值等于过滤条件, key是过滤字断，value是过滤的值的集合 | 否 |
| like | map | 包含过滤条件，key是过滤字断，value是过滤的值 | 否 |
| like_list | map | 包含过滤条件，key是过滤字断，value是过滤的值的集合 | 否 |
| greater | map | 大于过滤条件，key是过滤字断，value是过滤的值的集合 | 否 |
| greater_equal | map | 大于等于过滤条件，key是过滤字断，value是过滤的值的集合 | 否 |
| less | map | 小于过滤条件，key是过滤字断，value是过滤的值的集合 | 否 |
| less_equal | map | 小于等于过滤条件，key是过滤字断，value是过滤的值的集合 | 否 |


<h3 id="target">target</h3>


| 字断 | 类型 | 说明 | 是否必须 |
| :--: | :--: | :--: | :--: |
| key | string | 统计的字断 | 是 |
| fun | string数组 | 执行函数的数组（max：最大值, min：最小值, mean：均值, sum：合计, len：数量） | 是 |



## 例子

```
{
  "head": {
    "heads": [],
    "file": "",
    "save": ""
  },
  "filter": {
    "file": "admob.csv",
    "filter": [
      {
        "file": "admob_filter.csv",
        "key": [
          "data",
          "af_revenue",
          "adapter",
          "country",
          "af_id"
        ],
        "equal": {
          "adapter": "AdMobAdapter"
        },
        "equal_list": {
          "country": [
            "US",
            "PH"
          ]
        },
        "greater": {
          "af_revenue": 0.01
        },
        "less": {
          "af_revenue": 0.05
        }
      }
    ]
  },
  "statistical": {
    "file": "admob_test.txt",
    "task": [
      {
        "file": "admob.csv",
        "name": "AdMobAdapter统计",
        "filter": {
          "equal": {
            "adapter": "AdMobAdapter",
            "data": "2021-08-22"
          },
          "equal_list": {
            "country": [
              "US",
              "PH"
            ]
          },
          "greater": {
            "af_revenue": 0.01
          },
          "less": {
            "af_revenue": 0.05
          }
        },
        "target": [
          {
            "key": "af_revenue",
            "fun": [
              "max",
              "min",
              "mean",
              "sum",
              "len"
            ]
          }
        ]
      }
    ]
  }
}
```