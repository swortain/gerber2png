'''
功能: 
Author: swortain
Date: 2021-08-08 00:08:48
LastEditTime: 2021-08-10 11:54:48
'''
import os, sys

# import argparse
import glob

from gerber import load_layer
from gerber import PCB
from gerber.layers import guess_layer_class
from gerber.render import RenderSettings, theme
from gerber.render.cairo_backend import GerberCairoContext

# def parseArgs(args=None):
#     parser = argparse.ArgumentParser(description='convert gerber to png file')
#     parser.add_argument('-f',
#                         '--folder',
#                         help='folder path of GERBER files',
#                         required=True,
#                         default=None)
#     parser.add_argument('-o',
#                         '--output',
#                         help='output path',
#                         required=False,
#                         default=None)

#     return parser.parse_args(args)

if __name__ == '__main__':
    # val = parseArgs(sys.argv[1:])

    # files = glob.glob(val.folder + '/*')
    files = glob.glob('./gerbers/*')

    if not os.path.exists('./output'):
        os.makedirs('./output')

    ctx = GerberCairoContext()
    color_settings = RenderSettings(color=theme.COLORS['white'], alpha=1)
    back_settings = RenderSettings(color=theme.COLORS['black'], alpha=0)

    pcb = PCB.from_directory('./gerbers/')
    pcb_bounds = pcb.board_bounds

    # Render PCB top view
    ctx.render_layers(pcb.top_layers,
                      './output/pcb_top.png',
                      theme.THEMES['default'],
                      max_width=800,
                      max_height=600)

    # Render PCB bottom view
    ctx.render_layers(pcb.bottom_layers,
                      './output/pcb_bottom.png',
                      theme.THEMES['default'],
                      max_width=800,
                      max_height=600)

    # Render copper layers only
    ctx.render_layers(pcb.copper_layers + pcb.drill_layers,
                      './output/pcb_transparent_copper.png',
                      theme.THEMES['Transparent Copper'],
                      max_width=800,
                      max_height=600)

    # TODO: 兼容eagle自带的CAM生成的gerber文件，这里只能兼容嘉立创的CAM生成的文件
    for file in files:
        print(file)
        print(guess_layer_class(file))

        if guess_layer_class(file) == 'bottom':  # bottom cpooer
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/copper_bottom.png')

        if guess_layer_class(file) == 'top':  # top cpooer
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/copper_top.png')

        if guess_layer_class(file) == 'bottomsilk':  # bottom silkscreen
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/silkscreen_bottom.png')

        if guess_layer_class(file) == 'topsilk':  # top silkscreen
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/silkscreen_top.png')

        if guess_layer_class(file) == 'bottompaste':  # bottom solderpaste
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/solderpaste_bottom.png')

        if guess_layer_class(file) == 'toppaste':  # top solderpaste
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/solderpaste_top.png')

        if guess_layer_class(file) == 'bottommask':  # bottom soldermask
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/soldermask_bottom.png')

        if guess_layer_class(file) == 'topmask':  # top soldermask
            layer = load_layer(file)
            ctx.clear()
            ctx.render_layer(layer,
                             bounds=pcb_bounds,
                             settings=color_settings,
                             bgsettings=back_settings,
                             filename='./output/soldermask_top.png')

    print('finished!')