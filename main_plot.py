# !/usr/bin/env python

import os
import time
import random
import numpy as np
from config import *
from file2key import main
import matplotlib.pyplot as plt


def gene_file(sizes):
    for i in sizes:
        if i > 100:
            file = "%sMB" % (i // 1024)
        else:
            file = "%sKB" % i
        with open("statics/sample_%s" % file, "wb") as f:
            f.write(os.urandom(1024 * i))


def bar_plot(res_x, res_y, width=0.46, color="dodgerblue"):
    lens = len(res_x)
    fig, ax = plt.subplots()
    ind = np.arange(lens)
    res = ax.bar(ind, res_y, width, color=color, alpha=1)
    ax.set_xticklabels(res_x)
    ax.set_xticks(ind)
    ax.set_ylim([0, res_y[-1] + 20])
    ax.set_title("Time of the key pair generation")
    ax.set_ylabel("Time in milliseconds (ms)")
    ax.set_xlabel("Modulus size of $N$ (bits)")
    for i in res:
        h = i.get_height()
        ax.text(i.get_x() + width / 2, 1.03 * h, "%s" % h, ha='center', va='bottom')
    plt.show()


def get_bar_plot():
    res = []
    for x in xlist:
        sum = 0
        for _ in range(10):
            t = time.time()
            main("file", "statics/sample_1KB", x)
            sum += time.time() - t
        res.append(round(sum * 100, 2))
    results["1KB"] = res
    bar_plot(xlist, res)


def line_plot(res_x):
    ls = ["-", "--", "-.", ":"]
    marker = ["o", "v", "^", "D", "x", "+"]
    fig, ax = plt.subplots()
    ind = np.arange(len(ylist))
    ax.set_ylim([results[res_x[0]][0] - 20, results[res_x[-1]][-1] + 20])
    for i in res_x:
        ax.plot(ind, results[i], marker=random.choice(marker), ls=random.choice(ls), label="%s bits" % i)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.set_xticks(ind)
    ax.set_xticklabels(ylist)
    ax.set_xlabel("File size of $m$ (KB)")
    ax.set_ylabel("Time in milliseconds (ms)")
    ax.set_title("Time of the key pair generation")
    plt.show()


def get_line_plot():
    for x in xlist:
        res = []
        for y in ylist:
            sum = 0
            for _ in range(10):
                t = time.time()
                main("file", "statics/sample_%s" % y, x)
                sum += time.time() - t
            res.append(round(sum * 100, 2))
        results[x] = res
    line_plot(xlist)


def linem_plot():
    res = []
    ls = ["-", "--", "-.", ":"]
    marker = ["o", "v", "^", "D", "x", "+"]
    fig, ax = plt.subplots()
    ind = np.arange(len(xlist))
    ax.set_ylim([0, 1000])
    res.append(ax.plot(ind, results["1KB"], marker="^", ls="-.", label="Laptop"))
    res.append(ax.plot(ind, results["1KBM"], marker="v", ls="--", label="Mobile phone"))
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    ax.set_xticks(ind)
    ax.set_xticklabels(xlist)
    ax.set_xlabel("Modulus size of $N$ (bits)")
    ax.set_ylabel("Time in milliseconds (ms)")
    ax.set_title("Time of the key pair generation")
    for k in ["1KB", "1KBM"]:
        for a, b in zip(ind, results[k]):
            ax.text(a, b + 10, str(b), ha='center', va='bottom')
    plt.show()


def get_linem_plot():
    res = []
    for x in xlist:
        sum = 0
        for _ in range(10):
            t = time.time()
            main("file", "statics/sample_1KB", x)
            sum += time.time() - t
        res.append(round(sum * 100, 2))
    results["1KB"] = res
    linem_plot()

if __name__ == '__main__':
    # gene_file([1, 10, 100, 1024, 10240, 10240])
    # get_bar_plot()
    # get_line_plot()
    # get_linem_plot()
