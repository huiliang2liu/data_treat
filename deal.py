import json
import csv
import pandas as pd
import sys
import numpy as np


def add_head(keys, input_file, output_file):
    """
    添加表头
    :param keys: 表头列表
    :param input_file: 输入文件
    :param output_file: 输出文件
    :return:
    """
    with open(output_file, 'w') as c_f:
        csv_f = csv.writer(c_f)
        csv_f.writerow(keys)
        with open(input_file, 'r') as re:
            c_f.writelines(re.readlines())


def filter_equal(input_pd, filter_params):
    """
    等于过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'equal' not in filter_params:
        return input_pd
    equal = filter_params['equal']
    pd_f = input_pd
    for eq in equal.keys():
        value = equal[eq]
        pd_f = pd_f[pd_f[eq] == value]
    return pd_f


def filter_like(input_pd, filter_params):
    """
    包含条件过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'like' not in filter_params:
        return input_pd
    like = filter_params['like']
    pd_f = input_pd
    for li in like.keys():
        value = like[li]
        pd_f = pd_f[pd_f[li].str.contains(value)]
    return pd_f


def filter_equal_list(input_pd, filter_params):
    """
    多个等于过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'equal_list' not in filter_params:
        return input_pd
    equal_list = filter_params['equal_list']
    if len(equal_list) <= 0:
        return input_pd
    pd_f = input_pd
    values = None
    for key in equal_list.keys():
        value = equal_list[key]
        for va in value:
            pd_f_ = pd_f[pd_f[key] == va]
            if values is not None:
                values = np.vstack((values, pd_f_.values))
            else:
                values = pd_f_.values
    return pd.DataFrame(values, columns=pd_f.keys())


def filter_like_list(input_pd, filter_params):
    """
    多个包含过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'like_list' not in filter_params:
        return input_pd
    like_list = filter_params['like_list']
    if len(like_list) <= 0:
        return input_pd
    pd_f = input_pd
    values = None
    for key in like_list.keys():
        value = like_list[key]
        for va in value:
            pd_f_ = pd_f[pd_f[key].str.contains(va)]
            if values is not None:
                values = np.vstack((values, pd_f_.values))
            else:
                values = pd_f_.values
    return pd.DataFrame(values, columns=pd_f.keys())


def filter_greater(input_pd, filter_params):
    """
    大于过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'greater' not in filter_params:
        return input_pd
    greater = filter_params['greater']
    pd_f = input_pd
    for key in greater.keys():
        value = greater[key]
        pd_f = pd_f[pd_f[key] > value]
    return pd_f


def filter_greater_equal(input_pd, filter_params):
    """
    大于等于过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'greater_equal' not in filter_params:
        return input_pd
    greater_equal = filter_params['greater_equal']
    pd_f = input_pd
    for key in greater_equal.keys():
        value = greater_equal[key]
        pd_f = pd_f[pd_f[key] >= value]
    return pd_f


def filter_less(input_pd, filter_params):
    """
    小于过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'less' not in filter_params:
        return input_pd
    less = filter_params['less']
    pd_f = input_pd
    for key in less.keys():
        value = less[key]
        pd_f = pd_f[pd_f[key] < value]
    return pd_f


def filter_less_equal(input_pd, filter_params):
    """
    小于等于过滤
    :param input_pd: 原数据
    :param filter_params: 过滤条件
    :return: 过滤后的数据
    """
    if 'less_equal' not in filter_params:
        return input_pd
    less_equal = filter_params['less_equal']
    pd_f = input_pd
    for key in less_equal.keys():
        value = less_equal[key]
        pd_f = pd_f[pd_f[key] <= value]
    return pd_f


def filter_fun(input_pd, filter_params):
    pd_f = input_pd
    pd_f = filter_equal(pd_f, filter_params)
    pd_f = filter_like(pd_f, filter_params)
    pd_f = filter_equal_list(pd_f, filter_params)
    pd_f = filter_like_list(pd_f, filter_params)
    pd_f = filter_greater(pd_f, filter_params)
    pd_f = filter_greater_equal(pd_f, filter_params)
    pd_f = filter_less(pd_f, filter_params)
    pd_f = filter_less_equal(pd_f, filter_params)
    return pd_f


def deal(input_pd, filter_params):
    pd_f = input_pd
    key = filter_params['key']
    file_ = filter_params['file']
    with open(file_, 'w') as f_:
        csv_f = csv.writer(f_)
        csv_f.writerow(key)
        pd_f = filter_fun(pd_f, filter_params)
        size = len(pd_f)
        for i in range(size):
            values = []
            for ke in key:
                values.append(pd_f[ke].values[i])
            csv_f.writerow(values)


def filter_(filter_params):
    """
    使用说明：默认批处理文件在脚本目录下batch.json文件
    命令：python3 deal.py
    指定批处理文件的脚本文件
    命令:python3 deal.py batch.json
    """
    file_ = filter_params['file']
    save_file = None
    if 'save_file' in filter_params:
        save_file = filter_params['save_file']
    heads = None
    if 'heads' in filter_params:
        heads = filter_params['heads']
    if heads and len(heads) > 0:
        print("正在添加头部")
        add_head(heads, file_, save_file)
        print("头部添加完成")
        file_ = save_file
    filter_list = filter_params['filter']
    pd_f = pd.read_csv(file_)
    for item in filter_list:
        print('开始处理:', item, sep='')
        deal(pd_f, item)
        print('处理完成:', item, sep='')


def fun(pd_f, fun_list):
    line = []
    # "max", "min", "mean", "sum", "len"
    for fun_name in fun_list:
        if 'max' == fun_name:
            line.append('最大值:%s' % pd_f.max())
            continue
        if 'min' == fun_name:
            line.append('最小值:%s' % pd_f.min())
            continue
        if 'mean' == fun_name:
            line.append('均值:%s' % pd_f.mean())
            continue
        if 'sum' == fun_name:
            line.append("合计:%s" % pd_f.sum())
            continue
        if 'len' == fun_name:
            line.append('数量:%s' % len(pd_f))
            continue
    return line


def statistical(statistical_params):
    file_ = statistical_params['file']
    task = statistical_params['task']
    with open(file_, 'w') as f_:
        for t in task:
            file_ = t['file']
            name = t['name']
            target = t['target']
            f_.writelines('%s\n' % name)
            pd_f = pd.read_csv(file_)
            if 'filter' in t:
                pd_f = filter_fun(pd_f, t['filter'])
            for tar in target:
                pd_f_ = pd_f[tar['key']]
                line = fun(pd_f_, tar['fun'])
            f_.writelines('\t%s\n' % ','.join(line))
    pass


if __name__ == '__main__':
    """
    使用说明：默认批处理文件在脚本目录下batch.json文件
    命令：python3 deal.py
    指定批处理文件的脚本文件
    命令:python3 deal.py batch.json
    """
    file = 'batch.json'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    with open(file, 'r') as f:
        fil = json.load(f)
    if 'filter' in fil:
        filter_(fil['filter'])
    if 'statistical' in fil:
        statistical(fil['statistical'])
