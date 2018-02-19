import sys
val = sys.argv
if len(val) > 1:
    val = val[1]
    try:
        val = int(val)
        if val < 0:
            raise ValueError
        print("{} H, {} M".format(val//60, val%60))
    except ValueError:
        print("ValueError: Input number cannot be negative")
