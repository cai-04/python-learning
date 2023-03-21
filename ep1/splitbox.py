import numpy as np
# 宽度分箱函数
def width_binning(data, width):
    bins = []
    start = 0
    while start < len(data):
        bins.append(data[start:start+width])
        start += width
    return bins

# 深度分箱函数
def depth_binning(data, depth):
    bins = []
    for i in range(depth):
        bins.append([data[j] for j in range(i, len(data), depth)])
    return bins

# 均值平滑函数
def mean_smoothing(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size//2 or i >= len(data)-window_size//2:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1])/window_size)
    return smoothed_data

# 中值平滑函数
def median_smoothing(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size//2 or i >= len(data)-window_size//2:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sorted(data[i-window_size//2:i+window_size//2+1])[window_size//2])
    return smoothed_data

# 边界平滑函数
def boundary_smoothing(data, window_size):
    smoothed_data = []
    for i in range(len(data)):
        if i < window_size//2 or i >= len(data)-window_size//2:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(sum(data[i-window_size//2:i+window_size//2+1]+[data[i]])/(window_size+1))
    return smoothed_data

# 规范化函数
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x-min_val)/(max_val-min_val) for x in data]
    return normalized_data

# 读入数据
file_name = '1.txt'
data = np.loadtxt(file_name, dtype= 'int32', delimiter=',')
print("原始数据：", data)

# 宽度分箱
width = int(input("请输入宽度："))
width_bins = width_binning(data, width)
print("宽度分箱结果：", width_bins)

# 深度分箱
depth = int(input("请输入深度："))
depth_bins = depth_binning(data, depth)
print("深度分箱结果：", depth_bins)

# 均值平滑
mean_smoothed_data = []
for bin in depth_bins:
    mean_smoothed_data += mean_smoothing(bin, 3)
print("均值平滑结果：", mean_smoothed_data)


# 中值平滑
median_smoothed_data = []
for bin in depth_bins:
    median_smoothed_data += median_smoothing(bin, 3)
print("中值平滑结果：", median_smoothed_data)

# 边界平滑
boundary_smoothed_data = []
for bin in depth_bins:
    boundary_smoothed_data += boundary_smoothing(bin, 3)
print("边界平滑结果：", boundary_smoothed_data)

# 规范化
normalized_data = normalize(data)
print("规范化结果：", normalized_data)
