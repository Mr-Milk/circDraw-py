# -*- coding: utf-8 -*-
#name = "circDraw"

import numpy as np
import matplotlib
from matplotlib import patches
import matplotlib.pyplot as plt
from colour import Color

class circDraw:
    def __init__(self, bsj_start_color='green', bsj_end_color='red'):
        self.__palette = ["#8FD16F", "#108757", "#0B3A42", "#FF404A", "#5CA0F2", "#FF881D", '#e30067', '#924900', '#ab9c00',
                          '#ccd0d2', '#075800', '#5e0094', '#f28600', '#a327ea', '#ff8cc6', '#d60000', '#fff97a', '#ff0081', '#8aa0ae',
                          '#87d1ff', '#7f00b8', '#2ab3e7', '#bd0056', '#0c9200', '#ffe85b', '#d27400', '#3f2e27', '#846a5b', '#004ac7',
                          '#490063', '#ff5757', '#007aea', '#88cc66', '#ff4848', '#73aeff', '#ae5800', '#c1b900', '#c36cff', '#39b03b',
                          '#244c66', '#9c0000', '#6d0000', '#877400', '#002065', '#000cae', '#ecd600', '#ff44a2', '#ffa254', '#ff0000',
                          ]  # set default palette
        self.__mod_color = {'m6a': '#E98B2A',
                            'm5c': '#E16B8C',
                            'm1a': '#64363C',
                            'pu': '#ffa12c',
                            '2ome': '#1a6f00',
                            'mre': '#6D2E5B',
                            'rbp': "#2B5F75",
                            'orf': '#516E41'}
        self.__len_pal = len(self.__palette)  # how many color we have?
        self.__bsj_start_color = 'green'  # setting color of bsj start site
        self.__bsj_end_color = 'red'  # setting color of bsj end site
        self.__circ_center = (4.5, 4.5)
        self.__circ_low = None
        self.__circ_up = None

    def __validate_line(self, line, line_count, plot='circ_on_chr'):
        init = True
        check_start_end = int(line[0]) < int(
            line[1])  # check if start < end and int
        if plot == 'circ_on_chr':
            types = ['circ', 'exon', 'intron', 'gene']
        elif plot == 'mod_on_circ':
            types = ['circ', 'exon', 'intron', 'm6a', 'm5c',
                     'm1a', 'pu', '2ome', 'mre', 'rbp', 'orf']
        check_type = line[2].lower() in types

        if len(line) > 4:
            try:
                test_color = Color(line[4]).hex  # check color input format
            except:
                print('\033[1;31mWarning\033[0m: Wrong input in line',
                      line_count, ': color')
                init = False

        if check_start_end:
            pass
        else:
            print('\033[1;31mWarning\033[0m: Wrong input in line',
                  line_count, ': start, end')
            init = False

        if check_type:
            pass
        else:
            print('\033[1;31mWarning\033[0m: Wrong input in line',
                  line_count, ': Type')
            init = False

        return init

    def __process_data(self, file):
        f = open(file, 'r')
        col = len(f.readline().strip().split(','))
        user_color = False

        # check if user customize color input
        if col > 4:
            user_color = True

        # compile into standard data format
        data, cords, line_count = {'circ': [],
                                   'exon': [], 'intron': [], 'gene': []}, [], 0
        if user_color:
            for line in f.readlines():
                line_count += 1
                l = line.strip().split(',')
                if self.__validate_line(l, line_count):
                    data[l[2].lower()].append(l)
                    cords.append(int(l[0]))
                    cords.append(int(l[1]))
                else:
                    pass
        else:
            p = 0
            for line in f.readlines():
                line_count += 1
                l = line.strip().split(',')
                if self.__validate_line(l, line_count):
                    l.append(self.__palette[p])
                    data[l[2].lower()].append(l)
                    p += 1
                    cords.append(int(l[0]))
                    cords.append(int(l[1]))
                    if p >= self.__len_pal:
                        p = 0
                else:
                    pass

        # set value
        self.__data = data
        self.__low = min(cords)
        self.__up = max(cords)
        self.__ran = self.__up - self.__low

    def __draw_semi_circle(self, ax, x, y, width, linewidth=0.8, rotate=0):
        '''
        x,y is the left endpoint of semicircle
        '''
        xCord = x + width/2
        height = width/2
        s = patches.Arc((xCord, y), width=width,
                        height=height,
                        theta1=rotate,
                        theta2=rotate+180,
                        linewidth=linewidth,
                        alpha=0.8
                        )
        ax.add_patch(s)

    def __draw_rectangle(self, ax, x, y, height, width, color):
        '''
        The right center coordinate of rectangle(x, y)
        '''
        xCord = x - width/2
        yCord = y - width/2
        r = patches.Rectangle((xCord, yCord), height, width,
                              facecolor=color, edgecolor='none', zorder=10)
        ax.add_patch(r)

    def set_palette(self, palette):
        new_palette = []
        error_count = 0
        if type(palette) is list:
            if len(palette) >= 5:
                for i in palette:
                    try:
                        # check if the input color format is correct
                        new_palette.append(Color(i).hex)
                    except:
                        error_count += 1
            else:
                print('Palette require at least 5 color.')
        else:
            print('The palette input is a list')

        if error_count == len(palette):
            pass
        else:
            self.__palette = new_palette

        if error_count > 0:
            print('\033[1;31mWarning\033[0m:',
                  error_count, 'invalid color input.')
        self.__len_pal = len(self.__palette)

    def set_mod_palette(self, palette):
        error_count = 0
        for i in self.__mod_color.keys():
            try:
                self.__mod_color[i.lower()] = palette[i]
            except:
                error_count += 1
        print('\033[1;31mWarning\033[0m:', error_count, 'invalid color input.')

    def circ_on_chr(self, file, title='circDraw', dpi=300, save='png', show=True, size=(10, 5)):
        # process data
        self.__process_data(file)

        # set up the canvas
        fig = plt.figure(dpi=dpi, figsize=size)
        ax = fig.add_subplot(111, aspect='auto')
        ax.set_axis_off()
        ax.set_ylim(bottom=-1, top=5)
        ax.set_xlim(left=-0.5, right=10.5)
        plt.title(title)

        # draw chromosome skeleton
        self.__chr_y = 0.1
        x1, y1 = [-1.1, 11.1], [self.__chr_y, self.__chr_y]
        plt.plot(x1, y1, marker='o', linewidth=0.2, color='black')

        opt = {'gene': [0.08, -0.4, 'heavy'], 'intron': [0.02, -0.2,
                                                         'regular'], 'exon': [0.12, -0.2, 'regular'], 'circ': []}
        for c in opt.keys():
            data = self.__data[c]
            for d in data:
                x = 10*(int(d[0]) - self.__low)/self.__ran
                x_end = 10*(int(d[1]) - self.__low)/self.__ran
                width = x_end - x
                if c == 'circ':  # draw circ
                    self.__draw_rectangle(
                        ax, x + 0.06, self.__chr_y, 0.03, 0.25, self.__bsj_start_color)
                    self.__draw_rectangle(
                        ax, x_end + 0.06, self.__chr_y, 0.03, 0.25, self.__bsj_end_color)
                    self.__draw_semi_circle(
                        ax, x - 0.05, self.__chr_y + 0.17, width)
                    ax.text(x + width/2, width/4 + 0.5, d[3], fontsize=8,
                            horizontalalignment='center', verticalalignment='center')
                else:
                    color = '#000000' if c == 'intron' else d[4]
                    self.__draw_rectangle(
                        ax, x, self.__chr_y, width, opt[c][0], color)
                    ax.text(x + width/2, opt[c][1], d[3], fontsize=8, fontweight=opt[c][2],
                            horizontalalignment='center', verticalalignment='center', color=color)

        if show != None:
            filename = 'circDraw.' + str(save)
            plt.savefig(filename, dpi=dpi)
        if show:
            plt.show()
            plt.close()

#======================= drawing mod_on_circ components ===========================#

    def __draw_ring(self, ax, start, end, color, kind='exon'):
        wid = {'exon': [3, 0.4, color], 'intron': [2.83, 0.05, 'black']}
        ring = patches.Wedge(self.__circ_center, wid[kind][0], start,
                             end, width=wid[kind][1], facecolor=wid[kind][2])
        ax.add_patch(ring)

    def __draw_sec(self, ax, r, start, end, kind):
        opt = {'mre': self.__mod_color['mre'],
               'rbp': self.__mod_color['rbp'],
               'orf': self.__mod_color['orf']}
        sec = patches.Wedge(self.__circ_center, r, start,
                            end, width=0.2, facecolor=opt[kind])
        ax.add_patch(sec)

    def __draw_mod(self, ax, where, r, kind):
        # opt : [shape, size, color, rotation_angle]
        opt = {'m6a': ['\u25CF', 8, self.__mod_color['m6a'], 0],  # circle
               'm5c': ['\u25B2', 8, self.__mod_color['m5c'], 90+where+3], # tri
               'm1a': ['\u25A0', 8, self.__mod_color['m1a'], where+3],  # square
               'pu': ['\u002B', 8, self.__mod_color['pu'], where+3],  # plus sign
               '2ome': ['\u2726', 10, self.__mod_color['2ome'], where]}  # star

        x = self.__circ_center[0] + r*np.cos(np.radians(where))
        y = self.__circ_center[1] + r*np.sin(np.radians(where))
        aes = opt[kind]
        ax.text(x, y, aes[0], fontsize=aes[1], color=aes[2],
                horizontalalignment='center', verticalalignment='center', rotation=aes[3], alpha=0.85)

    def __process_circ_mod(self, file):
        f = open(file, 'r')
        col = len(f.readline().strip().split(','))
        user_color = False

        # check if user customize color input
        if col > 4:
            user_color = True

        # compile into standard data format
        data, line_count = {'circ': [], 'exon': [], 'intron': [], 'mod': []}, 0

        if user_color:
            for line in f.readlines():
                line_count += 1
                l = line.strip().split(',')
                if self.__validate_line(l, line_count, plot='mod_on_circ'):
                    try:
                        data[l[2].lower()].append(l)
                    except:
                        data['mod'].append(l)
                else:
                    pass
        else:
            p = 0
            for line in f.readlines():
                line_count += 1
                l = line.strip().split(',')
                if self.__validate_line(l, line_count, plot='mod_on_circ'):
                    l.append(self.__palette[p])
                    try:
                        data[l[2].lower()].append(l)
                    except:
                        data['mod'].append(l)
                    p += 1
                    if p >= self.__len_pal:
                        p = 0
                else:
                    pass
        
        # sorted exons/introns from start to end
        exons = sorted([[int(x[0]), int(x[1])] + x[2:]
                        for x in data['exon'] + data['intron']], key=lambda x: x[0])
        
        #print(exons)
        
        circs_components, circ_ran = [], 0
        for circ in data['circ']:
            start, end = int(circ[0]), int(circ[1])
            circ_info = {'name': circ[3],
                         'start': start,
                         'end': end,
                         'exons': []}
            for exon in exons:
                e_start, e_end = int(exon[0]), int(exon[1])
                if (e_start < start) & (e_end > start):
                    exon[0] = start
                elif (start <= e_start) & (e_end <= end):
                    pass
                elif (e_start < end) & (end < e_end):
                    exon[1] = end
                elif (e_start < start) & (e_end > end):
                    exon[0] = start
                    exon[1] = end
                e_start, e_end = int(exon[0]), int(exon[1])
                circ_ran += e_end - e_start
                exon.append([])

                for mod in data['mod']:
                    mod_start, mod_end = int(mod[0]), int(mod[1])

                    if (mod_start >= e_start) & (mod_end <= e_end):
                        mod[0], mod[1] = mod_start, mod_end
                        exon[-1].append(mod)
                
                #print(exon)
                
                circ_info['exons'].append(exon)

            circs_components.append(circ_info)

        # set value
        self.__circ_data = circs_components
        self.__circ_ran = circ_ran

        # return self.__circ_data
    def __legend_mod(self, ax, xy, types):
        opt = {'m6a': ['\u25CF', self.__mod_color['m6a'], 'm6A'],  # circle
               'm5c': ['\u25B2', self.__mod_color['m5c'], 'm5C'],  # triangle
               'm1a': ['\u25A0', self.__mod_color['m1a'], 'm1A'],  # square
               'pu': ['\u002B', self.__mod_color['pu'], 'pseudo-U'],  # plus sign
               '2ome': ['\u2726', self.__mod_color['2ome'], '2-O-Me'],
               'mre': ['\u25AC', self.__mod_color['mre'], 'MRE'],
               'rbp': ['\u25AC', self.__mod_color['rbp'], 'RBP'],
               'orf': ['\u25AC', self.__mod_color['orf'], 'ORF'], }

        h = 0.25 * len(types)
        position = (xy[0], xy[1] - h)
        ax.add_patch(patches.FancyBboxPatch(
            position, 1.3, 2, boxstyle='round,pad=0.15', fill=False, edgecolor='grey'))

        init, step = xy[1]-0.15, 0.25

        for i in range(0, len(types)):
            ax.text(xy[0], init - i*step, opt[types[i]][0], fontsize=10, color=opt[types[i]][1],
                    horizontalalignment='left', verticalalignment='center')
            ax.text(xy[0] + 0.27, init - i*step - 0.01, opt[types[i]][2], fontsize=8, color=opt[types[i]][1],
                    horizontalalignment='left', verticalalignment='center')

    def mod_on_circ(self, file, dpi=300, save='png', show=True, size=(7, 7), sep_mod=False):
        self.__process_circ_mod(file)

        for i in self.__circ_data:
            name = i['name']

            fig = plt.figure(dpi=dpi, figsize=size)
            ax = fig.add_subplot(111, aspect='auto')
            ax.set_axis_off()
            ax.set_ylim(bottom=0, top=10)
            ax.set_xlim(left=0, right=10)
            ax.text(self.__circ_center[0], 9, name, fontsize=12, color='black',
                    horizontalalignment='center', verticalalignment='center')

            tail, r, f, mods, fs = 90, 3.11, 2.5, {}, {}
            for exon in i['exons']:
                low, up = exon[0], exon[1]
                ran = up - low
                start = tail
                end = 360*(ran)/self.__circ_ran + start
                tail = end
                self.__draw_ring(ax, start, end, exon[4], kind=exon[2])
                for mod in exon[5]:
                    mod_start = (end - start)*(mod[0] - low)/ran + start
                    mod_end = (end - start)*(mod[1] - low)/ran + start
                    mod_name = mod[2].lower()
                    if mod_name in ['m6a', 'm5c', 'm1a', 'pu', '2ome']:
                        try:
                            mod_r = mods[mod_name]
                        except:
                            mods[mod_name] = r
                            mod_r = mods[mod_name]
                            if sep_mod:
                                r += 0.05
                            else:
                                r += 0
                        self.__draw_mod(ax, (mod_start+mod_end)/2, mod_r, kind=mod_name)

                    if mod_name in ['mre', 'rbp', 'orf']:
                        try:
                            f_r = fs[mod_name]
                        except:
                            fs[mod_name] = f
                            f_r = fs[mod_name]
                            f -= 0.25
                        self.__draw_sec(ax, f_r, mod_start,
                                        mod_end, kind=mod_name)

            self.__legend_mod(ax, (8, 9), list(
                mods.keys()) + list(fs.keys()))

            if show != None:
                filename = name + '.' + str(save)
                plt.savefig(filename, dpi=dpi)
            if show:
                plt.show()
                plt.close()