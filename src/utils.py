from PIL import Image

import glob


def convert_gif_to_pngs(gif_file, target_file_path):
  with Image.open(gif_file) as im:

    for i in range(im.n_frames):
          im.seek(i)
          im.save(f'{target_file_path}_{i:02d}.png')

  
      
def regenerate_gif(png_files='static/figs/fill_gif/fill_*.png', save_to='static/gifs/fill_gif_custom.gif', total_duration = 3.0, loop=0):

  files= sorted(glob.glob(png_files))
  images = [Image.open(f) for f in files]

  num_frames = len(images)

  duration_per_frame = 1000*total_duration/num_frames

  images[0].save(save_to, save_all=True, append_images=images[1:], optimize=False, duration=duration_per_frame, loop=loop)

regenerate_gif()