import cv2
import urllib


def getImg(args):
    """
    :return 画像データ(ndarray)
    """
    if args.mode == "net":
        # インターネットから画像をダウンロード
        urllib.request.urlretrieve(args.img_url, args.fname)
        # 画像を読み込み
        img = cv2.imread(args.fname)  # (H,W,3)

    elif args.mode == "local":
        img = cv2.imread(args.fpath)

    return img


def drawText(img, text, x, y):
    """
    画面に文字列を描画
    """
    cv2.putText(
        img,
        text=text,
        org=(x, y),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.6,
        color=(0, 255, 0),
        thickness=4,
        lineType=cv2.LINE_4,
    )
    cv2.putText(
        img,
        text=text,
        org=(x, y),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.6,
        color=(0, 0, 0),
        thickness=2,
        lineType=cv2.LINE_4,
    )


def drawLine(img, x1, y1, x2, y2, color):
    cv2.line(
        img,
        (x1, y1),
        (x2, y2),
        color,
        thickness=2,
        lineType=cv2.LINE_AA,
    )