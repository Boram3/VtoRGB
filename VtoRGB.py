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
        '-vf', f'scale={w}:{h},format=rgb24',          # Ensure RGB format
        "fps=1", 
        f'{output_dir}/fb%d.bmp'      # Output: [fp{NUMBER}.bmp]
    ]
    
    try:
        subprocess.run(command, check=True, stderr=subprocess.PIPE, universal_newlines=True)
        print(f"Frames extracted to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return 1

    return 0

def bmptobin(dir_bmps: str, dir_out: str, fc : int, bmphsz : int = 54) -> int:
    """
    # Bmp to Binary
    Convert frames to binaries.
    """

    if fc <= 0:
        print("Bad value")
        return 2

    frames = []


    for item in os.listdir(dir_bmps):
        item_full = f"{dir_bmps}/{item}"
        if item.startswith("fb") and item.endswith(".bmp"):
            frames.append(item_full)
            pass

    frames_len = len(frames) - fc + 1

    if frames_len <= 0:
        print("Too few")
        return 1

    for i in range(frames_len):
        with open(f"{dir_out}/b{i}.seq", "wb") as _out:
            for j in range(fc):
                with open(frames[i + j], "rb") as _readf:
                    _out.write(_readf.read()[bmphsz::])

    return 0

def vtobin(vd_path : str, dir_workaround : str, dir_out : str, w: int, h : int, fc : int) -> tuple[int, int]:
    a = vtobmps(vd_path, dir_workaround, w, h);
    if a != 0:
        return (a, -1)

    b = bmptobin(dir_workaround, dir_out, fc)

    if b != 0:
        return (a, b)

    return (0, 0)
