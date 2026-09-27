import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

def main():
    width = 256 
    height = 256

    r = np.linspace(0, 1, width)[None, :]
    print(f"{r.shape=}\t{r=}")
    g = np.linspace(0, 1, height)[:, None]
    print(f"{g.shape=}\t{g=}")

    img = np.zeros((height, width, 3), dtype=np.uint8)
    print(f"{img.shape=}")

    print(f"img[..., i].shape={img[..., 0].shape}")

    print(f"{2.999*r=}")
    print(f"{2.999*g=}")

    img[..., 0] = (2.999*r).astype(np.uint8)
    img[..., 1] = (2.999*g).astype(np.uint8)

    print(f"{img[..., 0]=}")
    print(f"{img[..., 1]=}")

    print(f"{img=}")

    plt.imshow(img)
    plt.axis('off')
    plt.show()


    for j in tqdm(range(height)):
        for i in range(width):
            r = float(i) / (width - 1)        
            g = float(j) / (height - 1)
            b = 0.0

            ir = int(255.999*r)
            ig = int(255.999*g)
            ib = int(255.999*b)

            print(f"{ir} {ig} {ib}")


if __name__ == "__main__":
    main()