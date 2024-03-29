## 一、使用文档说明：

1. 从 国内「[心知天气](https://www.seniverse.com)」，提供的API接口，抓取杭州本地 当天～第三天的天气概况；
2. 抓取数据，使用自己的个人免费API密钥即可；
3. 仅取，当天天气数据，至 Notion 同步更新，以便做其他笔记的参考数据库；
4. 挂靠github_workflow，国内时间每天早 8～9点更新（由于github外网，存在延迟因素）；
5. 同步更新的数据指标，如下所示；

## 二、数据示例：

* "daily" # 返回指定days天数的结果
* "date": "2023-09-20" # 日期（该城市的本地时间）
* "text_day": "多云" # 白天天气现象文字
* "code_day": "4" # 白天天气现象代码
* "text_night": "晴" # 晚间天气现象文字
* "code_night": "0" # 晚间天气现象代码
* "high": "26" # 当天最高温度
* "low": "17" # 当天最低温度
* "precip": "0" # 降水概率，范围0~1，单位百分比（目前仅支持国外城市）
* "wind_direction": "" # 风向文字
* "wind_direction_degree": "255" # 风向角度，范围0~360
* "wind_speed": "9.66" # 风速，单位km/h（当unit=c时）、mph（当unit=f时）
* "wind_scale": "" # 风力等级
* "rainfall": "0.0" # 降水量，单位mm
* "humidity": "76" # 相对湿度，0~100，单位为百分比
