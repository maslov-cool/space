from PIL import Image, ImageDraw


def benefit(file_name, w, col):
    col = list(col)
    im = Image.new("RGB", (16 * w, 24 * w), col[0])
    drawer = ImageDraw.Draw(im)
    drawer.ellipse((-8 * w, 8 * w, 24 * w, 40 * w), outline='#ccc', width=int(w / 5))
    drawer.ellipse(((0, int((16 * w))), (int(16 * w), int(32 * w))), col[1])
    drawer.ellipse(((int(4 * w), int(18 * w)), (int(7 * w), int(20 * w))), col[2])
    drawer.ellipse(((int(12 * w), int(20 * w)), (int(14 * w), int(23 * w))), col[2])
    drawer.polygon(((int(4.5 * w), int(7 * w)), (int(4.5 * w), int(9 * w)), (int(11.5 * w), int(9 * w)), (int(11.5 * w),
                                                                                                          int(7 * w))),
                   col[3])
    drawer.polygon(((int(11.5 * w), int(7 * w)),
                    (int(11.5 * w), int(9 * w)),
                    (int(13.5 * w), int(8 * w))),
                   col[4])
    drawer.polygon(((int(4.5 * w), int(6.5 * w)),
                    (int(4.5 * w), int(7.5 * w)),
                    (int(2.5 * w), int(6.5 * w))),
                   col[5])
    drawer.polygon(((int(4.5 * w), int(8.5 * w)),
                    (int(4.5 * w), int(9.5 * w)),
                    (int(2.5 * w), int(9.5 * w))),
                   col[5])
    im.save(file_name)


col = "#595959", "#fc0", "#ddd", "#0070c0", "#00b050", "#c09000"
benefit("path.png", 20, col)