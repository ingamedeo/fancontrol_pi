echo $(/opt/vc/bin/vcgencmd measure_temp | awk -F"=|'" '{print $2}')﻿
