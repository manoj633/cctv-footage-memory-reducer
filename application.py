import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
print(cap)

bgst = cv2.createBackgroundSubtractorMOG2()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter("cctv.avi", fourcc, 30, size)
ret = True

if __name__ == "__main__":
    while ret:
        ret, frame = cap.read()

        date_ = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_COMPLEX

        frame = cv2.putText(
            frame, date_, (10, 50), font, 0.5, (255, 255, 255), 0, cv2.LINE_AA
        )

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        dst = bgst.apply(frame)

        dst = np.array(dst, np.int8)

        cv2.imshow("Gray Frame", gray)

        for i in range(1):
            if np.count_nonzero(dst) < 2500:  # use this value to adjust the sensitivity

                print("No Motion Detected")
                continue

            else:

                print("Frame Motion detected : %s" % str(datetime.datetime.now()))
                out.write(frame)
                continue

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()
