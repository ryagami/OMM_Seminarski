import numpy as np
import matplotlib as plt
import matplotlib.animation as manimation


def animate(data):
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='opruga', artist='Matplotlib', comment='-')
    writer = FFMpegWriter(fps=15, metadata=metadata)

    fig = plt.figure()

    opruga, = plt.plot([], [], 'ro', markersize = 10)

    with writer.saving(fig, "spring_animation.mp4"):
        for i in data["range"]:
            x0 = data["range"][i]
            y0 = data["position"][i]
            opruga.set_data(x0, y0)
            writer.grab_frame()
