import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation


def animate(data, step):
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='opruga', artist='Matplotlib', comment='-')
    writer = FFMpegWriter(fps=120, metadata=metadata)

    fig = plt.figure()

    plt.plot(data["range"], data["position"])
    opruga, = plt.plot([], [], 'ro', markersize=10)

    with writer.saving(fig, "spring_animation.mp4", 100):
        for i in range(0, len(data["range"]), step):
            x0 = 0.5  # data["range"][i]
            y0 = data["position"][i]
            opruga.set_data(x0, y0)
            writer.grab_frame()
