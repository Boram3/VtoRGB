import subprocess
import os

def vtobmps(video_path : str, output_dir : str, w : int, h : int) -> int:
    """
    # Video to Bmps.
    Store the frames as Bmp resized as `w`:`h` to `output_dir`
    """

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if w < 0 or h < 0:
        print("bad request")
        return 2
    
    # FFmpeg command to extract frames as RGB images (PNG format)
    command = [
        'ffmpeg',
        '-i', video_path,               # Input video
        '-vf',
        f'scale={w}:{h},'
        'format=rgb24,'
        'fps=1',
        f'{output_dir}/fb%d.bmp'      # Output: [fp{NUMBER}.bmp]
    ]
    
    try:
        subprocess.run(command, check=True, stderr=subprocess.PIPE, universal_newlines=True)
        print(f"Frames extracted to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return 1

    return 0

def bmptobin(dir_bmps: str, path_out: str, bmphsz : int = 54) -> int:
    """
    # Bmp to Binary
    Convert frames to binaries.
    """


    frames = []


    for item in os.listdir(dir_bmps):
        if item.startswith("fb") and item.endswith(".bmp"):
            frames.append(item)
            pass
        pass

    frames.sort(key=lambda x : int(x[2::].split(".bmp")[0]))
    frames_len = len(frames)

    with open(f"{path_out}", "wb") as _out:
        for i in range(frames_len):
            print(f"Operation number {i}")
            print(f"\tOpening file: {frames[i]}")
            with open(f"{dir_bmps}/{frames[i]}", "rb") as _readf:
                _out.write(_readf.read()[bmphsz::])
                pass
            pass
        pass

    print("over")

    return 0

def vtobin(vd_path : str, dir_workaround : str, path_out : str, w: int = 640, h: int = 480) -> tuple[int, int]:
    a = vtobmps(vd_path, dir_workaround, w, h);
    if a != 0:
        return (a, -1)

    b = bmptobin(dir_workaround, path_out)

    if b != 0:
        return (a, b)

    return (0, 0)
